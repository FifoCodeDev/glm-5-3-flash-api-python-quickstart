"""Use explicit thinking controls for a repeatable GLM-5.3-Flash call."""

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
                "content": "Find two edge cases for a JSON API validator.",
            }
        ],
        extra_body={
            "thinking": {"type": "enabled"},
            "reasoning_effort": "max",
        },
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
