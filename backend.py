from flask import Flask, request, jsonify
from nvidia import JarvisClient, JarvisServerError

# Initialize Flask app
app = Flask(__name__)

# Initialize JarvisClient with API key and endpoint
client = JarvisClient(api_key='our_api_key', endpoint='endpoint url')

# Function to handle natural language processing (NLP)
def process_nlp(text):
    try:
        response = client.nlp(text=text)
        return response
    except JarvisServerError as e:
        print(f'Error processing NLP request: {e}')
        return {'error': 'Error processing NLP request'}

# Function to handle automatic speech recognition (ASR)
def process_asr(audio_data):
    try:
        response = client.asr(audio=audio_data)
        return response
    except JarvisServerError as e:
        print(f'Error processing ASR request: {e}')
        return {'error': 'Error processing ASR request'}

# Function to handle text-to-speech (TTS)
def process_tts(text):
    try:
        response = client.tts(text=text)
        return response
    except JarvisServerError as e:
        print(f'Error processing TTS request: {e}')
        return {'error': 'Error processing TTS request'}

# Route to handle user input processing
@app.route('/process', methods=['POST'])
def process_input():
    data = request.json
    user_input = data.get('userInput')
    action = data.get('action')  # Optional: 'nlp', 'asr', 'tts'

    if action == 'asr':
        
        audio_data = data.get('audioData')
        response = process_asr(audio_data)
    elif action == 'tts':
       
        response = process_tts(user_input)
    else:
        
        response = process_nlp(user_input)

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
