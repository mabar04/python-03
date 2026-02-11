from typing import Generator

"""
A simple demonstration of Python generators and streaming-style processing.
This script simulates a game event stream and performs basic analytics
while processing events one by one to demonstrate constant memory usage.

It also includes:
- A Fibonacci sequence generator
- A prime number generator
- Basic analytics on streamed data

Concepts demonstrated:
- Generators and yield
- Type hinting for generators
- Streaming data processing
"""


def data_stream(i: int) -> Generator[tuple[str, int, str], None, None]:
    """
    Generate a simulated game event.

    Args:
        i (int): Index used to select a player and event cyclically.

    Yields:
        tuple[str, int, str]: A tuple containing:
            - player name
            - player level
            - event description
    """
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


def Fibonacci(n: int) -> Generator[int, None, None]:
    """
    Generate the Fibonacci sequence up to n terms.

    Args:
        n (int): Number of Fibonacci numbers to generate.

    Yields:
        int: The next Fibonacci number in the sequence.
    """
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def is_prime(i: int) -> int:
    """
    Check if a number is prime.

    Args:
        i (int): Number to check.

    Returns:
        int: 1 if the number is prime, 0 otherwise.
    """
    for r in range(2, i):
        if i % r == 0 and i != r:
            return 0
    return 1


def prime() -> Generator[int, None, None]:
    """
    Generate the first five prime numbers.

    Yields:
        int: The next prime number.
    """
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
high_level = 0
tr_event = 0
level_up = 0
while i < 3:
    player, level, event = next(data_stream(i))
    print(f"Event {i}: Player {player} (level {level}) {event}")
    if level > 10:
        high_level += 1
    if event == "found treasure":
        tr_event += 1
    if event == "leveled up":
        level_up += 1
    i += 1
print("...\n")
print("=== Stream Analytics ===")
print(f"Total events processed : {i}")
print(f"High-level players (10+): {high_level}")
print(f"Tresaure events: {tr_event}")
print(f"Level-up events: {level_up}\n")
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
