from google import genai
from tools import explain_topic, find_resource, plan_today
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def run_agent(user_message: str):
    print(f"\nYOU: {user_message}")
    print("-"* 50)
    system_prompt = """
    You are a Data Engineering learning assistant.
    
    You help someone who is:
    - Transitioning from analytics to Data Engineering
    - Following a 6-7 month learning roadmap
    - Working 9-5 and studying 2-3 hours daily
    - Has Java and Spring Boot background
    - Moderate in Python
    
    Always:
    - Keep explanations practical with real examples
    - Be encouraging but honest
    - Suggest next steps after every answer
    - Relate concepts to Java when helpful
    """
    full_prompt = f"{system_prompt}\n\nUser question: {user_message}"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt
    )
    print(f"\nAGENT:{response.text}")
    return response.text
