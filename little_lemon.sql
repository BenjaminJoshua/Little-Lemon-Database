-- Create Database
CREATE DATABASE IF NOT EXISTS little_lemon;
USE little_lemon;

-- Bookings Table
CREATE TABLE IF NOT EXISTS Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,
    TableNumber INT NOT NULL,
    GuestFirstName VARCHAR(100) NOT NULL,
    GuestLastName VARCHAR(100) NOT NULL,
    BookingTime TIME NOT NULL,
    EmployeeID INT
);

-- Orders Table
CREATE TABLE IF NOT EXISTS Orders (
    OrderID INT PRIMARY KEY,
    MenuID INT,
    CustomerID INT,
    TotalCost DECIMAL(10, 2),
    Quantity INT
);

-- Menu Table
CREATE TABLE IF NOT EXISTS Menu (
    MenuID INT PRIMARY KEY,
    Cuisine VARCHAR(100),
    StarterName VARCHAR(100),
    CourseName VARCHAR(100),
    DrinkName VARCHAR(100),
    DessertName VARCHAR(100)
);

-- Sample Data for Verification
INSERT INTO Bookings (TableNumber, GuestFirstName, GuestLastName, BookingTime, EmployeeID) 
VALUES (5, 'John', 'Doe', '19:00:00', 1);
