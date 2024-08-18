import os
import argparse  # Make sure argparse is imported
from app import shodan_checker, scraper

def main():
    parser = argparse.ArgumentParser(description="IoT Device WebView Usage Checker")
    
    # Load Shodan API key from environment variables
    shodan_api_key = os.getenv('SHODAN_API_KEY')
    
    # If the API key is not set, print an error message and exit
    if not shodan_api_key:
        print("Error: Shodan API key not found. Please set the 'SHODAN_API_KEY' environment variable.")
        return

    # Define arguments for IP address analysis and Google Play Store scraping
    parser.add_argument('--ip', type=str, help="IP address to analyze with Shodan.")
    parser.add_argument('--url', type=str, help="Google Play Store URL to scrape for web technology usage.")
    
    args = parser.parse_args()

    # Perform Shodan analysis on the given IP address if provided
    if args.ip:
        print(f"Analyzing IP {args.ip} using Shodan...")
        shodan_checker.analyze_ip(args.ip, shodan_api_key)

    # Perform scraping on the given Google Play Store URL if provided
    if args.url:
        print(f"Scraping Google Play Store URL: {args.url}...")
        scraper.scrape_app(args.url)

if __name__ == "__main__":
    main()
