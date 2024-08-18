import requests
from bs4 import BeautifulSoup

def scrape_app(app_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    response = requests.get(app_url, headers=headers)

    if response.status_code != 200:
        print(f"Error: Unable to fetch the page. Status code {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Checking for the presence of common web technologies like WebView, JavaScript, HTML, etc.
    description = soup.find('meta', {'name': 'description'})
    if description and ("WebView" in description['content'] or "JavaScript" in description['content'] or "HTML" in description['content']):
        print("This app likely uses web technologies (WebView, JavaScript, HTML).")
    else:
        print("This app does not appear to use significant web technologies.")
