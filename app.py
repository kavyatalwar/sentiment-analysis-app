import streamlit as st
from transformers import pipeline

# 1. Page Config & Title
st.set_page_config(page_title="Sentiment Analyzer", page_icon="🔮")
st.title("🔮 Sentiment Analysis App") 
st.write("Enter text below to analyze whether the emotion is Positive, Negative, or Neutral.")

# 2. Load the model (Cached so it's fast)
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")

analyzer = load_model()

# 3. Input Box & Button
user_input = st.text_area("Enter your sentence or paragraph here:", height=150)
if st.button("Analyze Sentiment"):
    if user_input.strip():
        with st.spinner("Analyzing..."):
            # Get prediction
            prediction = analyzer(user_input)[0]['label'].lower()
            
            # 4. Display clean, simple result
            st.subheader("Result:")
            if prediction == "positive":
                st.success("😊 Positive")
            elif prediction == "negative":
                st.error("😡 Negative")
            else:
                st.info("😐 Neutral")
    else:
        st.warning("Please enter some text first!")