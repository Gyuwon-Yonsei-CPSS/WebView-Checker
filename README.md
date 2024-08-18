# 🌐 WebView Checker 🕵️‍♂️

**WebView Checker** is a CLI tool that utilizes the Shodan API and Google Play Store scraping to help you determine whether an IoT device's companion app uses **web technologies** (such as WebView, JavaScript, etc.).

![GitHub](https://img.shields.io/github/license/yourusername/webview-checker) ![Python](https://img.shields.io/badge/Python-3.7%2B-blue)

---

## 🎯 Key Features
- Analyze IoT devices' IP addresses and web server information using **Shodan API**.
- Scrape Google Play Store app descriptions to detect **web technology usage** (e.g., WebView, JavaScript, HTML).
- Quickly and easily check if an app might be using WebView with a simple command.

---

## 🚀 Installation & Usage

### 1️⃣ Clone the repository and install the package

```bash
git clone https://github.com/yourusername/webview-checker.git
cd webview-checker
pip install .
2️⃣ Set your Shodan API key
To use the Shodan API, you must first set your API key as an environment variable.

You can obtain a Shodan API key by following the steps below

How to get your Shodan API key
Sign up or log in to Shodan.io.
After logging in, go to your Account page.
Copy your API Key from the dashboard.


Set the API Key as an environment variable

For Windows (PowerShell)
$env:SHODAN_API_KEY="your_shodan_api_key"


For Windows (CMD)
set SHODAN_API_KEY="your_shodan_api_key"


For macOS/Linux (bash)
export SHODAN_API_KEY="your_shodan_api_key"


3️⃣ Run the CLI tool
1. Analyze an IP address (using Shodan API)
webview-checker --ip 1.1.1.1


2. Scrape Google Play Store
webview-checker --url https://play.google.com/store/apps/details?id=com.example.app


3. Analyze both IP and URL simultaneously
webview-checker --ip 1.1.1.1 --url https://play.google.com/store/apps/details?id=com.example.app


🛠️ Components
Shodan API Analysis: The module app/shodan_checker.py interacts with the Shodan API to analyze the provided IP address and gather web server information (e.g., open ports, server types).

Google Play Store Scraping: The module app/scraper.py scrapes the app page and detects whether the app uses web technologies such as WebView, JavaScript, or HTML.

CLI Interface: cli.py allows users to easily access both the Shodan and scraping functionalities through command-line options.

🎉 Why Use WebView Checker?
🌍 Combined Analysis: It merges network-level data (Shodan API) with app metadata (Google Play Store) for a comprehensive analysis.

🔍 Fast and Convenient: With just one command, you can simultaneously analyze IP addresses and app URLs, providing a clear view of possible WebView usage.

🛡️ Useful for Security Experts: This tool can be extremely helpful for security experts analyzing IoT devices or investigating whether companion apps use web technologies, which could present certain vulnerabilities.

🔧 Automated: No need to manually query Shodan or Google Play Store data. This tool automates everything for you.

📝 Contributing
We welcome contributions! Please fork this repository and submit a pull request with your improvements.

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
