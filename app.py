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
    

    if uploaded_file:
        st.write("Image Uploaded. Press Analyze to get results.")

        if st.button("Analyze"):
            analyzer = NewsPaperSentimentAnalyzer(api_key=API_KEY)


            response_data = analyzer.prompt_analysis(PROMPT, uploaded_file)
            
            df = pd.DataFrame(response_data)

            st.subheader("Result")
            st.dataframe(df)

            csv_file = df.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv_file,
                file_name='sentiment_results.csv',
                key='download_button'
)



if __name__ == "__main__":
    main()
