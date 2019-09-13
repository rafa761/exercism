class HighScores(object):
    def __init__(self, scores):
        self.scores = scores
        self.high = self.personal_top()[0]

    def personal_top(self):
        result_high = []
        high_score = list(self.scores).copy()
        high_score.sort(reverse=True)
        for index, value in enumerate(high_score):
            if index == 3:
                break
            else:
                result_high.append(value)
        return result_high

    def report(self):
        last = self.scores[-1]
        if self.high - last == 0:
            return f"Your latest score was {last}. That's your personal best!"
        else:
            return f"Your latest score was {last}. That's {self.high - last} short of your personal best!"

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)
