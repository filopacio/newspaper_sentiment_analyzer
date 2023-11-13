import re
import json
import pandas as pd
from PIL import Image
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
            
            pattern = r'```(.*?)```'
            matches = re.findall(pattern, response_data, re.DOTALL)
            extracted_text = matches[0].strip().replace('json', '')
            data_dict = json.loads(extracted_text)
            
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)

            keys = list(data_dict.keys())
            values = list(data_dict.values())
            
            # Create DataFrame with two columns
            df = pd.DataFrame({'Infos': keys, 'Values': values})
            
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
