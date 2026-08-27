"""Minimal GLM-5.3-Flash request through CometAPI."""

import os

from openai import OpenAI


def main() -> None:
    client = OpenAI(
        api_key=os.environ["COMETAPI_API_KEY"],
        base_url="https://api.cometapi.com/v1",
    )

    response = client.chat.completions.create(
        model=os.getenv("GLM_MODEL", "glm-5.3-flash"),
        messages=[
            {
                "role": "user",
                "content": "Give me one practical Python testing tip.",
            }
        ],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
