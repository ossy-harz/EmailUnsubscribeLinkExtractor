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
```

## Setup
1. Enable IMAP in Gmail settings.
2. Create a `.env` file with:
   ```makefile
   EMAIL=your_email@gmail.com
   PASSWORD=your_email_password
   ```
3. Run the script:
   ```bash
   python extractor.py
   ```

## Logging
The script logs connection status, link extraction, and visit attempts.

## Note
Ensure your credentials are stored securely in the `.env` file.
