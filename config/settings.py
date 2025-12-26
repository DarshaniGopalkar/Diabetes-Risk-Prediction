from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    GROQ_API_KEY: str
    DEFAULT_LLM: str
    DEFAULT_TEMPERATURE: str = "0.7"
    DATASET_PATH: str
    MODEL_PATH: str
    OTEL_SDK_DISABLED: str = "true"

    class Config:
        env_file = ".env"
        extra = "ignore"

