import numpy as np

if __name__ == "__main__":
    min_val = 2
    max_val = 8
    mean = 5
    deviation = 3
    num = 10000
    i = np.array(mean + deviation * np.random.randn(num))
    y, x = np.histogram(i, 500)
    P_gaussian = y / num

    xa = np.where((x > min_val) & (x < max_val))
    Pa = np.sum(P_gaussian[xa])*100
    print(Pa)
