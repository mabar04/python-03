"""
Game Analytics Dashboard

This script demonstrates Python comprehensions (list, dict, and set)
through a simple game analytics example. It covers:

- List comprehensions: doubling scores, slicing player lists.
- Dict comprehensions: mapping player scores and counting achievements.
- Set comprehensions: identifying unique players, achievements, and regions.
- Combined analysis: total players, unique achievements, average score, and
top performers.
"""
if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    players = ['alice', 'bob', 'charlie', 'diana']
    players_high = [p for p in players if p != "bob"]
    print(f"High scorers (>2000): {players_high}")
    scores = [2300, 1800, 2150, 2050]
    scores_d = [s * 2 for s in scores]
    print(f"Scores doubled: {scores_d}")
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
        }
    }
    player_scores = {p['name']: p['score'] for p in players_dict.values()}
    print(f"Player scores: {player_scores}")
    categories = {'high': sum(1 for p in players_dict.values() if
                              p['score'] >= 1800),
                  'medium': sum(1 for p in players_dict.values()
                                if 1800 <= p['score'] <= 2150),
                  'low': sum(1 for p in players_dict.values()
                             if p['score'] < 2000)
                  }
    print(f"Score categories: {{'high': {categories['high']}, "
          f"'medium': {categories["medium"]},"
          f"'low': {categories["low"]}}}")
    achievement_counts = {p['name']: p.get('achievement', 0)
                          for p in players_dict.values()}
    print(f"Achievement counts: {achievement_counts}")
    print()
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
    print(f"Total players: {len(players_set)}")
    achivement_set1 = {'first_kill', 'level_10', 'boss_slayer', 'leveled_up',
                       'level_20', 'level_50', 'monster_hunter', 'level_30',
                       'kill_arcane', 'Week_player', 'Katana', 'ONEman'}
    print(f"Total unique achievements: {len(achivement_set1)}")
    print(f"Average score: {(sum(scores) / len(scores))}")
    max_score = max(scores)
    top_players = {p['name']: p['achievement'] for p in players_dict.values()
                   if p['score'] >= max_score}
    for key, value in top_players.items():
        print(f"Top performer: {key} ({max_score:.0f} points, "
              f"{value} achievements)")
