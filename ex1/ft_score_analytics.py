import sys

"""
This program reads player scores from the command line,
stores them in a list, and calculates statistics such as
total, average, highest, lowest, and score range.
Invalid inputs are handled gracefully.
"""
print("=== Player Score Analytics ===")
if len(sys.argv) < 2:
    print(f"No scores provided. Usage: python3 {sys.argv[0]} "
          f"<score1> <score2> ...")
else:
    scores = []
    i = 1
    while i < len(sys.argv):
        try:
            scores += [int(sys.argv[i])]
        except ValueError:
            print(f"oops, I typed ’{sys.argv[i]}’ instead of ’1000’")
        i = i + 1

    print(f"Scores processed: {scores} ")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")
    print("\n")
