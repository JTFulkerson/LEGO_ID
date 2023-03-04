import requests
import json

class BrickognizeAPI:
    def predict_part(image_path):
        """Send an image to the Brickognize API and return the JSON response.

        Args:
            image_path (str): Path to the image file to send to the API.

        Returns:
            Response Object: JSON response from the Brickognize API.
        """
        url = "https://api.brickognize.com/predict/parts/"

        # Send the image file as a multipart-encoded file
        with open(image_path, "rb") as image_file:
            image_data = {"query_image": ("image.jpg", image_file, "image/jpeg")}
            response = requests.post(url, files=image_data)

        return response.json()