import matplotlib.pyplot as plt
import numpy as np


def main():
    values = np.arange(1, 11)
    squares = values ** 2
    plt.plot(values, squares, linewidth=1, color="red", linestyle="--")

    # 设置图表标题，并给坐标轴加上标签
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    # 设置刻度标记的大小
    plt.tick_params(axis="both", labelsize=14)

    plt.show()


if __name__ == "__main__":
    main()
