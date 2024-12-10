import requests
import json

# Define the API endpoint and query parameters
url = "https://api.openalex.org/works"
params = {
    "filter": "from_publication_date:2023-01-01,to_publication_date:2023-12-31","per-page":200
}

# Make the GET request
response = requests.get(url, params=params)

# Check the response status code
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    print(f"Number of results: {len(data.get('results', []))}")
    
    # Save data to a file (optional)
    with open("openalex_data2023.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
    # Display some example data
    for work in data.get('results', [])[:5]:  # Display the first 5 works
        print(f"Title: {work.get('title')}")
        print(f"DOI: {work.get('doi')}")
        print(f"Publication Date: {work.get('publication_date')}")
        print("-" * 50)
else:
    print(f"Failed to fetch data: {response.status_code} - {response.text}")
