# Email Tool

## Introduction

The Email Tool is a Python program that provides a menu-driven interface for sending and reading emails using the `smtplib` and `easyimap` libraries. It allows users to send single emails, read emails, and send mass emails to a list of recipients specified in a CSV file.

## Features

- **Sending a Single Email**: Compose and send a single email to a specified recipient.

- **Reading Emails**: Connect to an email account using IMAP to retrieve and view emails. Option to analyze the sentiment of the email using a `SentimentAnalyzer`.

- **Sending Mass Emails**: Send emails to a list of recipients specified in a CSV file. Option to attach files.

- **Exiting the Program**: Option to exit the program.

## Prerequisites

Before running the program, make sure you have the following:

- Python 3.x installed on your system.
- Required libraries: `smtplib`, `ssl`, `email`, `easyimap`, `sys`, `os`, `csv`, `getpass`.

## How to Use

1. Clone the repository or download the Python file (`mailer.py`).

2. Open a terminal or command prompt and navigate to the directory containing `mailer.py`.

3. Run the program by executing the following command:

   ```bash
   python mailer.py
