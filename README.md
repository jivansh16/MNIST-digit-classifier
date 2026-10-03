# MNIST Digit Classifier

This is a Streamlit web application that classifies handwritten digits (0-9) using a trained deep learning Convolutional Neural Network (CNN) built with TensorFlow and Keras.

## Features

- **Upload Images**: Users can upload images (PNG, JPG, JPEG) of handwritten digits.
- **Image Preprocessing**: The app automatically converts the image to grayscale and resizes it to 28x28 pixels to match the model's expected input.
- **Real-time Prediction**: Click a button to instantly see the model's prediction.
- **Interactive UI**: Built with Streamlit for a clean and simple user experience.

## Model Architecture

The application uses a custom Convolutional Neural Network (CNN) trained on the MNIST dataset. The architecture consists of:
- **3 Convolutional Layers (Conv2D)** with ReLU activation for feature extraction.
- **2 Max Pooling Layers (MaxPooling2D)** for spatial downsampling.
- **2 Dense Layers** including a hidden layer with 64 units and a 10-unit output layer (one for each digit).

The model was compiled with the Adam optimizer and Sparse Categorical Crossentropy loss, and trained for 5 epochs.

## Project Structure

- `app.py`: The main Streamlit application script.
- `MNIST_model_training.ipynb`: Jupyter notebook containing the code used to train the classification model.
- `mnist_model.pkl`: The saved pre-trained model used for predictions.
- `requirements.txt`: List of Python dependencies required to run the project.

## Installation and Setup

1. **Navigate to the project directory**:
   ```bash
   cd "MNIST digit classifier"
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

To start the Streamlit application, run the following command in your terminal:

```bash
streamlit run app.py
```

The app will open automatically in your default web browser (usually at `http://localhost:8501`).

## How to Use

1. Run the app using the command above.
2. Click on "Browse files" to upload an image of a handwritten digit. 
3. The uploaded image will be displayed on the screen.
4. Click the **Predict** button to see the model's prediction for the digit.
