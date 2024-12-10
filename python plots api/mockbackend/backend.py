import requests
import base64
from PIL import Image
import io 
import time
def send_get_request():
    response = requests.get("http://api:5000/")
    print(f"Response from API: {response.text}")

def send_post_request(functionstr, title, endpoint):
    print("POST REQUEST SENT")
    try: 
        response = requests.post(f"http://localhost:5000/{endpoint}", json={"function": functionstr, "title":title})
        print("SUCCESFULLY MADE A CONNECTION TO THE NON CONTAINERIZED APP")
        print("THE STATUS CODE IS", response.status_code)
    except:
        print("WHY IS IT EXCEPTING")
        response = requests.post(f"http://api:5000/{endpoint}", json={"function": functionstr, "title":title})
        

    "IS THIS CODE RAN?"
    if response.status_code == 200:
        print("BETER WERKT DEZE ONZIN ")
        image_data64 = response.json().get('plot')
        image_data = base64.b64decode(image_data64)


        image = Image.open(io.BytesIO(image_data))
        with open("plot.png", "wb") as f:
            f.write(image_data)


print("STARTING MOCK BACKEND")
send_post_request("x^2", "title", "plot")











