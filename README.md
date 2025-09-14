# 🚗 Car Rental Management System

A comprehensive web-based car rental management system built with Flask, featuring role-based authentication, booking management, payment processing, and automated invoicing.

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [User Roles](#user-roles)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### Core Functionality
- **Car Inventory Management** - Add, view, and manage vehicle fleet
- **Customer Registration** - Complete customer profile management
- **Booking System** - Real-time car availability and reservation
- **Payment Processing** - Integrated payment system with transaction tracking
- **Invoice Generation** - Automated billing with tax calculations
- **Return Management** - Car return processing and availability updates

### User Management
- **Role-Based Access Control** - Admin, Agent, and Customer roles
- **Authentication System** - Secure login/logout functionality
- **Dashboard Interfaces** - Customized dashboards per user role
- **Session Management** - Secure session handling

### Business Features
- **Dynamic Pricing** - Daily, weekly, and monthly rental rates
- **Availability Tracking** - Real-time car availability status
- **Rental History** - Complete rental transaction records
- **Service Tracking** - Vehicle maintenance date tracking
- **Multi-location Support** - Pickup and return location management

## 🛠️ Tech Stack

### Backend
- **Flask** - Python web framework
- **Flask-SQLAlchemy** - ORM for database operations
- **SQLite** - Lightweight database for data storage
- **Python 3.x** - Programming language

### Frontend
- **Jinja2** - Template engine for dynamic HTML
- **HTML5** - Markup language
- **CSS3** - Styling and layout
- **Bootstrap-inspired** - Responsive design elements

### Database
- **SQLite** - File-based database (`rental.db`)
- **SQLAlchemy ORM** - Object-relational mapping

## 📁 Project Structure

```
car/
├── app.py                 # Main application entry point
├── models.py              # Database models and schema
├── routes.py              # URL routes and business logic
├── README.md              # Project documentation
├── instance/
│   └── rental.db          # SQLite database file
├── static/
│   └── css/
│       └── styles.css     # Application styling
├── templates/             # HTML templates
│   ├── base.html          # Base template
│   ├── home.html          # Homepage
│   ├── login.html         # Login page
│   ├── signup.html        # Registration page
│   ├── booking.html       # Car booking form
│   ├── make_payment.html  # Payment processing
│   ├── dashboard_admin.html    # Admin dashboard
│   ├── dashboard_agent.html    # Agent dashboard
│   ├── dashboard_customer.html # Customer dashboard
│   └── [other templates]
└── __pycache__/           # Python cache files
```

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd car
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask flask-sqlalchemy
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Open your web browser
   - Navigate to `http://localhost:5000`

## 💻 Usage

### First Time Setup
When you run the application for the first time, it will:
- Create a new SQLite database
- Seed sample car data
- Create default user accounts

### Default User Accounts
| Username | Password | Role |
|----------|----------|------|
| admin | admin123 | admin |
| agent | agent123 | agent |
| customer | cust123 | customer |

### Basic Workflow

1. **Browse Cars** - View available vehicles on the homepage
2. **Register/Login** - Create account or login with existing credentials
3. **Book a Car** - Select a car and fill booking details
4. **Make Payment** - Process payment for the rental
5. **Manage Rentals** - View and manage bookings from dashboard

## 🗄️ Database Schema

### Core Models

#### User
- Authentication and role management
- Fields: `id`, `username`, `password`, `role`

#### Customer
- Customer profile information
- Fields: `customerId`, `firstName`, `lastName`, `email`, `phone`, etc.

#### Car
- Vehicle inventory management
- Fields: `registrationNumber`, `make`, `model`, `year`, `dailyRate`, etc.

#### Rental
- Rental transaction records
- Fields: `rentalId`, `customerId`, `carId`, `startDate`, `endDate`, etc.

#### Payment
- Payment processing and tracking
- Fields: `paymentId`, `rentalId`, `amount`, `paymentMethod`, etc.

#### Invoice
- Automated billing system
- Fields: `invoiceNumber`, `paymentId`, `totalAmount`, `taxAmount`, etc.

## 👥 User Roles

### Admin
- **User Management** - Create, view, and delete user accounts
- **System Administration** - Full system access and control
- **Dashboard Access** - Administrative dashboard with user overview

### Agent
- **Rental Management** - Handle customer bookings and returns
- **Customer Service** - Assist customers with rental processes
- **Dashboard Access** - Agent-specific dashboard interface

### Customer
- **Car Browsing** - View available vehicles and pricing
- **Booking Management** - Create and manage rental bookings
- **Payment Processing** - Handle rental payments
- **Rental History** - View past and current rentals

## 🔗 API Endpoints

### Authentication
- `GET /` - Homepage with car listings
- `GET/POST /login` - User authentication
- `GET/POST /signup` - User registration
- `GET /logout` - User logout

### Dashboards
- `GET /dashboard/admin` - Admin dashboard
- `GET /dashboard/agent` - Agent dashboard
- `GET /dashboard/customer` - Customer dashboard

### Booking & Rental
- `GET/POST /book/<registrationNumber>` - Car booking process
- `GET/POST /make-payment/<rental_id>` - Payment processing
- `GET /return/<registrationNumber>` - Car return process

### User Management (Admin Only)
- `GET /delete-user/<user_id>` - Delete user account

## 🎯 Key Features Explained

### Automatic Database Seeding
The application automatically creates sample data including:
- 3 sample cars (Toyota Innova, Honda City, Hyundai Creta)
- Default user accounts for testing
- Proper database relationships

### Dynamic Pricing Calculation
```python
rental_fee = car.dailyRate × number_of_days
tax_amount = rental_fee × 0.18  # 18% tax
```

### Car Availability Management
- Cars are marked unavailable when booked
- Automatically marked available when returned
- Real-time availability status on homepage

### Session-Based Authentication
- Secure session management
- Role-based access control
- Automatic redirection based on user role

## 🔧 Configuration

### Database Configuration
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rental.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

### Security Configuration
```python
app.secret_key = 'supersecretkey'  # Change in production
```

## 🚀 Development

### Running in Development Mode
The application runs in debug mode by default:
```python
app.run(debug=True)
```

### Database Reset
The application automatically deletes and recreates the database on each run during development.

## 📝 Future Enhancements

- [ ] Email notifications for bookings
- [ ] Advanced search and filtering
- [ ] Car images and gallery
- [ ] Rating and review system
- [ ] Mobile responsive design
- [ ] Payment gateway integration
- [ ] Rental agreement PDF generation
- [ ] Advanced reporting and analytics

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For support and questions:
- Create an issue in the repository
- Contact the development team

---

**Built with ❤️ using Flask and Python**
