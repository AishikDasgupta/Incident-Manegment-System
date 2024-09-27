import requests

def chatbot_response(message):
    responses = {
        'hi': 'Hello! How can I assist you?',
        'status': 'All systems are operational.',
        'error': 'Please describe the error in detail.'
    }
    return responses.get(message.lower(), "I didn't understand that.")
