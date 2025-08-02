import base64
import numpy as np
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
from io import BytesIO

def process_image(image_data):
    """
    Process the uploaded image using Gemini API and extract blood test features.
    
    Args:
        image_data: Base64 encoded image data
        
    Returns:
        dict: Dictionary containing extracted features
    """
    try:
        # Load environment variables
        load_dotenv()
        api_key = os.getenv("GOOGLE_GEMINI_API_KEY")
        if not api_key:
            raise ValueError("API key not found in .env file")

        # Configure Gemini
        genai.configure(api_key=api_key)

        # Prepare the image for Gemini
        # Directly handle raw image bytes
        image_bytes = image_data

        # Encode for API request
        encoded_image = base64.b64encode(image_bytes).decode('utf-8')
        
        # Create image payload
        image_payload = {
            'mime_type': 'image/jpeg',
            'data': encoded_image
        }

        # Define the prompt for feature extraction
        prompt = """
        Extract the following features from this blood report image and return the result in JSON format:

        - Gender (Male or Female)
        - Hemoglobin (numeric value in g/dl)
        - MCH (Mean Corpuscular Hemoglobin, numeric value in pg)
        - MCHC (Mean Corpuscular Hemoglobin Concentration, numeric value in gm/dl)
        - MCV (Mean Corpuscular Volume, numeric value in fl)

        Return only the JSON object without any additional text or explanation:
        {
          "gender": "Male",
          "hemoglobin": 14.4,
          "mch": 31.3,
          "mchc": 34.0,
          "mcv": 92.2
        }
        """

        # Get response from Gemini
        model = genai.GenerativeModel("gemini-2.0-flash-exp")
        response = model.generate_content([image_payload, prompt])
        
        # Parse the response
        response_text = response.text.strip()
        
        # Convert string response to dictionary
        import json
        try:
            features = json.loads(response_text)
        except json.JSONDecodeError:
            # If direct JSON parsing fails, try to extract JSON from text
            start_idx = response_text.find('{')
            end_idx = response_text.rfind('}') + 1
            if start_idx != -1 and end_idx != 0:
                json_str = response_text[start_idx:end_idx]
                features = json.loads(json_str)
            else:
                raise ValueError("Could not parse JSON from response")

        # Convert features to the required format
        gender_value = 1 if features['gender'].lower() == 'male' else 0
        
        formatted_features = {
            'gender': gender_value,
            'hemoglobin': float(features['hemoglobin']),
            'mch': float(features['mch']),
            'mchc': float(features['mchc']),
            'mcv': float(features['mcv'])
        }

        return formatted_features

    except Exception as e:
        raise Exception(f"Error processing image: {str(e)}")