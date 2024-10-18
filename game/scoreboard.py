class Scoreboard:
    def __init__(self):
        self.scores = {'Player': 0, 'Computer': 0}

    def update_score(self, winner):
        if winner in self.scores:
            self.scores[winner] += 1

    def display_scores(self):
        print("Текущие результаты:")
        for player, score in self.scores.items():
            print(f"{player}: {score}")

    def reset_scores(self):
        self.scores = {player: 0 for player in self.scores}
