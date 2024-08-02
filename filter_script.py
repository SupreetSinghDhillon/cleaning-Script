import json

# Load the JSON data from file
def load_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Save the modified data to a new JSON file
def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Filter the data
def filter_data(data):
    new_data = []
    for entry in data['data']:
        url = entry['data']['siteInfo']['url']
        # Check if 'search' is in the URL but not 'youtube'
        if 'search' in url and 'youtube' not in url:
            continue  # Skip adding this entry
        new_data.append(entry)
    return {'data': new_data}

# Example usage
data_filename = 'data.json'
filtered_filename = 'filtered_data.json'

# Load, filter, and save the data
data = load_data(data_filename)
filtered_data = filter_data(data)
save_data(filtered_data, filtered_filename)

print(f"Filtered data has been saved to {filtered_filename}")
