import openai
import urllib.request
from PIL import Image
import cv2
import streamlit as st

openai.api_key='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'

def generate_image(image_description):
    response = openai.images.generate(
        model="dall-e-3",
        prompt=image_description,
        size="1024x1024",
        quality="standard",
        n=1)
    image_url = response.data[0].url
    urllib.request.urlretrieve(image_url, 'img.png')
    img=Image.open("img.png")
    return img


st.title("DALL-E - Image Generation -OpenAI")
image_description=st.text_input("Image_Description")

if st.button("Generate Image"):
    generated_image=generate_image(image_description)
    st.image(generated_image)

