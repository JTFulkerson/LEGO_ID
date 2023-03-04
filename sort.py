import brickognize_api
import json


# Send the image to the brickognize API class and return the JSON response
response = brickognize_api.predict_part("image.jpg")

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
