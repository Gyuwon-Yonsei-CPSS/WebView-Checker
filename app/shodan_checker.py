import shodan

def analyze_ip(ip_address, api_key):
    # Initialize Shodan API instance with the provided API key
    api = shodan.Shodan(api_key)

    try:
        # Query Shodan for information on the provided IP address
        result = api.host(ip_address)
        web_servers = []

        # Loop through all data associated with the IP address
        for item in result['data']:
            # Check if HTTP or HTTPS ports are open
            if item['port'] == 80 or item['port'] == 443:
                server_info = item.get('http', {}).get('server', 'Unknown Server')
                web_servers.append(f"Port: {item['port']}, Server: {server_info}")
        
        # If web servers are found, print their information
        if web_servers:
            print(f"IP: {ip_address} has the following web servers:")
            for server in web_servers:
                print(f"  - {server}")
        else:
            print(f"IP: {ip_address} does not seem to host any web servers.")
    
    except shodan.APIError as e:
        # Handle Shodan API errors
        print(f"Shodan API Error: {e}")