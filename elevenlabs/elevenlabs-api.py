import requests

# Define your API key and voice ID
API_KEY = "your_api_key_here"
VOICE_ID = "your_voice_id_here"  # Replace with a valid voice ID

# Define the API endpoint and headers
url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
headers = {
    "Content-Type": "application/json",
    "xi-api-key": API_KEY
}

# Define the request payload with all voice settings
payload = {
    "text": "Hello, this is a test of ElevenLabs TTS with all voice settings!",
    "voice_settings": {
        "stability": 0.7,             # Controls consistency of the generated speech
        "similarity_boost": 0.85,      # Adjusts how much the output resembles the original voice
        "style_exaggeration": 1.0,     # Enhances expressive elements
        "use_speaker_boost": True      # Enables speaker boost for additional clarity
    }
}

# Send the request
response = requests.post(url, json=payload, headers=headers)

# Save the audio file if the request was successful
if response.status_code == 200:
    with open("output.mp3", "wb") as f:
        f.write(response.content)
    print("Audio file saved as output.mp3")
else:
    print("Error:", response.json())