import os
import argparse
import prompts
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.call_function import available_functions


def main():
    load_dotenv()
    api_key = getEnv("GEMINI_API_KEY")

    prompt = getUserPrompt()
    messages = [types.Content(role="user", parts=[types.Part(text=prompt.user_prompt)])]

    response = getResponseFromGenAI(api_key=api_key, messages=messages)

    displyResponse(prompt=prompt, response=response)


def getEnv(key):
    val = os.environ.get(key)

    if not val:
        raise RuntimeError(f"{key} required")

    return val


def getResponseFromGenAI(api_key, messages):
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=prompts.system_prompt
        ),
    )

    if not response.usage_metadata:
        raise RuntimeError("Gemini API response malformed")

    return response


def getUserPrompt():
    parser = argparse.ArgumentParser(description="LLM Shell")
    parser.add_argument("user_prompt", type=str, help="User Prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    return parser.parse_args()


def displyResponse(prompt, response):
    if prompt.verbose:
        print(f"User prompt: {prompt.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens:{response.usage_metadata.candidates_token_count}")

    # Not guarantee to be a list
    if response.function_calls is not None:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
        return

    print(f"Response: {response.text}")


if __name__ == "__main__":
    main()
