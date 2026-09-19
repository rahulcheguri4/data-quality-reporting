# 📊 Data Quality Reporting Tool:
A simple Python tool that profiles a CSV dataset and generates a data quality report. It helps identify missing values, duplicate records, incorrect data types, unique values, and suspicious records.

# 🎯 Objective:
The main objective of this project is to understand and implement basic data-quality assessment techniques used in data analytics and data engineering.

# 🛠️ Technologies Used:
• 🐍 Python
• 🐼 Pandas
• 🔢 NumPy
• 📄 CSV

# ✨ Features:
• Detect missing values
• Identify duplicate rows
• Check column data types
• Count unique values
• Calculate data completeness
• Calculate uniqueness
• Detect suspicious records
• Generate a text-based quality report
• Reusable for different CSV files


# 📁 Project Structure:
data_quality_tool/
│
├── main.py
├── data.csv
├── quality_report.txt
└── README.md
📄 Sample Dataset

# The project uses a CSV file such as:
Name,Age,Email,Salary,City
Rahul,25,rahul@gmail.com,45000,Hyderabad
Priya,28,priya@gmail.com,55000,Chennai
Arun,,arun@gmail.com,40000,Bangalore
Rahul,25,rahul@gmail.com,45000,Hyderabad
Sita,abc,sita@gmail.com,-5000,Delhi
Kiran,30,,60000,Hyderabad
