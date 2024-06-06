import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px 
from PIL import Image 

def run(): 
    #membuat judul
    st.title('Rice Classification')

    #tambah gambar
    image = Image.open('rice.jpg')
    st.image(image, caption = 'Beras menjadi salah satu makanan pokok terfavorit di seluruh negara.')

    #font size
    st.write('##### Tinjau jenis beras yang akan Anda beli')

    #membuat batas dengan garis lurus
    st.markdown('---')

    #load gambar beras
    image = Image.open('arborio.jpg')
    st.image(image, caption = 'Beras Arborio')

    image = Image.open('Basmati.jpg')
    st.image(image, caption = 'Beras Basmati')
    
    image = Image.open('Ipsala.jpg')
    st.image(image, caption = 'Beras Ipsala')
    
    image = Image.open('jasmine.jpg')
    st.image(image, caption = 'Beras Jasmine')
    
    image = Image.open('Karacadag.jpg')
    st.image(image, caption = 'Beras Karacadag')

    st.markdown('---')
    st.write('**Page dibuat oleh Amelia P.S. untuk graded assignment 7 Hacktiv8 FTDS batch RMT-30**')

if __name__=='__main__':
    run()