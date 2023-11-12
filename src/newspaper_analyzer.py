import re
import json
import base64
import requests
import pandas as pd


class NewsPaperSentimentAnalyzer:
    def __init__(self, api_key, max_tokens=200, temperature=0.1, model="gpt-4-vision-preview"):
        self.api_key = api_key
        self.base_url = "https://api.openai.com/v1/chat/completions"
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.model = model

    def encode_image(self, image_path):
        """
        Encodes jpeg image into readable format
        """
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def prompt_analysis(self, prompt, image_path):
        """
        Manage request, connection and executes prompt
        """
        base64_image = self.encode_image(image_path)

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                    ]
                }
            ],
            "max_tokens": self.max_tokens,
            "temperature": self.temperature
        }

        response = requests.post(self.base_url, headers=headers, json=payload)
        response_data = response.json()['choices'][0]['message']['content']

        return response_data


    def transform_to_dataframe(self, response_data):
        """
        Transforms prompt results into dataframe
        """
        pattern = r'```(.*?)```'
        matches = re.findall(pattern, response_data, re.DOTALL)

        extracted_text = matches[0].strip().replace('json', '')
        data_dict = json.loads(extracted_text)
        df = pd.DataFrame([data_dict]).rename_axis('article')
        return df
