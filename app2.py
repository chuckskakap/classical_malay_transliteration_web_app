import streamlit as st
import malaya

# Load the transliteration model
# model = malaya.jawi_rumi.transformer(model="small", quantized=True)
model = malaya.jawi_rumi.transformer(model="small", quantized=True)


def transliterate(input_text):
    result = model.greedy_decoder([input_text])
    return result[0]


# Add your logo
logo_url = "https://static.wixstatic.com/media/a82f81_ee5d3c423b80433eaac59bb71b2bba16~mv2.png"  # Replace with the URL of your logo
st.image(logo_url, width=100)  # Adjust width as needed
# Streamlit app
st.title("Deep Learning for Classical Malay Text Transliteration")


# Input text box
input_text = st.text_input("Enter Jawi Text:")

# Transliteration button
if st.button("Transliterate"):
    output_text = transliterate(input_text)
    st.success(f"Transliterated Text: {output_text}")
