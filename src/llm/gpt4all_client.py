from typing import List, Dict
from gpt4all import GPT4All
from base_client import BaseLLMClient

class GPT4AllClient(BaseLLMClient):
    def __init__(self, model_path="ggml-gpt4all-j-v1.3-groovy.bin"):
        self.model = GPT4All(model_path)

    def chat(self, messages: List[Dict], temperature=0.7, max_tokens=150) -> str:
        prompt = self._convert_messages_to_prompt(messages)
        response = self.model.generate(prompt, temp=temperature, max_tokens=max_tokens)
        return response

    def _convert_messages_to_prompt(self, messages: List[Dict]) -> str:
        prompt = ""
        for msg in messages:
            role = msg.get("role", "")
            content = msg.get("content", "")
            prompt += f"{role.capitalize()}: {content}\n"
        prompt += "Assistant: "
        return prompt
