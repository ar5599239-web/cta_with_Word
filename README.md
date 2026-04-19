# Client Task Automation & Email Reporting System

A Python-based automation tool that processes client task data, generates structured reports, and securely sends them via email with attachments.

# Overview

This project simulates a real-world business workflow where client task data is managed, reported, and distributed automatically.

# The system:

Generates a structured report (Word document)
Sends the report via email with attachment
Secures credentials using environment variables

# Tech Stack

python-os
python-docx
smtplib (SMTP email automation)
python-dotenv

# Features

Generate formatted Word reports
Send automated emails with attachments
Secure credential management using .env
Compatible with Gmail SMTP (App Password authentication)

# Security

Sensitive credentials are stored in a .env file and excluded from version control using .gitignore.

# Output

Generates a Word report (report.docx)
Sends an email with the report attached to the specified recipient

# Challenges & Solutions

SMTP Authentication Errors: Resolved by implementing Gmail App Password authentication.
SSL/TLS Connection Issues: Diagnosed and resolved by configuring correct ports and protocols.
Secure Credential Handling: Implemented .env and .gitignore to prevent sensitive data exposure.

# This project demonstrates:

Python automation for business workflows
Secure handling of sensitive data
Email integration using SMTP protocols
File processing and report generation
Real-world debugging and problem-solving

# Author

Anthony Reyes
Aspiring Python Automation Developer | Cybersecurity Background
