import os

import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.environ.get("MYSQL_PASSWORD", "Treasure2018#"),
    database="flask_assignment",
)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/submit-form", methods=["POST"])
def submit_form():
    # Receive the form data
    full_name = request.form.get("full_name")
    email = request.form.get("email")
    age = request.form.get("age")
    city = request.form.get("city")
    country = request.form.get("country")
    occupation = request.form.get("occupation")
    hobby = request.form.get("hobby")
    programming_language = request.form.get("programming_language")
    online_hours = request.form.get("online_hours")
    entertainment = request.form.get("entertainment")

    # Process the data
    full_name = full_name.strip()
    email = email.strip()
    age = int(age)
    city = city.strip()
    country = country.strip()
    occupation = occupation.strip()
    hobby = hobby.strip()
    programming_language = programming_language.strip()
    online_hours = int(online_hours)
    entertainment = entertainment.strip()

    # Store the data in MySQL
    query = """
        INSERT INTO users
        (full_name, email, age, city, country, occupation,
         hobby, programming_language, online_hours, entertainment)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor = db.cursor()
    cursor.execute(
        query,
        (
            full_name,
            email,
            age,
            city,
            country,
            occupation,
            hobby,
            programming_language,
            online_hours,
            entertainment,
        ),
    )
    db.commit()
    cursor.close()

    return render_template("success.html", full_name=full_name)


@app.route("/users")
def users():
    cursor = db.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    users = cursor.fetchall()
    cursor.close()

    return render_template("users.html", users=users)


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG", "0") == "1")


 # create a peremetre 
 