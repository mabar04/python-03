
print("=== Achievement Tracker System ===\n")
Alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
Bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
Charlie = {'level_10', 'treasure_hunter', 'boss_slayer',
           'speed_demon', 'perfectionist'}
print(f"Player alice achievements: {Alice}")
print(f"Player bob achievements: {Bob}")
print(f"Player charlie achievements: {Charlie}")
print("\n=== Achievement Analytics ===")
all = Alice.union(Bob, Charlie)
print(f"All unique achievements: {all}")
print(f"Total unique achievements: {len(all)}\n")
print(f"Common to all players: {Alice.intersection(Bob, Charlie)}")
Rare = Alice.difference(Bob, Charlie) | Bob.difference(Alice, Charlie)
Rare2 = Rare | Charlie.difference(Alice, Bob)
print(f"Rare achievements (1 player): {Rare2}")
print("\n")
print(f"Alice vs Bob common: {Alice.intersection(Bob)}")
print(f"Alcie unique: {Alice.difference(Bob)}")
print(f"Bob unique: {Bob.difference(Alice)}")
