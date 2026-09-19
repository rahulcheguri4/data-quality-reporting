import pandas as data_frame
# Load CSV file
file_name = "data.csv"
data = data_frame.read_csv(file_name)

print("DATA QUALITY REPORT")
print("=" * 50)

# Basic information
print("\n1. DATASET INFORMATION")
print("-" * 30)

print("Rows:", len(data))
print("Columns:", len(data.columns))

# Missing values
print("\n2. MISSING VALUES")
print("-" * 30)

missing = data.isnull().sum()

for column in data.columns:
    print(column, ":", missing[column])

# Duplicate rows
print("\n3. DUPLICATE ROWS")
print("-" * 30)

duplicates = data.duplicated().sum()

print("Duplicate rows:", duplicates)

# Data types
print("\n4. DATA TYPES")
print("-" * 30)

for column in data.columns:
    print(column, ":", data[column].dtype)

# Unique values
print("\n5. UNIQUE VALUES")
print("-" * 30)

for column in data.columns:
    print(column, ":", data[column].nunique())

# Completeness
print("\n6. COMPLETENESS")
print("-" * 30)

total_cells = data.shape[0] * data.shape[1]
missing_cells = data.isnull().sum().sum()

completeness = ((total_cells - missing_cells) / total_cells) * 100

print("Completeness:", round(completeness, 2), "%")

# Uniqueness
print("\n7. UNIQUENESS")
print("-" * 30)

unique_cells = data.nunique().sum()
total_columns = len(data.columns)

uniqueness = (unique_cells / (len(data) * total_columns)) * 100

print("Uniqueness:", round(uniqueness, 2), "%")

# Suspicious records
print("\n8. SUSPICIOUS RECORDS")
print("-" * 30)

# Negative salary
if "Salary" in data.columns:
    negative_salary = data[data["Salary"] < 0]

    print("\nNegative Salary Records:")
    print(negative_salary)

# Invalid age
if "Age" in data.columns:
    numeric_age = pd.to_numeric(data["Age"], errors="coerce")

    invalid_age = data[
        numeric_age.isnull() | 
        (numeric_age < 0)
    ]

    print("\nInvalid Age Records:")
    print(invalid_age)

# Save report
with open("quality_report.txt", "w") as report:

    report.write("DATA QUALITY REPORT\n")
    report.write("=" * 50 + "\n\n")

    report.write("Rows: " + str(len(data)) + "\n")
    report.write("Columns: " + str(len(data.columns)) + "\n\n")

    report.write("MISSING VALUES\n")
    report.write(str(missing))
    report.write("\n\n")

    report.write("DUPLICATE ROWS\n")
    report.write(str(duplicates))
    report.write("\n\n")

    report.write("DATA TYPES\n")
    report.write(str(data.dtypes))
    report.write("\n\n")

    report.write("UNIQUE VALUES\n")
    report.write(str(data.nunique()))
    report.write("\n\n")

    report.write("COMPLETENESS\n")
    report.write(str(round(completeness, 2)) + "%\n")

print("\n" + "=" * 50)
print("Report created successfully!")
print("File: quality_report.txt")