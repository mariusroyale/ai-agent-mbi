from pydantic import BaseSettings, Field
from typing import Optional

class Config(BaseSettings):
    # ==== OpenAI ====
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    openai_api_base: str = Field("https://api.openai.com/v1", env="OPENAI_API_BASE")

    # ==== LlamaIndex ====
    llama_index_api_key: Optional[str] = Field(default=None, env="LLAMA_INDEX_API_KEY")

    # ==== HuggingFace ====
    huggingface_api_key: Optional[str] = Field(default=None, env="HUGGINGFACE_API_KEY")

    # ==== Jira ====
    jira_server: str = Field(..., env="JIRA_SERVER")
    jira_email: str = Field(..., env="JIRA_EMAIL")
    jira_api_token: str = Field(..., env="JIRA_API_TOKEN")

    # ==== FastAPI ====
    api_host: str = Field("0.0.0.0", env="API_HOST")
    api_port: int = Field(8000, env="API_PORT")

    # ==== Optional ====
    log_level: str = Field("INFO", env="LOG_LEVEL")
    env: str = Field("development", env="ENV")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Instantiate settings once to import anywhere
config = Config()
