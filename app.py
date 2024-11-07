import io
from PIL import Image
import numpy as np
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# CORS configuration to allow requests from your Angular frontend (change the URL if needed)
CORS(app, resources={r"/predict": {"origins": "http://localhost:4200"}})

# Load the saved model (only once at the start)
model = load_model('fashion_classifier_model.h5')

# Category labels
categories = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", 
              "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

@app.route('/')
def home():
    return 'Hello, World!'

@app.route("/predict", methods=["POST"])
def predict():
    # Check if file is part of the request
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    
    # Check if the file is valid
    if not file or not file.filename.endswith(('jpg', 'jpeg', 'png', 'jfif')):
       return jsonify({"error": "Invalid file type. Only images are allowed."}), 400

    
    try:
        # Read the image data into memory
        img = Image.open(io.BytesIO(file.read()))  # Convert FileStorage to image
        img = img.convert('L')  # Convert image to grayscale (if needed)
        img = img.resize((28, 28))  # Resize the image to 28x28 pixels
        
        img_array = np.array(img)  # Convert to numpy array
        img_array = img_array.reshape(1, 28, 28, 1)  # Reshape for the model
        img_array = img_array / 255.0  # Normalize the image
        
        # Get prediction
        predictions = model.predict(img_array)
        predicted_class = categories[np.argmax(predictions[0])]
        
        # Return the prediction as JSON
        return jsonify({"prediction": predicted_class})

    except Exception as e:
        return jsonify({"error": f"Error processing the file: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
