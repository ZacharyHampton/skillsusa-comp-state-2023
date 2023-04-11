from classes.school_class import SchoolClass
import numpy as np
import sys
from rich.console import Console
from rich.table import Table
from rich.align import Align
from rich.live import Live
from rich.prompt import Prompt
from rich import box
import dataclasses
from contextlib import contextmanager
import time


def calculate_overall_average(classes: list[SchoolClass]) -> float:
    #: Get the average for each class, then average those averages
    return round(np.average([school_class.get_average() for school_class in classes if school_class.scores]))


#: Iterative sleep for rich ui library
@contextmanager
def beat(length: int = 1) -> None:
    yield
    time.sleep(length * 0.04)


def main():
    console = Console()
    console.print("Hello user! On any input, please input 'q' if you would like to exit the question.")
    console.print('Please input a class you would like to add.')

    classes: list[SchoolClass] = []

    #: Get class names
    while (name := Prompt.ask("Class name")) != "q":
        classes.append(SchoolClass(name=name))
        console.clear()

    if classes is None:
        console.print("No classes were inputted, closing program.")
        sys.exit(0)

    for school_class in classes:
        console.print("Please input a score (0-100) for {} class: ".format(school_class.name))

        #: Get scores for class
        while (score := Prompt.ask("Score")) != "q":
            #: Validate if score is a number
            try:
                score = float(score)
            except ValueError:
                console.print("Please try again, the score was not a number.")
                continue  #: not needed, however verbose

            #: Round score
            score = round(score)

            #: if score is between or equal to 0 and 100
            if not 0 <= score <= 100:
                console.print("Please try again, the score was not between 0 or 100.")
                continue

            school_class.scores.append(score)
            console.clear()

    #: Create table base
    table = Table(show_header=True, header_style="bold magenta", show_footer=True, box=box.ROUNDED)
    table.add_column("Name")
    table.add_column("Scores", no_wrap=False)
    table.add_column("Current Average")
    table.add_column("Highest Score")
    table.add_column("Lowest Score")
    table.add_column("Overall Average", footer="{}%".format(calculate_overall_average(classes)))
    table_centered = Align.center(table)

    table_data = []

    #: Print data for each class
    for school_class in classes:
        #: If a class does not have scores, it can be disregarded as junk.
        if school_class.scores:
            stats = school_class.get_statistics()

            #: Add report card data to list
            table_data.append([getattr(stats, field.name) for field in dataclasses.fields(stats)])

    #: Format report card & generate report card
    with Live(table_centered, console=console, screen=False, refresh_per_second=20):
        with beat(10):
            table.title = "Report Card"

        for row in table_data:
            with beat(10):
                table.add_row(*row)


if __name__ == "__main__":
    main()
