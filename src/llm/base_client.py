from typing import List, Dict

class BaseLLMClient:
    def chat(self, messages: List[Dict], temperature=0.7, max_tokens=150) -> str:
        raise NotImplementedError
