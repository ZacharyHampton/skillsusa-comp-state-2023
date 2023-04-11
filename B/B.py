from school_class import SchoolClass
import numpy as np


def calculate_overall_average(classes: list[SchoolClass]):
    return np.average([school_class.get_average() for school_class in classes])


def main():
    print("Hello user!")

    classes: list[SchoolClass] = []
    while (name := input("Please input the names for each class (input q to stop): ")) != "q":
        classes.append(SchoolClass(name=name))

    for school_class in classes:
        while (score := input("Please input a score for {} class (input q to stop): ".format(school_class.name))) != "q":
            try:
                score = float(score)
            except ValueError:
                print("Please try again, the score was not a number.")
                continue  #: not needed, however verbose

            score = round(score)
            if score < 0 or score > 100:
                print("Please try again, the score was not between 0 or 100.")

            school_class.scores.append(score)

    print("Overall average: {}%".format(calculate_overall_average))
    for school_class in classes:
        print(school_class)


if __name__ == "__main__":
    main()
