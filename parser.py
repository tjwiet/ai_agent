import argparse

def parse_args():
    # init parser
    parser = argparse.ArgumentParser(description = "Chatbot")
    # allow for user input argument
    parser.add_argument("user_prompt", type = str, help = "User prompt")
    # allow for optional verbose argument
    parser.add_argument("--verbose", action = "store_true", help = "Enable verbose output")
    # Parse the arguments
    args = parser.parse_args()
    return args
