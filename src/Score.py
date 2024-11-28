class Score:
    """Class thay represents a score.

    Args:
        score(int): Score in the game
    """
    def __init__(self, score):
        self.score = score
        self.next = None
        self.prev = None
