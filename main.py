import os
import argparse
import prompts
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.call_function import available_functions, call_function


def main():
    load_dotenv()
    api_key = getEnv("GEMINI_API_KEY")

    prompt = getUserPrompt()
    messages = [types.Content(role="user", parts=[types.Part(text=prompt.user_prompt)])]

    for _ in range(20):
        response = generateContentFromGenAI(api_key=api_key, messages=messages)
        if response.candidates:  # list of model's response from the last prompt
            for candidate in response.candidates:
                messages.append(candidate.content)

        function_responses = callFunctionFromGeneratedResponse(
            prompt=prompt, response=response
        )

        if not function_responses:  # no more function calls. Done
            print(response.text)
            exit(0)

        messages.append(types.Content(role="user", parts=function_responses))

    print("Maximum calls reached")
    exit(1)


def getEnv(key):
    val = os.environ.get(key)

    if not val:
        raise RuntimeError(f"{key} required")

    return val


def generateContentFromGenAI(api_key, messages):
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


def callFunctionFromGeneratedResponse(prompt, response):
    if prompt.verbose:
        print(f"User prompt: {prompt.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens:{response.usage_metadata.candidates_token_count}")

    responses = []

    # Not guarantee to be a list
    if response.function_calls is not None:
        for function_call in response.function_calls:
            result = call_function(function_call=function_call, verbose=prompt.verbose)
            if not result.parts:
                raise RuntimeError("No parts in the function call result")
            if result.parts[0].function_response is None:
                raise RuntimeError("No function response in parts")
            if result.parts[0].function_response.response is None:
                raise RuntimeError("No response in function response")

            responses.append(result.parts[0])

            if prompt.verbose:
                print(f"-> {responses.function_response.response}")

    return responses


if __name__ == "__main__":
    main()
