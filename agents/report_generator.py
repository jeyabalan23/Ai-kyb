from services.groq_api import query_groq
from agents.data_filler import fill_missing_data

def generate_report(company_name):
    data = fill_missing_data(company_name)
    return query_groq(f"Generate KYB report for {data}")
