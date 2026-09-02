import streamlit as st
import numpy as np
import pickle
from PIL import Image
# Load model
model = pickle.load(open("mnist_model.pkl", "rb"))

class_names = [
    "0", "1", "2", "3", "4",
    "5", "6", "7", "8", "9"
]

st.title("🔢 MNIST Digit Classification")
st.write("Upload a 28x28 grayscale handwritten digit image")

uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("L")
    image = image.resize((28, 28))
    img_array = np.array(image) / 255.0
    img_array = img_array.reshape(1, 28,28,1)

    st.image(image, caption="Uploaded Image", width=150)

    if st.button("Predict"):
        prob_dist = model.predict(img_array)
        prediction = prob_dist.argmax(axis=1)
        result = class_names[prediction[0]]
        st.success(f"Predicted Digit: **{result}**")
