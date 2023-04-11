import numpy as np
from dataclasses import dataclass
from rich.pretty import Pretty


@dataclass
class SchoolData:
    name: str
    scores: Pretty
    current_avg: str
    highest_score: str
    lowest_score: str


class SchoolClass:
    """Holds information relating to a specific class."""
    def __init__(self, name: str):
        self.name: str = name
        self.scores: list[float] = []

    def get_statistics(self):
        return SchoolData(
            name=self.name,
            scores=Pretty([str(score) + "%" for score in self.scores]),
            current_avg=str(int(self.get_average())) + "%",
            highest_score=str(np.max(self.scores)) + "%",
            lowest_score=str(np.min(self.scores)) + "%",
        )

    def get_average(self) -> float:
        return round(np.average(self.scores))
