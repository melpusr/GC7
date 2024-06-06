import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image


def run():
    # Load the best model
    best_model_path = '/content/drive/MyDrive/best_rice_classification_model.h5'
    model = load_model(best_model_path)

    # Define image dimensions
    img_height, img_width = 150, 150

    # Class labels
    class_labels = ['Arborio', 'Basmati', 'Ipsala', 'Jasmine', 'Karacadag']

    # Preprocess the image
    def preprocess_image(img):
        img = img.resize((img_height, img_width))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        img_array /= 255.0  # Normalize the image to [0, 1] range
        return img_array

    # Streamlit app
    st.title("Rice Type Classification")
    st.write("Upload an image of rice grain to classify its type.")

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Classifying...")

        processed_image = preprocess_image(img)
        predictions = model.predict(processed_image)
        predicted_class = np.argmax(predictions, axis=1)
        predicted_label = class_labels[predicted_class[0]]

        st.write(f'The predicted class is: {predicted_label}')


if __name__ == '__main__':
   run()
