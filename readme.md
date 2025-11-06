#  Attendance Checker (Selenium)

A beginner-friendly Python automation project that uses **Selenium** to log in to a student portal and scrape **attendance information** automatically.  
This project demonstrates how to automate browser tasks, handle logins, and interact with web elements like buttons, inputs, and dropdowns.

---

##  Features

- Automates login using Selenium WebDriver  
- Waits dynamically for elements to load (using `WebDriverWait`)  
- Interacts with dropdowns and buttons  
- Reads sensitive data like passwords from a `.env` file  
- Beginner-friendly and easy to understand  

---

##  Requirements

- Python 3.10 or later  
- Google Chrome (latest version recommended)  
- ChromeDriver (matching your Chrome version)

---

##  Setup Instructions

### Clone the repository

git clone `https://github.com/sout-abhay-kumar/attendance-checker-selenium.git`
cd `attendance-checker-selenium`

### Create a virtual environment

`python -m venv .venv`

### Activate the virtual environment

Windows (PowerShell): `.venv\Scripts\Activate.ps1`
macOS/Linux: `source .venv/bin/activate`

### Install dependencies

`pip install selenium python-dotenv`

### Create a .env file

Create a .env file in the project root directory and add your password: `PASSWORD=your_password_here`

### How to Run the Script

`python web_scrapping.py`

When you run the script:

1. A Chrome window will open automatically.

2. It will fill your login credentials.

3. You manually solve the CAPTCHA and click Login.

4. After login, it navigates to the Attendance page and selects your semester details.

## Disclaimer 

This project automates the process of logging into the [UKTECH University Student Portal](https://online.uktech.ac.in/ums/Student/Account/Login) and viewing attendance reports using **Python** and **Selenium**.

This project does not works on differnt student portal other than UKTECH University Student Portal.
