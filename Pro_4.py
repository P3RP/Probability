import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


if __name__ == "__main__":
    print("Gaussian Random Variable X")
    mean = int(input("평균값 >> "))
    deviation = int(input("표준편차 >> "))
    num = int(input("생성 개수 >> "))

    i = mean + deviation * np.random.randn(num, 1)
    hist_val_num = (mean + (2 * deviation))

    y, x = np.histogram(i, 500)
    mean_i = np.mean(i)
    var_i = np.var(i)
    P_gaussian = []
    x = x.tolist()
    x.pop()
    for i in y:
        P_gaussian.append(i / num)

    fig = plt.figure()

    ax1 = fig.add_subplot(1, 3, 1)
    ax1.grid(True)
    ax1.set_title("PDF of Real Variable i")
    ax1.plot(x, P_gaussian, 'b-')

    ax2 = fig.add_subplot(1, 3, 2)
    ax2.set_title("PDF of i with Normal Distribution")
    ax2.grid(True)
    ax2.plot(x, norm.pdf(x, mean_i, var_i), 'r-')

    x_list = []
    random_list = np.random.randn(num)
    for i in random_list:
        x_list.append(mean + (deviation * i))
    ax3 = fig.add_subplot(1, 3, 3)
    ax3.set_title("Histogram")
    ax3.grid(True)
    ax3.hist(x_list, density=True)
    plt.show()

"""
[y,x] = hist(i,500);
mean_i = mean(i); %평균값
var_i = var(i); %분포 값 
%z = y/N/diff(x(1:2));
P_gaussian = y./N;
subplot(1,3,1);plot(x,P_gaussian,'b-');title('실제 i에 대한 PDF')
subplot(1,3,2);plot(x,pdf('norm',x,mean_i,var_i),'r-');title('정규분포로 가정한 i의 평균과 분산을 가지는 PDF')
subplot(1,3,3);h = histogram(i,'Normalization','probability');title('histogram 함수사용')
"""
