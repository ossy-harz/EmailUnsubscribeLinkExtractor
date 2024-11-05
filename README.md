# Email Unsubscribe Link Extractor

This Python script connects to a Gmail inbox, searches for emails with "unsubscribe" links, visits each link, and saves the links to a text file.

## Features
- Connects to Gmail via IMAP
- Extracts and visits unsubscribe links
- Logs actions and errors
- Saves links in `links.txt`

## Requirements
- Python 3.6+
- Gmail account with IMAP enabled
- Environment variables for credentials

## Dependencies
Install required packages:
```bash
pip install python-dotenv beautifulsoup4 requests

Setup
Enable IMAP in Gmail settings.
Create a .env file with:
makefile
Copy code
EMAIL=your_email@gmail.com
PASSWORD=your_email_password
Run the script:
bash
Copy code
python extractor.py
Logging
The script logs connection status, link extraction, and visit attempts.

Note
Ensure your credentials are stored securely in the .env file.

### Instructions for Use
1. Create a new file named `README.md` in your project directory.
2. Copy and paste the formatted text above into the `README.md` file.
3. Commit your changes and push them to your GitHub repository.

This README provides clear instructions and important information about your project, making it easier for others to understand and use!

