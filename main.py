import os
import argparse
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY required")

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=getUserPrompt()
    )

    if not response.usage_metadata:
        raise RuntimeError("Gemini API response malformed")

    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens:{response.usage_metadata.candidates_token_count}")
    print(f"Response: {response.text}")


def getUserPrompt():
    parser = argparse.ArgumentParser(description="LLM Shell")
    parser.add_argument("user_prompt", type=str, help="User Prompt")

    return parser.parse_args().user_prompt


if __name__ == "__main__":
    main()
