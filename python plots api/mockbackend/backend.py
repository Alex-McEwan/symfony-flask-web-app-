import requests
import base64
from PIL import Image
import io 
import time
def send_get_request():
    response = requests.get("http://api:5000/")
    print(f"Response from API: {response.text}")

def send_post_request(functionstr, title):
    response = requests.post("http://localhost:5000/plot", json={"function": functionstr, "title":title})
    if response.status_code != 200: 
        response = requests.post("http://api:5000/plot", json={"function": functionstr, "title":title})

    if response.status_code == 200:
        print("BETER WERKT DEZE ONZIN ")
        image_data64 = response.json().get('plot')
        image_data = base64.b64decode(image_data64)


        image = Image.open(io.BytesIO(image_data))
        with open("plot.png", "wb") as f:
            f.write(image_data)


send_post_request("sin(x) + x", "alt")











