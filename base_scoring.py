import pandas as pd

def rank_players(players):
    df = pd.DataFrame(players)

    rank_df = df.set_index('name').rank(ascending=False, method='min')

    rank_df['Train Average Rank'] = rank_df[['param1', 'param4', 'param7']].mean(axis=1)
    rank_df['Predict Average Rank'] = rank_df[['param2', 'param5', 'param8']].mean(axis=1)
    rank_df['Accuracy Average Rank'] = rank_df[['param3', 'param6', 'param9']].mean(axis=1)

    rank_df['overall_avg'] = rank_df[['Train Average Rank', 'Predict Average Rank', 'Accuracy Average Rank']].mean(axis=1)

    rank_df.reset_index(inplace=True)

    ranked_sorted = rank_df.sort_values(by='overall_avg')

    return ranked_sorted[['name', 'Train Average Rank', 'Predict Average Rank', 'Accuracy Average Rank', 'overall_avg']]

players = [
    {"name": "Alice", "param1": 50, "param2": 70, "param3": 30, "param4": 90, "param5": 60, "param6": 85, "param7": 40, "param8": 75, "param9": 95},
    {"name": "Bob", "param1": 80, "param2": 60, "param3": 55, "param4": 70, "param5": 85, "param6": 75, "param7": 65, "param8": 80, "param9": 90},
    {"name": "Charlie", "param1": 65, "param2": 85, "param3": 45, "param4": 95, "param5": 75, "param6": 65, "param7": 60, "param8": 85, "param9": 70},
]

ranked_players = rank_players(players)
print(ranked_players)

