"""
This program tracks player achievements using sets.
It calculates:
- All unique achievements
- Achievements common to all players
- Rare achievements (owned by only one player)
- Achievements shared between specific players
- Achievements unique to a specific player

Set operations (union, intersection, difference) are used to perform the
analysis.
"""

print("=== Achievement Tracker System ===\n")
Alice: set[str] = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
Bob: set[str] = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
Charlie: set[str] = {'level_10', 'treasure_hunter', 'boss_slayer',
                     'speed_demon', 'perfectionist'}
print(f"Player alice achievements: {Alice}")
print(f"Player bob achievements: {Bob}")
print(f"Player charlie achievements: {Charlie}")
print("\n=== Achievement Analytics ===")
all_ach: set[str] = Alice.union(Bob, Charlie)
print(f"All unique achievements: {all_ach}")
print(f"Total unique achievements: {len(all_ach)}\n")
print(f"Common to all players: {Alice.intersection(Bob, Charlie)}")
Rare2 = (Alice ^ Bob ^ Charlie)
print(f"Rare achievements (1 player): {Rare2}")
print()
print(f"Alice vs Bob common: {Alice.intersection(Bob)}")
print(f"Alcie unique: {Alice.difference(Bob)}")
print(f"Bob unique: {Bob.difference(Alice)}")
