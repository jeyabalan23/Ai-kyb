# KYB Report Generator

## Overview
The **KYB Report Generator** is a Streamlit-based web application that generates Know Your Business (KYB) reports using the Groq API. It allows users to enter a company name and API key, generate a KYB report, and download the results in Excel format. Additionally, the application provides AI agent discovery and inventory management capabilities by integrating with a database.

## Features
- **KYB Report Generation:**
  - Fetches company details via Groq API.
  - Displays generated reports in a text area.
  - Saves reports in an Excel file with a unique company name.
  - Provides a downloadable report for users.
- **AI Agent Management:**
  - Allows users to enter AI agent details (name, version, features, use cases, associated company).
  - Saves and updates AI agent data in a database.
  - Ensures structured agent discovery and tracking.

## Installation
### Prerequisites
- Python 3.8+
- Streamlit
- Pandas
- OpenPyXL (for Excel support)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/kyb-report-generator.git
   cd kyb-report-generator
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   streamlit run app.py
   ```

## Usage
1. **Enter API Key & Company Name**
   - Input your **Groq API key** and **Company Name** in the text fields.
   - Click **Generate Report** to fetch and display the KYB report.

2. **Download KYB Report**
   - The report is saved as `{company_name}_kyb_report.xlsx`.
   - Click the **Download** button to retrieve the file.

3. **AI Agent Management**
   - Enter AI Agent details (name, version, features, use cases, associated company).
   - Click **Save Agent Information** to store/update in the database.

## File Structure
```
kyb-report-generator/
│-- app.py                   # Main Streamlit application
│-- services/
│   │-- groq_api.py          # API client for Groq
│   │-- database.py          # Database handler
│-- data/                    # Folder to store generated reports
│-- requirements.txt         # Python dependencies
│-- README.md                # Documentation (this file)
```

## Troubleshooting
- **Error: API Key Required** → Ensure the API key is entered before generating a report.
- **Error: Report Not Generating** → Check if the Groq API is reachable.
- **Error: Database Connection Issues** → Verify database credentials in `database.py`.

## License
This project is licensed under the MIT License.

## Contact
For issues or contributions, please reach out via [GitHub Issues](https://github.com/your-repo/kyb-report-generator/issues).

