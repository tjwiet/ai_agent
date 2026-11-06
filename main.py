import os
from parser import parse_args
from dotenv import load_dotenv
from openai import OpenAI

# Load and read the .env file
load_dotenv()

# Get api key from .env
api_key = os.environ.get("OPENROUTER_API_KEY")

# Create AI client
client = OpenAI(
    base_url = "https://openrouter.ai/api/v1",
    api_key = api_key
)


def main():
    if api_key == None:
        raise RuntimeError("Could not find api key")


    args = parse_args()
    response = client.chat.completions.create(
        model = "openrouter/free",
        messages = [
            {
                "role": "user",
                "content": args.user_prompt
            }
        ]
    )
    if response.usage == None:
        raise RuntimeError("Failed API request")
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")
    print(f"Response:\n {response.choices[0].message.content}")

if __name__ == "__main__":
    main()
