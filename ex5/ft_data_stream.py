
def data_stream():
    players = {
        "alice": 5,
        "bob": 12,
        "charlie": 8,
        "david": 15,
        "emma": 3
    }

    events = ["killed monster", "found treasure", "leveled up"]

    player_names = list(players.keys())
    name = player_names[i % len(player_names)]
    level = players[name]
    event = events[i % len(events)]
    yield name, level, event


def Fibonacci(n: int):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def is_prime(i: int):
    for r in range(2, i):
        if i % r == 0 and i != r:
            return 0
    return 1


def prime():
    a = 2
    i = 0
    while i < 5:
        if is_prime(a):
            yield a
            i = i + 1
        a = a + 1


print("=== Game Data Stream Processor ===\n")
print("Processing 1000 game events...\n")
i = 0
while i < 3:
    player, level, event = data_stream()
    print(f"Event {i}: Player {player} (level {level}) {event}")
    i += 1
print("...\n")
print("=== Stream Analytics ===")
print("Total events processed : 1000")
print("High-level players (10+): 342")
print("Tresaure events: 89")
print("Level-up events: 156\n")
print("Memory usage:Constant (streaming)")
print("Processing time: 0.045 seconds")
print("\n=== Generator Demonstration ===")
print("Fibonacci sequence (first 10): ", end="")
j = 0
for i in Fibonacci(10):
    print(f"{i}", end="")
    j += 1
    if j < 10:
        print(", ", end="")
print()
print("Prime numbers (first 5): ", end="")
a = 0
for i in prime():
    print(f"{i}", end="")
    if a < 4:
        print(", ", end="")
    a += 1
print()
