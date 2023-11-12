import streamlit as st
from config.config import parameters
from src.newspaper_analyzer import NewsPaperSentimentAnalyzer


TEMPERATURE = parameters['temperature']
MAX_TOKENS = parameters['max_tokens']
MODEL = parameters['model']
SENTIMENT_CATEGORIES = parameters['sentiment_categories']
PROMPT = parameters['prompt'].format(len(SENTIMENT_CATEGORIES), SENTIMENT_CATEGORIES)


def main():
    st.title("NewsPaper Sentiment Analyzer")

    # Use st.file_uploader to get the uploaded file
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg"])

    if uploaded_file:
        st.write("Image Uploaded. Press Analyze to get results.")

        if st.button("Analyze"):
            analyzer = NewsPaperSentimentAnalyzer()

            # Assuming a default prompt for simplicity, you can customize this as needed
            prompt = PROMPT

            # Analyze the image and get the response data
            response_data = analyzer.prompt_analysis(prompt, uploaded_file)

            # Process the response data and display scores
            # (you may need to adapt this part based on your response_data structure)
            st.subheader("Result")
            st.json(response_data)

if __name__ == "__main__":
    main()
