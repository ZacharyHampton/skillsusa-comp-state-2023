from classes.school_class import SchoolClass
import numpy as np
import sys


def calculate_overall_average(classes: list[SchoolClass]) -> float:
    #: Get the average for each class, then average those averages
    return np.average([school_class.get_average() for school_class in classes if school_class.scores])


def main():
    print("Hello user!")

    classes: list[SchoolClass] = []

    #: Get class names
    while (name := input("Please input the names for each class (input q to stop): ")) != "q":
        classes.append(SchoolClass(name=name))

    if classes is None:
        print("No classes were inputted, closing program.")
        sys.exit(0)

    for school_class in classes:
        #: Get scores for class
        while (score := input("Please input a score for {} class (input q to stop): ".format(school_class.name))) != "q":
            #: Validate if score is a number
            try:
                score = float(score)
            except ValueError:
                print("Please try again, the score was not a number.")
                continue  #: not needed, however verbose

            #: Round score
            score = round(score)

            #: if score is between or equal to 0 and 100
            if not 0 <= score <= 100:
                print("Please try again, the score was not between 0 or 100.")

            school_class.scores.append(score)

    #: Print overall class average.
    print("Overall average: {}%".format(calculate_overall_average(classes)))

    #: Print data for each class
    for school_class in classes:
        #: If a class does not have scores, it can be disregarded as junk.
        if school_class.scores:
            print(school_class)


if __name__ == "__main__":
    main()
