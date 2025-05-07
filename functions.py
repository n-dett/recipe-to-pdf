import pymupdf
import os
from pathlib import Path

def get_ai_response(client, input_string:str)->str:
    """Sends pdf text to GPT; receives extracted recipe text"""
    response = client.responses.create(
        model="gpt-4.1-mini",
        input="From this text, extract only the recipe title, instructions, and ingredients with amounts."
              f"Text: {input_string}"
    )

    print(response.output_text)
    return print(response.output_text)


def process_response(ai_response:str)->str:
    """Cleans up the AI response text"""
    # Break output into paragraphs
    title, ingredients, instructions = ai_response.split("\n\n")

    # Remove **Recipe Title** text
    title = title.replace("**Recipe Title:**  \n", "")
    print(title)


def create_recipe_book():
    """ Creates recipe book PDF if it doesn't exist"""
    recipe_book_path = Path("/Users/nataliedettmer/Library/Mobile Documents/com~apple~CloudDocs/recipe-book.pdf")

    if not recipe_book_path.is_file():
        # Create new file
        recipe_book = pymupdf.open()

        # Create title page
        n = recipe_book.insert_page(-1,  # default insertion point
                            text="My Recipe Book",
                            fontsize=11,
                            width=595,
                            height=842,
                            fontname="Helvetica",  # default font
                            fontfile=None,  # any font file name
                            color=(0, 0, 0))  # text color (RGB)
        recipe_book.save(recipe_book_path)

    else:
        recipe_book = pymupdf.open("/Users/nataliedettmer/Library/Mobile Documents/com~apple~CloudDocs/recipe-book.pdf")

    return recipe_book

def new_recipe_book_page(recipe_book_path:str):
    pass
