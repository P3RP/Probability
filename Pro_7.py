import numpy as np
import scipy.special

if __name__ == "__main__":
    max_val = -4.2
    mean = 5
    deviation = 3
    num = 10000
    i = np.array(mean + deviation * np.random.randn(num))
    y, x = np.histogram(i, 500)
    P_gaussian = y / num

    xa = np.where(x <= max_val)
    Pa = np.sum(P_gaussian[xa])*100
    print(Pa)

    qfunc = lambda x: 0.5 - 0.5 * scipy.special.erf(x / np.sqrt(2))
    print(qfunc(4.2))
