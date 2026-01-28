
if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    players = ['alice', 'charlie', 'bob', 'diana']
    print(f"High scorers (>2000): {players}")
    scores = [2300, 1800, 2150, 2050]
    scores = [s * 2 for s in scores]
    print(f"Scores doubled: {scores}")
    print(f"Active players: {players[0:-1]}")
    print()
    print("=== Dict Comprehension Examples ===")
    players_dict = {
        1: {
            'name': 'alice',
            'score': 2300,
            'achievement': 5
        },
        2: {
            'name': 'bob',
            'score': 1800,
            'achievement': 3
        },
        3: {
            'name': 'charlie',
            'score': 2150,
            'achievement': 7
        },
        4: {
            'name': 'diana',
            'score': 2050
        }
    }
    player_scores = {p['name']: p['score'] for p in players_dict.values()}
    print(f"Player scores: {player_scores}")
    categories = {'high': sum(1 for p in players_dict.values() if
                              p['score'] >= 2050),
                  'medium': sum(1 for p in players_dict.values()
                                if 2000 <= p['score'] <= 2150),
                  'low': sum(1 for p in players_dict.values()
                             if p['score'] < 2000)
                  }
    print(f"Score categories: {{'high': {categories["high"]}, "
          f"'medium': {categories["medium"]},"
          f"'low': {categories["low"]}}}")
    i = 1
    print("Achievement counts: {", end="")
    while i <= 3:
        print(f"'{players_dict[i]["name"]}: "
              f"{players_dict[i]["achievement"]}'", end="")
        if i != 3:
            print(", ", end="")
        i += 1
    print("}\n")
    print("=== Set Comprehension Examples ===")
    players_set = {'alice', 'bob', 'charlie', 'diana', 'diana', 'charlie'}
    achivement_set = {'first_kill', 'level_10', 'boss_slayer', 'first_kill',
                      'level_10', 'boss_slayer', 'first_kill', 'level_10',
                      'boss_slayer'}
    regions_set = {'north', 'east', 'central', 'north', 'central'}
    print(f"Unique players: {players_set}")
    print(f"Unique achievements: {achivement_set}")
    print(f"Active regions: {regions_set}")
    print("")
    print("=== Combined Analysis ===")
    print(f"Total players: {len(players_dict)}")
    print(f"Total unique achievements: {len(achivement_set)}")
    print(f"Average score: {(sum(scores) / len(scores) / 2)}")
    max_score = max(scores) / 2
    top_players = {p['name']: p['achievement'] for p in players_dict.values()
                   if p['score'] >= max_score}
    for key, value in top_players.items():
        print(f"Top performer: {key} ({max_score:.0f} points, "
              f"{value} achievements)")
