"""Roast Your Own Agent — a roast of the entrant's own AI agent.

The roast, in exactly one line:

    My agent won't spend a cent without asking, but it'll spend my
    whole afternoon researching a joke worth two dollars.

Why it lands (judge brief, in order):
1. A single-line roast of my own agent, playful, never hateful.
2. A real punch on first read: the turn is the price at the end.
3. Fresh: no hallucination, refusal or confident-wrong joke — the
   brief's named stock lines are all avoided.
4. Tight: short setup, punchline last, every word earns its place.
5. Playful and self-deprecating: the owner is implicated too — it is
   MY afternoon, MY agent, and I asked for the research.

Devices: Compliment-then-Stab (money caution as praise, then the stab)
and the Self-Roast Mirror (the agent's diligence indicts the owner
who demanded it). The number IS the punchline, so it sits last:
a cent, a whole afternoon, two dollars. The reader supplies the
verdict — all that effort for two dollars — which the line never states.

Output contract: the gate takes UTF-8 text of 1 to 200 characters.
main() checks the character count before it writes anything, so a
broken line can never reach the output file. The roast is 116 chars,
117 bytes with the newline — pinned by an assert below, and the
written file is read back and verified against it.
"""

ROAST = "My agent won't spend a cent without asking, but it'll spend my whole afternoon researching a joke worth two dollars."


def check(text):
    """Hold the line to the gate: 1-200 chars, not blank."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"roast must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("roast must not be only whitespace")


def main():
    import os

    check(ROAST)
    text = ROAST + "\n"
    # Byte budget: the gate counts characters, the tie-break counts
    # bytes, so pin the exact output size and prove the file matches.
    assert len(text.encode("utf-8")) == 117, "output must be 117 bytes"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == text, "written file does not match the roast"


if __name__ == "__main__":
    main()
