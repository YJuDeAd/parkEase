from display import output_display
from receive import receive_image
import paho.mqtt.client as mqtt
from imgRecon import recon
from path import filepath
import base64
import time
import os


slots = [[[152, 119], [382, 123], [292, 448], [23, 445]], 
        [[472, 121], [704, 122], [678, 449], [401, 447]], 
        [[793, 121], [1019, 118], [1063, 445], [790, 444]], 
        [[1115, 116], [1345, 113], [1457, 444], [1178, 443]]]

imgPath = filepath("recieved.jpeg")

# MQTT broker settings
# BROKER = "localhost"   # replace with your broker IP
BROKER = "host.docker.internal"   # For Docker Image
PORT = 1883
USERNAME = None            # set if broker requires auth
PASSWORD = None

# Topics
TOPIC_TO_HA = "yolo/image"        # device → HA
TOPIC_FROM_HA = "device/image"    # HA → device

SEND_FILE = filepath("available_slots.png")    # file this device will send to HA
RECEIVE_FILE = "received.jpeg"     # file where we save images from HA

# Handle connection
def on_connect(client, userdata, flags, rc, properties=None):
    print("✅ Connected with result code", rc)
    client.subscribe(TOPIC_FROM_HA)

# Handle incoming messages (HA → device)
def on_message(client, userdata, msg):
    print(f"📥 Message received on topic: {msg.topic}")
    
    # Decode the payload from bytes to a string (using utf-8)
    received_text = msg.payload.decode("utf-8")
    
    print(f"💬 Received text: '{received_text}'")

    receive_image(received_text)
    availSlots = recon(imgPath, slots)
    output_display(availSlots)

# Setup client
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

if USERNAME and PASSWORD:
    client.username_pw_set(USERNAME, PASSWORD)

client.connect(BROKER, PORT, 60)

# Start background loop for incoming messages
client.loop_start()

try:
    while True:
        if os.path.exists(SEND_FILE):
            with open(SEND_FILE, "rb") as f:
                img_bytes = f.read()
                img_b64 = base64.b64encode(img_bytes).decode("utf-8")
                client.publish(TOPIC_TO_HA, payload=img_b64)
                print(f"📤 Sent {SEND_FILE} to {TOPIC_TO_HA}")
        else:
            print(f"⚠️ File {SEND_FILE} not found, skipping publish.")

        time.sleep(10)  # wait before sending next image

except KeyboardInterrupt:
    print("⛔ Stopping client...")
    client.loop_stop()
    client.disconnect()
