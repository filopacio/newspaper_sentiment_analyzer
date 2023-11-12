from config.config import SRC_DIR, parameters, api_key
from src.newspaper_analyzer import NewsPaperSentimentAnalyzer


TEMPERATURE = parameters['temperature']
MAX_TOKENS = parameters['max_tokens']
MODEL = parameters['model']
SENTIMENT_CATEGORIES = parameters['sentiment_categories']
PROMPT = parameters['prompt'].format(len(SENTIMENT_CATEGORIES), SENTIMENT_CATEGORIES)
API_KEY = api_key

image_path = SRC_DIR / "data/article.jpeg"
if __name__ == "__main__":
    analyzer = NewsPaperSentimentAnalyzer(api_key=API_KEY,
                                          temperature=TEMPERATURE,
                                          max_tokens=MAX_TOKENS,
                                          model=MODEL)
    response_data = analyzer.prompt_analysis(PROMPT, image_path)
    result_df = analyzer.transform_to_dataframe(response_data)
    print(result_df)



