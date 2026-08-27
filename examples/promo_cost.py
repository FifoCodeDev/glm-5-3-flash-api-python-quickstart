"""Estimate GLM-5.3-Flash token cost before and during the promotion."""

import argparse


STANDARD = {
    "input": 0.15,
    "cached_input": 0.03,
    "output": 0.50,
}
PROMO = {key: value / 2 for key, value in STANDARD.items()}


def estimate(tokens: dict[str, int], rates: dict[str, float]) -> float:
    return sum(tokens[key] / 1_000_000 * rates[key] for key in rates)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=int, required=True)
    parser.add_argument("--cached-input", type=int, default=0)
    parser.add_argument("--output", type=int, required=True)
    args = parser.parse_args()

    tokens = {
        "input": args.input,
        "cached_input": args.cached_input,
        "output": args.output,
    }
    print("Standard reference: $" + f"{estimate(tokens, STANDARD):.6f}")
    print("50% promotion:      $" + f"{estimate(tokens, PROMO):.6f}")


if __name__ == "__main__":
    main()
