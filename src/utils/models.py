import dspy
from dotenv import load_dotenv
from utils import settings

load_dotenv()

llm = dspy.Cohere(model=settings.COHERE_LLM_MODEL)
