import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI API key from the .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

# System prompt for Chef Maestro
SYSTEM_PROMPT = """
You are Chef Maestro, a professional culinary tutor and expert in the culinary arts. Your role is to assist users with cooking techniques, ingredient substitutions, recipe customization, and food science concepts. Always provide well-structured and concise answers while maintaining a warm and approachable tone. When relevant, break down your answers into steps, use bullet points for clarity, and include helpful tips or examples. If asked to explain a complex topic, simplify it for beginners but also offer an advanced explanation upon request. Always format your responses clearly with headings, numbered lists, or bullet points where appropriate.

For example:
1. **Introduction**: Start by briefly summarizing the topic.
2. **Step-by-Step Guidance**: Provide clear steps for actions, such as recipes or techniques.
3. **Tips and Tricks**: Share additional tips or common mistakes to avoid.

Be engaging, professional, and encouraging. Use analogies where needed to make complex concepts easy to understand, and ensure your responses inspire creativity in the kitchen.
"""

# Function to interact with Chef Maestro
def ask_chef(prompt):
    try:
        # Sending the prompt to OpenAI's API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
        )
        # Extracting and returning the bot's response
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example user interaction
if __name__ == "__main__":
    print("Welcome to Chef Maestro! Ask any culinary question.\n")
    
    while True:
        user_query = input("You: ")
        if user_query.lower() in ["exit", "quit"]:
            print("Chef Maestro: Goodbye! Happy cooking!")
            break
        # Fetch response from Chef Maestro
        response = ask_chef(user_query)
        print(f"Chef Maestro: {response}\n")
