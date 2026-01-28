import sys

print("=== Player Score Analytics ===")
if len(sys.argv) < 2:
    print(f"No scores provided. Usage: python3 {sys.argv[0]}"
          f"<score1> <score2> ...")
else:
    list = []
    i = 1
    while i < len(sys.argv):
        try:
            list += [int(sys.argv[i])]
        except ValueError:
            print(f"oops, I typed ’{sys.argv[i]}’ instead of ’1000’")
        i = i + 1

    print(f"Scores processed: {list} ")
    print(f"Total players: {len(list)}")
    print(f"Total score: {sum(list)}")
    print(f"Average score: {sum(list) / len(list)}")
    print(f"High score: {max(list)}")
    print(f"Low score: {min(list)}")
    print(f"Score range: {max(list) - min(list)}")
    print("\n")
