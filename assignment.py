import json
import requests

def fetch_data(api_url):
    """Fetch data from an API."""
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def process_data(data):
    """Process and analyze the data."""
    if not data:
        return "No data to process."
    
    processed_result = {}  # Example data transformation
    for item in data:
        key = item.get("category", "Unknown")
        processed_result[key] = processed_result.get(key, 0) + 1
    
    return processed_result

def save_to_file(data, filename="output.json"):
    """Save processed data to a JSON file."""
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully saved to {filename}")
    except IOError as e:
        print(f"Error saving data: {e}")

# Example usage
API_URL = "https://jsonplaceholder.typicode.com/posts"  # Sample API
data = fetch_data(API_URL)
result = process_data(data)
save_to_file(result)