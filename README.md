# AUTOMATED INTEGRATION FLOW - AIF

AIF (Automated Integration Flow) is a **Flask-based web application** designed to centralize and automate the management of **integration projects**, **requests**, and **network nodes** within **Ericsson environments**. It includes **role-based access control**, allowing authorized users to securely manage and monitor integration operations.

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Technologies](#technologies)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)

---

## Overview

The Automated Integration Flow (AIF) provides a centralized platform for engineers and project managers to efficiently manage integration workflows across internal Ericsson systems.

It offers full project lifecycle support—**create**, **update**, **delete**—along with **real-time tracking** of requests and associated nodes. With built-in **role-based access**, AIF improves operational visibility, reduces human error, and ensures secure access to project data.

---

## Features

- User authentication (login/logout)  
- Project listing, creation, editing, and deletion  
- Request overview interface  
- Node details linked to related requests  
- SQLAlchemy-based database integration  
- Role-based access control for secure management  

---

## Installation

### 1. Create and activate a virtual environment:  
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables:
Create a .env file and add your configuration (e.g., SECRET_KEY, DATABASE_URI):

```ruby
USER = your_user
PASSWORD = your_password
HOST = your_host
PORT = your_port
DATABASE = your_database
SSL_CERT = your_cert_path
SSL_DISABLED = False
SECRET_KEY = secret_key
```

### 4. Run the application:

```bash
flask run --debug
```

## Usage
- After running the application, you can access the web interface to:
- Register and log in as a user
- View and manage projects, requests, and nodes
- Perform role-based actions depending on your privileges


## Technologies
- ![Flask](https://flask.palletsprojects.com/en/stable/)
- ![SQLAlchemy](https://www.sqlalchemy.org/)
- ![Flask-Login](https://flask-login.readthedocs.io/en/latest/)
- HTML & Jinja2 Templates  
- [Bootstrap](https://getbootstrap.com/) (optional)
- [MySQL](https://www.mysql.com/)

--- 

## Contributing
Contributions are welcome! Please fork the repository and create a pull request.

--- 

## License
This project is licensed under the MIT License. See the LICENSE file for details.

--- 

## Contact
For questions, feedback, or support:

Ali Al-Kaissi
Mail: ali.al-kaissi@ericsson.com

Mohamad Ayad
mohamad.ayad@ericsson.com
