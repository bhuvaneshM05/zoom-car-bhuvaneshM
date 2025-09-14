# app.py
from flask import Flask
from models import db, Car, Customer, Rental, Payment, Invoice, User
from routes import init_routes
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rental.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'

db.init_app(app)
init_routes(app)

if __name__ == '__main__':
    if os.path.exists("rental.db"):
        os.remove("rental.db")
        print("🗑️ Old database deleted.")

    with app.app_context():
        db.create_all()

        if not Car.query.first():
            sample_cars = [
                Car(
                    registrationNumber="MH12AB1234",
                    make="Toyota", model="Innova", year=2020, color="White",
                    mileage=30000, fuelType="Diesel", transmission="Manual",
                    passengerCapacity=7, dailyRate=2500.0, weeklyRate=15000.0,
                    monthlyRate=55000.0, availability=True, lastServiceDate=datetime(2024, 12, 15)
                ),
                Car(
                    registrationNumber="DL10XY9876",
                    make="Honda", model="City", year=2021, color="Black",
                    mileage=15000, fuelType="Petrol", transmission="Automatic",
                    passengerCapacity=5, dailyRate=2000.0, weeklyRate=12000.0,
                    monthlyRate=45000.0, availability=True, lastServiceDate=datetime(2025, 2, 10)
                ),
                Car(
                    registrationNumber="KA05CD5678",
                    make="Hyundai", model="Creta", year=2022, color="Blue",
                    mileage=10000, fuelType="Diesel", transmission="Manual",
                    passengerCapacity=5, dailyRate=2200.0, weeklyRate=13000.0,
                    monthlyRate=47000.0, availability=True, lastServiceDate=datetime(2025, 1, 20)
                )
            ]
            db.session.add_all(sample_cars)
            db.session.commit()
            print("🚗 Sample cars seeded.")

        if not User.query.first():
            users = [
                User(username="admin", password="admin123", role="admin"),
                User(username="agent", password="agent123", role="agent"),
                User(username="customer", password="cust123", role="customer")
            ]
            db.session.add_all(users)
            db.session.commit()
            print("👥 Sample users seeded.")

    app.run(debug=True)

