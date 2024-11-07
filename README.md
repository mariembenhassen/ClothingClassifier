# ClothingClassifier
FashionClassifier is an AI-powered web application built using Flask and TensorFlow to classify fashion items based on uploaded images. The application utilizes a pre-trained deep learning model to predict the category of clothing items such as T-shirts, dresses, shoes, and more from user-uploaded images. The model processes images in grayscale, resizes them, and normalizes them before making predictions.

Key Features:
Image Classification: Classifies various types of clothing into predefined categories like T-shirt, dress, sandal, sneaker, etc.
Web Interface: Users can upload images directly through a simple web interface for easy interaction.
CORS Support: Ensures that the application can be accessed from external sources (like Angular front-end) through Cross-Origin Resource Sharing (CORS).
Real-Time Predictions: Fast image processing and classification in real-time.
Error Handling: Detailed error messages for invalid files or processing issues.
Technologies Used:
Flask: For creating a RESTful API that handles image uploads and predictions.
TensorFlow/Keras: For building and using a deep learning model to classify images.
Pillow: For handling image processing tasks like resizing and conversion to grayscale.
NumPy: For numerical operations and image array manipulation.
CORS: For allowing cross-origin requests, enabling interaction with front-end applications.
