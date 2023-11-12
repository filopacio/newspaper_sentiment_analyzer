import re
import os
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

    def encode_image(self, image_input):
        try:
            if isinstance(image_input, str):  # File path case (not used in the current scenario)
                with open(image_input, "rb") as image_file:
                    image_data = image_file.read()
            elif hasattr(image_input, 'read'):  # File-like object case
                image_data = image_input.read()
            else:
                raise ValueError("Invalid input. Provide a file path or a file-like object.")

            return base64.b64encode(image_data).decode('utf-8')
        except Exception as e:
            print(f"Error encoding image: {e}")
            raise

    def prompt_analysis(self, prompt, image_input):
        """
        Manage request, connection and executes prompt
        """
        base64_image = self.encode_image(image_input)

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
