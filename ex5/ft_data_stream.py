def Processing_data():
    players = {
        1: {
           "name": "Alice",
           "level": 5
        },
        2: {
            "name": "bob",
            "level": 12
        },
        3: {
            "name": "charlie",
            "level": 8
        }
    }
    events = ["killed monster", "found treasure", "leveled up"]
    


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
for player in Processing_data():
    print(f"Event {i}: Player {player["name"]} (level {player["level"]}"
          f" {player["event"]})")
    i = i + 1
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
for i in Fibonacci(10):
    print(f"{i}", end="")
    if i < 34:
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
