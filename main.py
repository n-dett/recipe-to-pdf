import os
from dotenv import load_dotenv
from openai import OpenAI
import sample_data as sd
from functions import process_response, get_ai_response


def main():

    # Load API key
    load_dotenv()
    api_key= os.environ.get("OPENAI_API_KEY")

    # New OpenAI instance
    client = OpenAI(api_key=api_key)


    pdf_text = ""

    # Sends pdf text to GPT; receives extracted recipe text
    response_text = get_ai_response(client, pdf_text)

    # Clean up GPT response
    recipe_text = process_response(response_text)


if __name__ == "__main__":
    main()