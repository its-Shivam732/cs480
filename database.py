import os
from datetime import datetime

import pymysql
import pymysql.cursors


def get_connection():
    """Create and return a new database connection."""
    return pymysql.connect(
        host="localhost",
        user="frontend_user",
        password="your_password",
        database="travel_management_system",
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )


# User-related operations
def add_user( name, email, password, phone, registration_date):
    """Insert a new user."""
    registration_date = datetime.today().date()
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = '''
            INSERT INTO `Users` (name, email, password, phone,user_type, registration_date)
            VALUES (%s, %s, %s, %s, %s, %s)
            '''
            cursor.execute(sql, (name, email, password, phone, 'simple', registration_date))
        connection.commit()
        return True


def get_user(email, password):
    """Fetch user details by user ID."""
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `Users` WHERE `email` = %s and `password`= %s "
            cursor.execute(sql, (email, password))
            return cursor.fetchone()


def delete_user(user_id):
    """Delete a user by user ID."""
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `users` WHERE `user_id` = %s"
            cursor.execute(sql, (user_id,))
        connection.commit()
        return cursor.rowcount > 0


# Transport-related operations
def add_transport(transport_id, transport_type, company_name, seating_capacity, available_seats):
    """Insert a new transport."""
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = '''
            INSERT INTO `transports` (transport_id, transport_type, company_name, seating_capacity, available_seats)
            VALUES (%s, %s, %s, %s, %s)
            '''
            cursor.execute(sql, (transport_id, transport_type, company_name, seating_capacity, available_seats))
        connection.commit()
        return True


def get_transport(transport_id):
    """Fetch transport details by transport ID."""
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `transports` WHERE `transport_id` = %s"
            cursor.execute(sql, (transport_id,))
            return cursor.fetchone()


# Destination-related operations
def add_destination(destination_id, destination_name, city, state, country):
    """Insert a new destination."""
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = '''
            INSERT INTO `destinations` (destination_id, destination_name, city, state, country)
            VALUES (%s, %s, %s, %s, %s)
            '''
            cursor.execute(sql, (destination_id, destination_name, city, state, country))
        connection.commit()
        return True


def get_destination():
    """Fetch destination details by destination ID."""
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `Destination`"
            cursor.execute(sql)
            return cursor.fetchall()


# Booking-related operations
def add_booking( user_id,packageid, booking_date, traveldate, status):
    """Insert a new booking."""
    bookingdate = datetime.today().date()
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = '''
            INSERT INTO `Bookings` (userid, traveldate, bookingdate, packageid, bookingstatus)
            VALUES (%s, %s, %s, %s, %s)
            '''
            cursor.execute(sql, (user_id, traveldate, bookingdate, packageid, status))
        connection.commit()
        return True


def get_booking(user_id):
    """Fetch booking details by booking ID."""
    connection = get_connection()
    current_date = datetime.today().date()
    with connection:
        with connection.cursor() as cursor:
            sql = ("SELECT u.name, b.*, p.package_name, p.duration, p.price, d.*"
                   " FROM Users u join  Bookings b on u.user_id = b.userid join Package p on"
                   " b.packageid=p.packageid join Destination d on d.destinationid = p.destinationid"
                   " WHERE b.userid = %s AND b.traveldate < %s")
            cursor.execute(sql, (user_id,current_date))
            return cursor.fetchall()


def get_bookings_by_user(user_id):
    """Fetch all bookings for a specific user."""
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `bookings` WHERE `user_id` = %s"
            cursor.execute(sql, (user_id,))
            return cursor.fetchall()


def delete_booking(booking_id):
    """Delete a booking by booking ID."""
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `bookings` WHERE `booking_id` = %s"
            cursor.execute(sql, (booking_id,))
        connection.commit()
        return cursor.rowcount > 0


# Package-related operations
def add_package(package_id, package_name, price, duration, destination_id):
    """Insert a new package."""
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = '''
            INSERT INTO `packages` (package_id, package_name, price, duration, destination_id)
            VALUES (%s, %s, %s, %s, %s)
            '''
            cursor.execute(sql, (package_id, package_name, price, duration, destination_id))
        connection.commit()
        return True


def get_package(destinationid):
    """Fetch package details by package ID."""
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT p.*  FROM Package p JOIN Destination d ON p.destinationid = d.destinationid WHERE d.destinationid = %s"
            cursor.execute(sql, (destinationid))
            return cursor.fetchall()


def get_packages_by_destination(destination_id):
    """Fetch all packages for a specific destination."""
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `packages` WHERE `destination_id` = %s"
            cursor.execute(sql, (destination_id,))
            return cursor.fetchall()


def getPopularPkg():
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT pkg.package_name, COUNT(b.bookingid) AS booking_count FROM Package pkg JOIN Bookings b ON pkg.packageid = b.packageid GROUP BY pkg.package_name ORDER BY booking_count DESC LIMIT 5"


            cursor.execute(sql, ())
            return cursor.fetchall()


def popularcity():
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = ("SELECT d.city, COUNT(b.bookingid) AS booking_count FROM Destination d JOIN Package pkg ON "
                   "d.destinationid = pkg.destinationid JOIN Bookings b ON pkg.packageid = b.packageid GROUP BY "
                   "d.city ORDER BY booking_count DESC LIMIT 3")
            cursor.execute(sql, ())
            return cursor.fetchall()


def sortPricePerDes():
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = ("SELECT      d.city AS destination,      pkg.package_name,      pkg.price FROM      Package pkg "
                   " JOIN      Destination d  ON      pkg.destinationid = d.destinationid ORDER BY      d.city,    "
                   "  pkg.price DESC LIMIT 0, 1000")
            cursor.execute(sql, ())
            return cursor.fetchall()