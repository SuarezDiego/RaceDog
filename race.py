from random import randint
from result import Result

class Race:
    """
    Attributes:
        date: date
            The date and time of the race
        competitors: List<Dog>
            The list of dogs that compete in the race
        results: List<Result>
            The list of positions the dogs finished
    """
    def __init__(self, date, competitors):
        self.date = date
        self.competitors = competitors
        self.results = list()

    def run_race(self):
        cant_competitors = len(self.competitors)
        aux_positions = list(range(1, cant_competitors + 1 ))
        for competitor in self.competitors:
            position = aux_positions.pop(randint(0, cant_competitors - 1))
            cant_competitors -= 1
            result = Result(competitor,position)
            self.results.append(result)
        return self.results

    def make_positions_table(self):
        positions_table = "Positions table:\n"
        self.results.sort(key=lambda result: result.position, reverse=False)
        for result in self.results:
            positions_table += str(result.position) + "\t" + str(result.dog.name) + "\n"
        return positions_table
