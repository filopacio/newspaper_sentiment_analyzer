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
    api_key = st.text_input("Enter your API Key", type="password")
    
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg"])
    
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Optionally, you can perform additional operations on the image
        # For example, you can use Pillow to process the image
    image = Image.open(uploaded_file)
    st.write("Image Size:", image.size)

    if uploaded_file:
        st.write("Image Uploaded. Press Analyze to get results.")

        if st.button("Analyze"):
            analyzer = NewsPaperSentimentAnalyzer(api_key=api_key)

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
