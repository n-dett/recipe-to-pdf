import os
from dotenv import load_dotenv
from openai import OpenAI
import pymupdf
import sample_data as sd
from functions import process_response, get_ai_response


def main():
    # # Load API key
    # load_dotenv()
    # api_key= os.environ.get("OPENAI_API_KEY")
    #
    # # New OpenAI instance
    # client = OpenAI(api_key=api_key)

    # Recipes folder
    dir_path = "/Users/nataliedettmer/Library/Mobile Documents/com~apple~CloudDocs/Recipes"

    # Loop through all files in directory
    for entry in os.scandir(dir_path):
        if entry.is_file():
            file_path = entry.path
            print(file_path)

            # Read text from PDF
            webpage_pdf = pymupdf.open(file_path)
            webpage_text = ""
            for page in webpage_pdf:  # iterate the document pages
                text = page.get_text()  # get plain text (is in UTF-8)
                webpage_text += text

            print (webpage_text, "\n\n\n\n\n")




            # # Send pdf text to GPT; receive extracted recipe text
            # response_text = get_ai_response(client, input_pdf_text)
            #
            # # Clean up GPT response
            # recipe_text = process_response(response_text)


if __name__ == "__main__":
    main()