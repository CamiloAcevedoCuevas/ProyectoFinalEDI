from Score import Score

class Scores:
    """Class representing a double circular list of scores."""
    def __init__(self):
        self.head = None

    def add_score(self, score):
        """

        Args:
            score (int): _description_
        """
        new_score = Score(score)
        if self.head is None:
            self.head = new_score
            new_score.next = self.head
            new_score.prev = self.head
        else:
            last = self.head.prev
            new_score.next = self.head
            self.head.prev = new_score
            new_score.prev = last
            last.next = new_score
            self.head = new_score

    def get_scorage(self):
        current = self.head
        scorage = 0
        while current != self.head:
            scorage += current.score
            current = current.next
        return scorage
    