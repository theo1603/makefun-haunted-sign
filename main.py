"""Write the haunted server room door sign to /output/entry.txt.

Deterministic, stdlib only, no network. The entry is one line: a sign
taped to the door of a haunted server room. The joke is deadpan and
short: the ghost is not an intruder to be removed, it is the senior
staff member in the room — it has root access and it outranks you.
"""

import os

ENTRY = (
    "NOTICE: The ghost in this server room has root access "
    "and seniority over you."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
