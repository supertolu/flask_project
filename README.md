# Flask User Form Project

This project is a simple Flask application that lets users fill out a form, submit their details, and save the information into a MySQL database. It also includes pages for the home screen, contact page, and a list of saved users.

## Features

- Home page
- Contact page
- User registration form
- Form submission to MySQL database
- Users listing page
- Basic Flask application structure

## Tech Stack

- Python
- Flask
- MySQL
- mysql-connector-python

## Project Structure

```text
flask_project/
├── main.py
├── setpu.sql
├── templates/
│   ├── contact.html
│   ├── form.html
│   ├── home.html
│   ├── suceess.html
│   └── users.html
└── README.md
```

## Database Setup

1. Open MySQL and create the database using the SQL script:

```sql
CREATE DATABASE flask_assignment;

USE flask_assignment;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100),
    email VARCHAR(150),
    age INT,
    city VARCHAR(100),
    country VARCHAR(100),
    occupation VARCHAR(100),
    hobby VARCHAR(150),
    programming_language VARCHAR(50),
    online_hours INT,
    entertainment VARCHAR(100)
);
```

You can run the commands from the file `setpu.sql` in your MySQL client or terminal.

## Environment Configuration

The application connects to MySQL using:

- Host: `localhost`
- User: `root`
- Database: `flask_assignment`

The password is read from the `MYSQL_PASSWORD` environment variable, with a default value defined in the code. For security, it is recommended to set your own password in the environment instead of relying on a hardcoded value.

Example:

```bash
set MYSQL_PASSWORD=your_mysql_password
```

On macOS/Linux:

```bash
export MYSQL_PASSWORD=your_mysql_password
```

## Installation

1. Open the project folder.
2. Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install flask mysql-connector-python
```

## Run the Application

From the project folder, run:

```bash
python main.py
```

Then open the app in your browser:

```text
http://127.0.0.1:5000/
```

## Available Routes

- `/` - Home page
- `/contact` - Contact page
- `/form` - User form
- `/submit-form` - Submits form data to the database
- `/users` - Displays all stored users

## Notes

- The app uses debug mode based on the `FLASK_DEBUG` environment variable.
- You can enable debug mode with:

```bash
set FLASK_DEBUG=1
python main.py
```

or:

```bash
export FLASK_DEBUG=1
python main.py
```

## License

This project is for educational and personal use.
