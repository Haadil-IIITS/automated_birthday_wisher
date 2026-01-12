# 🎂 Automated Birthday Wisher

> **⚠️ IMPORTANT CONFIGURATION REQUIRED**
>
> Before running this script, you **must** open `main.py` and update the following variables with your own details:
> * **`email`**: Enter your Gmail address.
> * **`password`**: Enter your Google **App Password** (not your login password).
> * **`senderemail`**: This determines who receives the mail (this is usually automated from the CSV, but check your variables).

A Python automation script that tracks birthdays from a database and sends personalized email wishes automatically. Never miss a friend's birthday again!

![Project Banner]
(placeholder-image.jpg) 


## 📝 Description

This project is an **Automated Birthday Wisher** designed to run daily. It reads a database of friends' birth dates (`dates.csv`), checks if today matches any entries, and automatically sends a custom-formatted email using SMTP.

It uses **Pandas** for efficient data handling and **SMTP** to communicate with Gmail servers securely.

## 🚀 Features

* **Automated Date Checking:** Automatically compares today's date with a CSV database.
* **Personalized Emails:** Pulls the correct name and email address for each person.
* **Template System:** Uses a text file (`letter.txt`) as a template, allowing you to easily change the birthday message without touching the code.
* **Secure Login:** Uses TLS encryption for secure email transmission.

## 🛠️ Libraries Used

* **[Pandas](https://pandas.pydata.org/):** For reading and filtering the CSV data (`dates.csv`).
* **[smtplib](https://docs.python.org/3/library/smtplib.html):** For establishing the connection to the email server and sending the mail.
* **[datetime](https://docs.python.org/3/library/datetime.html):** For retrieving the current day and month.

## 📂 Project Structure

```text
├── dates.csv       # Database containing names, emails, and birth dates
├── letter.txt      # The email body template (uses [name] as placeholder)
├── main.py         # The main Python script
└── README.md       # Project documentation
