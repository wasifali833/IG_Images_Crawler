import requests

#REQUEST 1 THAT USES KEYWORD

data = {
    'keyword': 'cat'
}

# URL of the API endpoint
url = 'http://localhost:5000/search' 

# Send a POST request to the API endpoint
response = requests.post(url, json=data)

# Print the response from the API
print(response.json())


#REQUEST 2 TO PASS THE IMAGE FOR THE CLASSIFICATION AND

import requests

# The URL of the API endpoint
url = "http://localhost:5000/upload"

# image path
image_path = "downloaded_image0.jpg"

# Sending the POST request with the file
with open(image_path, 'rb') as file:
    response = requests.post(url, files={'image': (image_path, file)})

# Printing the response
print("Status Code:", response.status_code)
print("Response JSON:", response.text)
