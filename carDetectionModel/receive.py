from path import filepath
import requests

def receive_image(url):
    try:    
        # Download the image content
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes

        filename = filepath("recieved.jpeg")
            
        with open(filename, 'wb') as f:
            f.write(response.content)
            
        print(f"💾 Saved received image to {filename}")

    except Exception as e:
        print(f"❌ An error occurred: {e}")