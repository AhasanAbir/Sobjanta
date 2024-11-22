# sobjanta_search.py

from sobjanta_api_package import MyAPIClient

# Replace 'ENTER_YOUR_API_KEY' with your actual API key
api_key = '72e8384c-8d8b-46e0-9643-15730998a56c'  # Your actual API key
client = MyAPIClient(api_key)  # The client is now ready for use

# Define the search function to make API requests
def search(query):
    categories = 'general'            # Options: 'general', 'news', 'images', 'videos'
    engines = 'all'                   # Use 'all' to search across all engines
    format = 'json'                   # Response format, 'json' is common
    count = 10                         # Number of results to return
    
    try:
        # Perform the search using the Sobjanta API
        data = client.get_data(query, categories=categories, engines=engines, format=format, count=count)
        
        # Check if 'results' is part of the data and return it, else return empty list
        return data.get('results', [])  
    except Exception as e:
        print("An error occurred:", e)
        return []  # Return empty list in case of error
