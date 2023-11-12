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

    API_KEY = st.text_input("Enter your API Key", type="password")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg"])

    if API_KEY and uploaded_file:
        st.write("API Key and Image Uploaded. Press Analyze to get results.")

        if st.button("Analyze"):
            analyzer = NewsPaperSentimentAnalyzer(API_KEY)

            response_data = analyzer.prompt_analysis(PROMPT, uploaded_file)
            categories_scores = analyzer.transform_to_dataframe(response_data)

            st.subheader("Categories Scores")
            st.table(categories_scores)


if __name__ == "__main__":
    main()
