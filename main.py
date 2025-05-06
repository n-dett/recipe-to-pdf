import os
from dotenv import load_dotenv
from openai import OpenAI


# Load API key
load_dotenv()
API_KEY = os.environ.get("OPENAI_API_KEY")

# New OpenAI instance
client = OpenAI(api_key=API_KEY)


# Get response from GPT
response = client.responses.create(
    model="gpt-4.1-mini",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)