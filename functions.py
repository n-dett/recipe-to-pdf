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