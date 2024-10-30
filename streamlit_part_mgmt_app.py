import streamlit as st
from datetime import date
from database_setup import session, Contract  # Import session and Contract from database_setup.py
from sqlalchemy import select

# Streamlit App Title
st.title("Contract Management System")

# Contract Entry Form
st.header("Add New Contract")
with st.form("new_contract_form"):
    name = st.text_input("Contract Name", value="Cisne Corp")
    status = st.selectbox("Status", ["Pending", "Approved", "Rejected"])
    expiry_date = st.date_input("Expiry Date", min_value=date.today())
    department = st.selectbox("Department", ["Custom Engineering", "Engineering", "Powertrain", "EE Wiring", "Satellite Engineering", "Body"])
    part_number = st.text_input("Part Number")
    part_description = st.text_area("Part Description")
    reason = st.text_area("Reason (optional)")
    
    submitted = st.form_submit_button("Add Contract")

    if submitted:
        # Add new contract to the database
        new_contract = Contract(
            name=name,
            status=status,
            expiry_date=expiry_date,
            department=department,
            part_number=part_number,
            part_description=part_description,
            reason=reason
        )
        session.add(new_contract)
        session.commit()
        st.success("Contract added successfully!")

# Display All Contracts
st.header("All Contracts")

# Query to get all contracts from the database
contracts_query = select(Contract)
contracts = session.execute(contracts_query).scalars().all()

if contracts:
    for contract in contracts:
        st.write(f"**Contract ID**: {contract.id}")
        st.write(f"**Name**: {contract.name}")
        st.write(f"**Status**: {contract.status}")
        st.write(f"**Expiry Date**: {contract.expiry_date}")
        st.write(f"**Department**: {contract.department}")
        st.write(f"**Part Number**: {contract.part_number}")
        st.write(f"**Part Description**: {contract.part_description}")
        st.write(f"**Reason**: {contract.reason}")
        st.markdown("---")
else:
    st.write("No contracts found in the database.")
