from typing import List, Dict
from gpt4all import GPT4All
from llm.base_client import BaseLLMClient
from pathlib import Path

class GPT4AllClient(BaseLLMClient):
    def __init__(self, model_name="ggml-gpt4all-j-v1.3-groovy.bin", model_dir="bin"):
        model_path = Path(model_dir)

        if not model_path.exists():
            raise FileNotFoundError(f"Model not found at path: {model_path}")

        # self.llm = GPT4All(model_name=model_name, model_path=str(model_path), allow_download=False)

    def query_prompt(self, messages: List[Dict], temperature=0.7, max_tokens=150) -> str:
        prompt = self._convert_messages_to_prompt(messages)
        response = self.llm.generate(prompt, temp=temperature, max_tokens=max_tokens)
        return response

    def _convert_messages_to_prompt(self, messages: List[Dict]) -> str:
        prompt = ""
        for msg in messages:
            role = msg.get("role", "")
            content = msg.get("content", "")
            prompt += f"{role.capitalize()}: {content}\n"
        prompt += "Assistant: "
        return prompt
