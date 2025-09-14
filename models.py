# models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Customer(db.Model):
    customerId = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50))
    lastName = db.Column(db.String(50))
    address = db.Column(db.String(255))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    zipCode = db.Column(db.String(10))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)
    driverLicense = db.Column(db.String(50))
    dateOfBirth = db.Column(db.Date)
    membershipNumber = db.Column(db.String(50))

class Car(db.Model):
    registrationNumber = db.Column(db.String(50), primary_key=True)
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    year = db.Column(db.Integer)
    color = db.Column(db.String(30))
    mileage = db.Column(db.Integer)
    fuelType = db.Column(db.String(30))
    transmission = db.Column(db.String(30))
    passengerCapacity = db.Column(db.Integer)
    dailyRate = db.Column(db.Float)
    weeklyRate = db.Column(db.Float)
    monthlyRate = db.Column(db.Float)
    availability = db.Column(db.Boolean, default=True)
    lastServiceDate = db.Column(db.Date)

class Rental(db.Model):
    rentalId = db.Column(db.Integer, primary_key=True)
    customerId = db.Column(db.Integer, db.ForeignKey('customer.customerId'))
    carId = db.Column(db.String(50), db.ForeignKey('car.registrationNumber'))
    startDate = db.Column(db.Date)
    endDate = db.Column(db.Date)
    rentalFee = db.Column(db.Float)
    returned = db.Column(db.Boolean, default=False)
    pickupLocation = db.Column(db.String(100))
    returnLocation = db.Column(db.String(100))
    rentalAgreement = db.Column(db.String(255))

class Payment(db.Model):
    paymentId = db.Column(db.Integer, primary_key=True)
    rentalId = db.Column(db.Integer, db.ForeignKey('rental.rentalId'))
    amount = db.Column(db.Float)
    paymentDate = db.Column(db.Date, default=datetime.utcnow)
    paymentMethod = db.Column(db.String(50))
    transactionId = db.Column(db.String(100))
    paymentStatus = db.Column(db.String(50))

class Invoice(db.Model):
    invoiceNumber = db.Column(db.String(50), primary_key=True)
    paymentId = db.Column(db.Integer, db.ForeignKey('payment.paymentId'))
    invoiceDate = db.Column(db.Date, default=datetime.utcnow)
    totalAmount = db.Column(db.Float)
    dueDate = db.Column(db.Date)
    taxAmount = db.Column(db.Float)
    discountAmount = db.Column(db.Float)

class Location(db.Model):
    locationId = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    zipCode = db.Column(db.String(10))
    phoneNumber = db.Column(db.String(20))

class Booking(db.Model):
    bookingId = db.Column(db.Integer, primary_key=True)
    customerId = db.Column(db.Integer, db.ForeignKey('customer.customerId'))
    carId = db.Column(db.String(50), db.ForeignKey('car.registrationNumber'))
    bookingDate = db.Column(db.Date, default=datetime.utcnow)
    pickupDate = db.Column(db.Date)
    returnDate = db.Column(db.Date)
    bookingStatus = db.Column(db.String(50))
    bookingReference = db.Column(db.String(100))

class Review(db.Model):
    reviewId = db.Column(db.Integer, primary_key=True)
    customerId = db.Column(db.Integer, db.ForeignKey('customer.customerId'))
    carId = db.Column(db.String(50), db.ForeignKey('car.registrationNumber'))
    rating = db.Column(db.Integer)
    comment = db.Column(db.String(255))
    reviewDate = db.Column(db.Date, default=datetime.utcnow)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)
