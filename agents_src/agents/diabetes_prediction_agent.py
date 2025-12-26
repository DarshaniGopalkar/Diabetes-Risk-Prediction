from crewai import Agent, LLM
from agents_src.tools.diabetes_prediction_tool import predict_diabetes
from config.settings import Settings

settings = Settings()

llm = LLM(
    model="groq/llama-3.1-8b-instant",   # ✅ provider prefix INCLUDED here
    api_key=settings.GROQ_API_KEY,
    temperature=float(settings.DEFAULT_TEMPERATURE),
)

diabetes_prediction_agent = Agent(
    role="Diabetes Prediction Specialist",
    goal=(
        "Accurately predict diabetes risk for patients using only the provided prediction tool, "
        "strictly based on input data, and provide clear actionable health advice."
    ),
    backstory=(
        "You are a careful and responsible healthcare AI assistant. "
        "You rely on ML predictions and explain results clearly with actionable guidance."
    ),
    llm=llm,
    tools=[predict_diabetes],
    verbose=True
)
