from openai_client import OpenAIClient
from gpt4all_client import GPT4AllClient
from base_client import BaseLLMClient

def get_llm_client(use_local=False, **kwargs) -> BaseLLMClient:
    if use_local:
        model_path = kwargs.get("model_path", "ggml-gpt4all-j-v1.3-groovy.bin")
        return GPT4AllClient(model_path=model_path)
    else:
        api_key = kwargs.get("api_key", None)
        model = kwargs.get("model", "gpt-3.5-turbo")
        return OpenAIClient(api_key=api_key, model=model)
