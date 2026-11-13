import os
from parser import parse_args
from dotenv import load_dotenv
from openai import OpenAI
from output import display_output, display_verbose_output

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

    messages = [
        {
            "role": "user",
            "content": args.user_prompt
        },
    ]

    response = client.chat.completions.create(
        model = "openrouter/free",
        messages = messages
    )
    if response.usage == None:
        raise RuntimeError("Failed API request")

    if args.verbose:
        display_verbose_output(args.user_prompt, response)

    display_output(response)

if __name__ == "__main__":
    main()
