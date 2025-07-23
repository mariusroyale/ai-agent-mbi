from llm.gpt4all_client import GPT4AllClient

class Agent007:
    def __init__(self):
        self.llm_client = GPT4AllClient()
        self.messages = []

    def reset(self):
        self.messages = []

    def add_message(self, role: str, content: str):
        message = {"role": role, "content": content}
        self.messages.append(message)
        return message

    def get_messages(self):
        return self.messages

    def query_prompt(self) -> str:
        return "This was supposed to be a response to your prompt."
        # return self.llm_client.query_prompt(self.messages)
