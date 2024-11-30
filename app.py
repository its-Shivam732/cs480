from flask import Flask, request, jsonify, render_template
import database  # Importing your `database.py` module

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/booking.html')
def booking():
    return render_template('booking.html')

@app.route('/package.html')
def package():
    return render_template('package.html')


# User Routes
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    try:
        result = database.add_user(
            name=data["name"],
            email=data["email"],
            password=data["password"],  # Ensure to hash the password in production
            phone=data["phone"],
            registration_date=data["registration_date"],
        )
        return jsonify({"success": result, "message": "User added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/users/login", methods=["POST"])
def login_user():
    data = request.json
    try:
        user = database.get_user(data["email"], data["password"])
        if user and user["password"] == data["password"]:  # Simplified validation, hash passwords in production
            return jsonify({"message": "Login successful!", "user": user}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/getpopularpkg", methods=["GET"])
def popularpkg():
    try:
        result = database.getPopularPkg()
        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "error"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/popularcity", methods=["GET"])
def popularcity():
    try:
        result = database.popularcity()
        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "error"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/priceperdestination", methods=["GET"])
def sortPricePerDes():
    try:
        result = database.sortPricePerDes()
        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "error"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500




@app.route("/destinations", methods=["GET"])
def get_destination():
    try:
        destination = database.get_destination()
        if destination:
            return jsonify(destination)
        else:
            return jsonify({"error": "Destination not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Booking Routes
@app.route("/bookings", methods=["POST"])
def add_booking():
    data = request.json
    try:
        result = database.add_booking(
            data["user_id"],
            data["packageid"],
            data["bookingdate"],
            data["traveldate"],
            data['bookingstatus'],
        )
        return jsonify({"success": result, "message": "Booking created successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/bookings/<user_id>", methods=["GET"])
def get_booking(user_id):
    try:
        booking = database.get_booking(user_id)
        if booking:
            return jsonify(booking)
        else:
            return jsonify({"error": "Booking not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/bookings/user/<user_id>", methods=["GET"])
def get_bookings_by_user(user_id):
    try:
        bookings = database.get_bookings_by_user(user_id)
        return jsonify(bookings)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/packages/<destinationId>", methods=["GET"])
def get_package(destinationId):
    try:
        package = database.get_package(destinationId)
        if package:
            return jsonify(package)
        else:
            return jsonify({"error": "Package not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/packages/destination/<destination_id>", methods=["GET"])
def get_packages_by_destination(destination_id):
    try:
        packages = database.get_packages_by_destination(destination_id)
        return jsonify(packages)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
