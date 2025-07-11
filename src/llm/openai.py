import openai
from config import config

class OpenAIClient:
    def __init__(self, api_key=None, model="gpt-4o"):
        self.api_key = api_key or config.openai_api_key
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY must be set")
        openai.api_key = self.api_key
        self.model = model

    def chat(self, messages, temperature=0.7, max_tokens=150):
        """
        Expects `messages` in OpenAI chat format: list of dicts with roles & content
        """
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"OpenAI API error: {e}"
