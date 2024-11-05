import imaplib
import email
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables once
load_dotenv()
username = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

def connect_to_mail():
    """Connect to Gmail's IMAP server and login with credentials."""
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(username, password)
        mail.select("inbox")
        logging.info("Connected to Gmail inbox.")
        return mail
    except imaplib.IMAP4.error as e:
        logging.error("Failed to connect to the mail server: %s", e)
        raise

def extract_links_from_html(html_content):
    """Extract unsubscribe links from HTML content."""
    soup = BeautifulSoup(html_content, "html.parser")
    return [link["href"] for link in soup.find_all("a", href=True) if "unsubscribe" in link["href"].lower()]

def click_links(links):
    """Visit each link in the list using a requests session."""
    with requests.Session() as session:
        for link in links:
            try:
                response = session.get(link)
                if response.status_code == 200:
                    logging.info("Successfully visited %s", link)
                else:
                    logging.warning("Failed to visit %s (status code: %s)", link, response.status_code)
            except requests.RequestException as e:
                logging.error("Error visiting %s: %s", link, e)

def decode_content(content):
    """Decode email content, falling back if necessary."""
    try:
        return content.decode("utf-8")
    except UnicodeDecodeError:
        return content.decode("iso-8859-1")

def search_for_email():
    """Search inbox for emails containing 'unsubscribe' in the body and extract unsubscribe links."""
    mail = connect_to_mail()
    try:
        _, search_data = mail.search(None, '(BODY "unsubscribe")')
        email_ids = search_data[0].split()
        all_links = []

        for num in email_ids:
            _, data = mail.fetch(num, "(RFC822)")
            msg = email.message_from_bytes(data[0][1])

            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/html":
                        html_content = decode_content(part.get_payload(decode=True))
                        all_links.extend(extract_links_from_html(html_content))
            elif msg.get_content_type() == "text/html":
                html_content = decode_content(msg.get_payload(decode=True))
                all_links.extend(extract_links_from_html(html_content))
        
        return all_links
    finally:
        mail.logout()
        logging.info("Logged out from the mail server.")

def save_links(links, file_path="links.txt"):
    """Save links to a text file."""
    with open(file_path, "w") as f:
        f.write("\n".join(links))
    logging.info("Links saved to %s", file_path)

def main():
    """Main function to search emails, extract links, click them, and save results."""
    links = search_for_email()
    click_links(links)
    save_links(links)

# Run the main function
if __name__ == "__main__":
    main()
