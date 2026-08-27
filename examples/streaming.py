"""Stream GLM-5.3-Flash text deltas through CometAPI."""

import os

from openai import OpenAI


def main() -> None:
    client = OpenAI(
        api_key=os.environ["COMETAPI_API_KEY"],
        base_url="https://api.cometapi.com/v1",
    )

    stream = client.chat.completions.create(
        model=os.getenv("GLM_MODEL", "glm-5.3-flash"),
        messages=[
            {
                "role": "user",
                "content": "Explain why streaming is useful in an agent UI.",
            }
        ],
        stream=True,
    )

    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            print(delta, end="", flush=True)
    print()


if __name__ == "__main__":
    main()
