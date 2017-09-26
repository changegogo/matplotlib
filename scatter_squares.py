# encoding=utf8
import numpy as np
import matplotlib.pyplot as plt


def main():
    x_values = np.arange(-100, 101, 5)
    y_values = x_values**3

    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolors='none', s=10)
    # 设置每个坐标轴的取值范围
    # plt.axis([0, 500, 0, 250000])
    plt.savefig('./data/sscatter.png', bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()
