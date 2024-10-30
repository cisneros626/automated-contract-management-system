import pandas as pd
import random
from datetime import date
from database_setup import session, Contract  # Import session and Contract from database_setup.py

# Load data from the Excel (or CSV) file
excel_file = 'part_no_desc_dummy_data.csv'  # Replace with your actual file path
df = pd.read_csv(excel_file, usecols=["part_no", "part_desc"])

# Filter out rows with missing values in part_no or part_desc
df = df.dropna(subset=["part_no", "part_desc"])

# Function to create contracts from Excel data
def generate_contracts_from_excel(dataframe):
    contracts = []
    for _, row in dataframe.iterrows():
        contract = Contract(
            name="Cisne Corp",
            status=random.choice(["Pending", "Approved", "Rejected"]),
            expiry_date=date.today(),
            department=random.choice(["Custom Engineering", "Engineering", "Powertrain", "EE Wiring", "Satellite Engineering", "Body"]),
            part_number=row["part_no"],
            part_description=row["part_desc"],
            reason=""
        )
        contracts.append(contract)
    return contracts

# Insert contracts into the database
contracts = generate_contracts_from_excel(df)
session.bulk_save_objects(contracts)
session.commit()

print("Database populated with data from Excel!")