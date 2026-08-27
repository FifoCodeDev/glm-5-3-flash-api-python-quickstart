"""Send text plus an image URL to GLM-5.3-Flash through CometAPI."""

import os

from openai import OpenAI


def main() -> None:
    image_url = os.environ["IMAGE_URL"]
    client = OpenAI(
        api_key=os.environ["COMETAPI_API_KEY"],
        base_url="https://api.cometapi.com/v1",
    )

    response = client.chat.completions.create(
        model=os.getenv("GLM_MODEL", "glm-5.3-flash"),
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Describe the key UI elements in this image.",
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": image_url},
                    },
                ],
            }
        ],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
