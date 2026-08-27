# GLM-5.3-Flash API Python Quickstart with CometAPI

Runnable Python examples for calling **GLM-5.3-Flash** through CometAPI's OpenAI-compatible API: chat completions, streaming, multimodal input, reasoning controls, and temporary launch pricing.

> **Quick answer:** use the model ID `glm-5.3-flash`, the CometAPI base URL `https://api.cometapi.com/v1`, and the Chat Completions endpoint `POST /chat/completions`. Check the live CometAPI model details before shipping because model availability, fields, and promotional pricing can change.

## GLM-5.3-Flash at a glance

GLM-5.3-Flash is the first natively multimodal model in the GLM-5 series, according to Z.ai's launch announcement. It is positioned for coding agents, long-context work, and visual feedback loops while keeping inference costs low.

| Setting | Value |
| --- | --- |
| API model ID | `glm-5.3-flash` |
| Provider | Z.ai |
| API style | OpenAI-compatible Chat Completions |
| CometAPI base URL | `https://api.cometapi.com/v1` |
| Endpoint | `POST /chat/completions` |
| Modalities described by the provider | Text, image, and video input |
| Context window | Up to 1M tokens, according to the launch materials |
| Reasoning | Thinking is enabled; use the live route's supported effort values |

The model is different from the text-focused `glm-5.3`. Do not silently substitute one model ID for the other in production configuration.

## Promotional pricing snapshot

The CometAPI update shown on **August 27, 2026** describes a limited-time 50% discount for `glm-5.3-flash`. Treat the discount as a dated launch promotion rather than a permanent budget assumption.

| Price per 1M tokens | Standard reference | 50% promotion |
| --- | ---: | ---: |
| New input | $0.15 | $0.075 |
| Cached input | $0.03 | $0.015 |
| Output | $0.50 | $0.25 |

The promotion is shown as ending at **24:00 on September 9, 2026 (UTC+8, Singapore Time)**, equivalent to **16:00 UTC on September 9, 2026**. Re-check the live CometAPI model details and billing page before using these numbers in a quote or cost model.

## What is in this repository?

- `examples/quickstart.py` — the smallest working text request
- `examples/streaming.py` — prints text deltas as they arrive
- `examples/multimodal.py` — sends text plus an image URL
- `examples/reasoning_controls.py` — shows explicit thinking settings
- `examples/promo_cost.py` — estimates token cost at standard and promotional rates
- `.env.example` — environment-variable template with no real credentials

## Quickstart

### 1. Install the dependency

```bash
python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

### 2. Set your API key

Copy `.env.example` to your local environment and export the variables. The examples read environment variables directly so a secret is never committed to Git.

```bash
# macOS / Linux
export COMETAPI_API_KEY="YOUR_COMETAPI_KEY"
export DEEPSEEK_MODEL="glm-5.3-flash"

# Windows PowerShell
$env:COMETAPI_API_KEY = "YOUR_COMETAPI_KEY"
$env:GLM_MODEL = "glm-5.3-flash"
```

The `DEEPSEEK_MODEL` line is optional and is retained only for compatibility with the earlier quickstart pattern. The GLM examples use `GLM_MODEL`.

### 3. Run the first request

```bash
python examples/quickstart.py
```

The core call is:

```python
import os

from openai import OpenAI

client = OpenAI(
    api_key=os.environ["COMETAPI_API_KEY"],
    base_url="https://api.cometapi.com/v1",
)

response = client.chat.completions.create(
    model="glm-5.3-flash",
    messages=[
        {"role": "user", "content": "Give me one practical Python testing tip."}
    ],
)

print(response.choices[0].message.content)
```

## Streaming responses

Streaming is useful for agent interfaces and long answers because the UI can render text before the full response is complete:

```bash
python examples/streaming.py
```

The example uses the standard OpenAI Python SDK shape with `stream=True`. Add timeouts, retry policy, request IDs, and structured logging before using it in a production worker.

## Multimodal input

The GLM-5.3-Flash launch materials describe native image and video input. The example sends an image URL using the OpenAI-compatible content-block format:

```bash
python examples/multimodal.py
```

Set `IMAGE_URL` to a test image you are allowed to access. A specific CometAPI route may expose a subset of the provider's modalities, so verify the live model details and error behavior before depending on image or video input.

## Thinking and reasoning controls

For repeatable evaluations, set the reasoning fields explicitly when the live CometAPI route supports them:

```bash
python examples/reasoning_controls.py
```

The example sends:

```python
extra_body={
    "thinking": {"type": "enabled"},
    "reasoning_effort": "max",
}
```

Z.ai's launch materials describe enabled thinking for GLM-5.3-Flash. If the route rejects a provider-specific field, remove that field and follow the current CometAPI API reference rather than guessing at a fallback.

## Cost estimation

Use the included helper to compare the temporary promotion with the standard reference price:

```bash
python examples/promo_cost.py --input 1000000 --cached-input 200000 --output 300000
```

The helper is an estimate only. Actual billing depends on the live CometAPI rate card, tokenization, caching rules, and the date of the request. Budget against the standard rate after the promotion ends.

## Production checklist

1. Keep `COMETAPI_API_KEY` in a secret manager or environment variable.
2. Pin `glm-5.3-flash` in configuration and validate allowed model IDs.
3. Set network timeouts and bounded retries for `POST /chat/completions`.
4. Log latency, input/output tokens, retry count, and provider request IDs without logging secrets.
5. Test text-only and multimodal prompts separately; do not assume every route supports every input type.
6. Compare the standard rate with the temporary promotion before approving a budget.
7. Re-check the live CometAPI model details after September 9, 2026.

## FAQ

### What is the GLM-5.3-Flash API model ID?

The model ID used by this repository is `glm-5.3-flash`. It is not the same as `glm-5.3`.

### How do I call GLM-5.3-Flash with CometAPI?

Install the OpenAI Python package, set `COMETAPI_API_KEY`, use `https://api.cometapi.com/v1` as `base_url`, and call `client.chat.completions.create(model="glm-5.3-flash", ...)`.

### Is GLM-5.3-Flash multimodal?

Z.ai describes it as natively multimodal with text, image, and video input. The exact modalities exposed by a hosted API route should be verified in the current CometAPI model details.

### How long does the 50% promotion last?

The update snapshot says the promotion ends at 24:00 UTC+8 on September 9, 2026, which is 16:00 UTC. Treat this as temporary and verify the live rate card.

### Does this repository include model weights?

No. It contains small API client examples only. For local deployment information, read the official Z.ai announcement and model repository linked below.

## Source and verification links

- [CometAPI model catalog](https://www.cometapi.com/models/?utm_source=github&utm_medium=organic&utm_campaign=glm_5_3_flash_launch&utm_content=readme)
- [CometAPI API quickstart](https://www.cometapi.com/quickstart/?utm_source=github&utm_medium=organic&utm_campaign=glm_5_3_flash_launch&utm_content=readme)
- [CometAPI API documentation](https://apidoc.cometapi.com/?utm_source=github&utm_medium=organic&utm_campaign=glm_5_3_flash_launch&utm_content=readme)
- [Z.ai: GLM-5.3-Flash announcement](https://z.ai/blog/glm-5.3-flash)
- [Z.ai GLM-5.3-Flash model repository](https://huggingface.co/zai-org/GLM-5.3-Flash)

This is an original, code-focused developer adaptation of the linked documentation. Provider model IDs, capabilities, availability, and pricing can change; verify the live sources before shipping.
