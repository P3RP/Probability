import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    print("Gaussian Random Variable X")
    mean = int(input("평균값 >> "))
    deviation = int(input("표준편차 >> "))
    num = int(input("생성 개수 >> "))
    x_list = []
    random_list = np.random.randn(num)
    for i in random_list:
        x_list.append(mean + (deviation * i))
    plt.scatter(np.linspace(0, 9999, 10000), x_list, s=5)
    plt.xlabel("N")
    plt.ylabel("X")
    plt.show()
