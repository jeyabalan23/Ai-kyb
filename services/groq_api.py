import requests

class GroqAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"  # Updated URL

    def generate_kyb_report(self, company_name):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "llama3-8b-8192",  # Use an available Groq model
            "messages": [
                {"role": "system", "content": "You are an expert in business intelligence and Know Your Business (KYB) reporting."},
                {"role": "user", "content": f"Generate a KYB report for the company: {company_name}"}
            ],
            "temperature": 0.7
        }

        response = requests.post(self.base_url, headers=headers, json=data)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"Error: {response.json().get('message', 'Unknown error')}"
