
# Original output
def display_output(response: object):
    print(f"Response:\n {response.choices[0].message.content}")

def display_verbose_output(prompt, response: object):
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")
