import requests
import json

# Define the URL for the API endpoint
url = "https://api.brickognize.com/predict/parts/"

# Define the image file to be analyzed
image_path = "./image.jpg"

# Send the image file as a multipart-encoded file
with open(image_path, "rb") as image_file:
    image_data = {"query_image": ("image.jpg", image_file, "image/jpeg")}
    response = requests.post(url, files=image_data)

# Save the JSON response to a file
with open("response.json", "w") as json_file:
    json.dump(response.json(), json_file)

# Parse the JSON response
response_json = json.loads(response.text)

# Extract the name and listing_id of the first part in the list
if response_json['items']:
    name = response_json['items'][0]['name']
    listing_id = response_json['listing_id']
    print(f"Name: {name}, Listing ID: {listing_id}")
else:
    print("No parts found in response.")
