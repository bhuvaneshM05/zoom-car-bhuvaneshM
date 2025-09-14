# routes.py
from flask import render_template, request, redirect, url_for, flash, session
from models import db, Customer, Car, Rental, Payment, Invoice, Booking, User
from datetime import datetime

def init_routes(app):
    @app.route('/')
    def home():
        cars = Car.query.all()
        return render_template('home.html', cars=cars)

    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            role = request.form['role']
            if User.query.filter_by(username=username).first():
                flash("Username already exists.")
            else:
                new_user = User(username=username, password=password, role=role)
                db.session.add(new_user)
                db.session.commit()
                flash("Account created successfully. Please login.")
                return redirect(url_for('login'))
        return render_template("signup.html")

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(username=username, password=password).first()
            if user:
                session['username'] = user.username
                session['role'] = user.role
                flash(f"Welcome, {user.role}!")
                return redirect(url_for(f"dashboard_{user.role}"))
            else:
                flash("Invalid credentials")
        return render_template("login.html")

    @app.route('/logout')
    def logout():
        session.clear()
        flash("Logged out successfully.")
        return redirect(url_for('login'))

    @app.route('/dashboard/admin')
    def dashboard_admin():
        if session.get('role') != 'admin':
            flash("Unauthorized")
            return redirect(url_for('login'))
        users = User.query.all()
        return render_template("dashboard_admin.html", users=users)

    @app.route('/delete-user/<int:user_id>')
    def delete_user(user_id):
        if session.get('role') != 'admin':
            flash("Unauthorized")
            return redirect(url_for('login'))
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        flash("User deleted successfully.")
        return redirect(url_for('dashboard_admin'))

    @app.route('/dashboard/agent')
    def dashboard_agent():
        if session.get('role') != 'agent':
            flash("Unauthorized")
            return redirect(url_for('login'))
        return render_template("dashboard_agent.html")

    @app.route('/dashboard/customer')
    def dashboard_customer():
        if session.get('role') != 'customer':
            flash("Unauthorized")
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()
        customer = Customer.query.filter_by(email=user.username).first()
        rentals = Rental.query.filter_by(customerId=customer.customerId).all() if customer else []
        return render_template("dashboard_customer.html", rentals=rentals)

    @app.route('/book/<registrationNumber>', methods=['GET', 'POST'])
    def book_car(registrationNumber):
        car = Car.query.get_or_404(registrationNumber)
        if request.method == 'POST':
            customer = Customer.query.filter_by(email=request.form['email']).first()
            if not customer:
                customer = Customer(
                    firstName=request.form['firstName'],
                    lastName=request.form['lastName'],
                    address=request.form['address'],
                    city=request.form['city'],
                    state=request.form['state'],
                    zipCode=request.form['zipCode'],
                    phone=request.form['phone'],
                    email=request.form['email'],
                    driverLicense=request.form['driverLicense'],
                    dateOfBirth=datetime.strptime(request.form['dateOfBirth'], '%Y-%m-%d'),
                    membershipNumber=request.form['membershipNumber']
                )
                db.session.add(customer)
                db.session.commit()

            rental = Rental(
                customerId=customer.customerId,
                carId=car.registrationNumber,
                startDate=datetime.strptime(request.form['startDate'], '%Y-%m-%d'),
                endDate=datetime.strptime(request.form['endDate'], '%Y-%m-%d'),
                pickupLocation=request.form['pickupLocation'],
                returnLocation=request.form['returnLocation'],
                rentalFee=car.dailyRate * int((datetime.strptime(request.form['endDate'], '%Y-%m-%d') - datetime.strptime(request.form['startDate'], '%Y-%m-%d')).days),
                rentalAgreement='LinkToAgreement.pdf'
            )
            car.availability = False
            db.session.add(rental)
            db.session.commit()

            flash('Booking successful!')
            return redirect(url_for('make_payment', rental_id=rental.rentalId))

        return render_template('booking.html', car=car)

    @app.route('/make-payment/<int:rental_id>', methods=['GET', 'POST'])
    def make_payment(rental_id):
        rental = Rental.query.get_or_404(rental_id)
        if request.method == 'POST':
            payment = Payment(
                rentalId=rental_id,
                amount=rental.rentalFee,
                paymentMethod=request.form['method'],
                transactionId="TXN" + str(datetime.now().timestamp()).replace('.', ''),
                paymentStatus="Successful"
            )
            db.session.add(payment)
            db.session.commit()

            invoice = Invoice(
                invoiceNumber="INV" + str(payment.paymentId),
                paymentId=payment.paymentId,
                totalAmount=payment.amount,
                dueDate=datetime.now(),
                taxAmount=payment.amount * 0.18,
                discountAmount=0.0
            )
            db.session.add(invoice)

            rental.returned = True
            car = Car.query.get(rental.carId)
            car.availability = True

            db.session.commit()
            flash("Payment successful, car marked as returned and available.")
            return redirect(url_for('dashboard_customer'))

        return render_template('make_payment.html', rental=rental)

    @app.route('/return/<registrationNumber>')
    def return_car(registrationNumber):
        car = Car.query.get_or_404(registrationNumber)
        car.availability = True
        db.session.commit()
        flash('Car returned successfully.')
        return redirect(url_for('home'))
