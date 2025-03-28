import streamlit as st
import pandas as pd
from services.groq_api import GroqAPI
from services.database import Database

st.title("KYB Report Generator")

# User Input for API Key
api_key = st.text_input("Enter your Groq API Key", type="password")
company_name = st.text_input("Enter Company Name")

if st.button("Generate Report"):
    if not api_key:
        st.error("API Key is required!")
    elif not company_name:
        st.error("Company name is required!")
    else:
        groq_client = GroqAPI(api_key)
        report = groq_client.generate_kyb_report(company_name)

        if report:
            st.text_area("Generated KYB Report", report, height=300)

            # Save report to Excel
            df = pd.DataFrame([[company_name, report]], columns=["Company Name", "KYB Report"])
            excel_path = "data/kyb_reports.xlsx"

            try:
                existing_data = pd.read_excel(excel_path)
                updated_data = pd.concat([existing_data, df], ignore_index=True)
            except FileNotFoundError:
                updated_data = df  # Create new if file doesn't exist

            updated_data.to_excel(excel_path, index=False)
            st.success(f"Report saved to {excel_path}")

        else:
            st.error("Failed to generate report. Please check API Key.")

# AI Agent Discovery Section
st.header("AI Agent Discovery & Inventory Check")

agent_name = st.text_input("Enter AI Agent Name")
agent_version = st.text_input("Enter Version")
agent_features = st.text_area("Enter Key Features")
agent_use_case = st.text_area("Enter Intended Use Cases")

if st.button("Save Agent Information"):
    db = Database()
    existing_agent = db.check_agent_exists(agent_name, agent_version)

    if existing_agent:
        db.update_agent(agent_name, agent_version, agent_features, agent_use_case)
        st.success(f"Agent '{agent_name}' updated successfully!")
    else:
        db.save_new_agent(agent_name, agent_version, agent_features, agent_use_case)
        st.success(f"New AI Agent '{agent_name}' added successfully!")
