import numpy as np


class SchoolClass:
    """Holds information relating to a specific class."""
    def __init__(self, name: str):
        self.name: str = name
        self.scores: list[float] = []

    def __str__(self):
        return """Class Name: {}
All Scores Entered: {}
Current Average: {}%
Highest Score: {}%
Lowest Score: {}%""".format(
            self.name,
            '\n'.join([str(score) + "%" for score in self.scores]),
            int(self.get_average()),
            np.max(self.scores),
            np.min(self.scores)
        )

    def get_average(self) -> float:
        return np.average(self.scores)
