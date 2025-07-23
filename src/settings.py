from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional

class Settings(BaseSettings):
    # Uncomment when you want to use these:
    # openai_api_key: str = Field(default=..., env="OPENAI_API_KEY")
    # openai_api_base: str = Field(default="https://api.openai.com/v1", env="OPENAI_API_BASE")

    # llama_index_api_key: Optional[str] = Field(default=None, env="LLAMA_INDEX_API_KEY")
    # huggingface_api_key: Optional[str] = Field(default=None, env="HUGGINGFACE_API_KEY")

    # jira_server: str = Field(default=..., env="JIRA_SERVER")
    # jira_email: str = Field(default=..., env="JIRA_EMAIL")
    # jira_api_token: str = Field(default=..., env="JIRA_API_TOKEN")

    api_host: str = Field(default="0.0.0.0", env="API_HOST")
    api_port: int = Field(default=8000, env="API_PORT")

    log_level: str = Field(default="INFO", env="LOG_LEVEL")
    env: str = Field(default="development", env="ENV")

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore",
    }

settings = Settings()
