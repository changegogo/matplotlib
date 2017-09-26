# encoding=utf8


import matplotlib.pyplot as plt
from randwalk import random_walk as rw


def walk():
    rwalk = rw.RandomWalk()
    rwalk.fill_walk()
    plt.scatter(rwalk.x_values, rwalk.y_values, s=15, c="black")
    plt.show()


if __name__ == "__main__":
    while True:
        rwalk = rw.RandomWalk()
        rwalk.fill_walk()
        point_numbers = list(range(rwalk.num_points))
        plt.scatter(rwalk.x_values, rwalk.y_values, c=point_numbers, cmap=plt.cm.Blues,
                    s=15, edgecolor="none")
        plt.show()
        keep_running = input("Make another walk?(y/n)")
        if keep_running == "n":
            break
