![Python](https://img.shields.io/badge/Python-3.x-blue)
![Google Sheets](https://img.shields.io/badge/Google%20Sheets-API-green)
![gspread](https://img.shields.io/badge/gspread-Library-orange)
![OAuth2](https://img.shields.io/badge/OAuth2-Authentication-red)
 
 
 
 # 📊  Google Sheets Data Analyzer 


A simple Python project that reads financial data from a .txt file, analyzes it, and writes both the raw data and statistical insights to Google Sheets automatically.

This project demonstrates how to integrate:

File processing

Data analysis

Google Sheets API automation


 # 🚀 Features
 

✔ Read structured data from a .txt file
✔ Parse names and monetary values
✔ Analyze the dataset to find:

The richest person

The poorest person

The average amount

✔ Automatically write the results to Google Sheets
✔ Generate a clean table inside the spreadsheet


 # 🧠 Example Input


The program expects a file called datos.txt with the following format:

Name,Amount

Example:

Ana,1200.50
Bruno,845.00
Carlos,3000.75
Daniela,450.25
Emilia,1900.00
 # 📈 Example Output (Google Sheets)
Nombre	Dinero
Ana	1200.50
Bruno	845.00
Carlos	3000.75
Daniela	450.25
Analysis
Metric	Result
Más rico	Carlos ($3000.75)
Más pobre	Facundo ($220.10)
Promedio	$1249.85
🛠 Tech Stack

Python

gspread

Google Sheets API

OAuth2 authentication

Libraries used:

gspread
oauth2client

# ⚙️ Installation

## 1️⃣ Clone the repository

git clone https://github.com/SantiagoCrivellaro/google-sheets-data-analyzer.git

cd google-sheets-data-analyzer

## 2️⃣ Install dependencies

pip install gspread oauth2client

## 3️⃣ Setup Google Sheets API

Go to Google Cloud Console

Create a project

Enable:

Google Sheets API

Google Drive API

Create a Service Account

Download the credentials JSON file

Rename it to:

credentials.json

Place it in the root folder of the project.

# 4️⃣ Share the Spreadsheet

Share your Google Sheet with the service account email inside the credentials.json.

Example:

project-name@project-id.iam.gserviceaccount.com

Give it Editor permissions.

# ▶️ Running the Project

Make sure you have:

datos.txt
credentials.json

Then run:

python main.py

Output:

Datos y análisis escritos en columnas A y B de Google Sheets.


# 📂 Project Structure

project
│
├── main.py
├── datos.txt
├── credentials.json
└── README.md





# Author

Santiago Crivellaro

Backend Developer focused on:

Java

Spring Boot

APIs

Microservices

Python

Software Architecture

## GitHub:
https://github.com/SantiagoCrivellaro

## LinkedIn:
https://www.linkedin.com/in/santiago-crivellaro-3372143b6/
