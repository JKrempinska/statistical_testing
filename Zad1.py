import numpy as np
from scipy.stats import norm
from urllib.request import urlopen
import matplotlib.pyplot as plt


url = "https://prac.im.pwr.edu.pl/~wyloman/ss_2023_2024/lista8_zad1.txt"
page = urlopen(url)
html_lines = page.readlines()
data = [float(line.decode("utf-8")) for line in html_lines]
np.array(data)

H0 = 1.5
sig = 0.2
n = len(data)
alpha = 0.05

data_mean = np.mean(data)
z = (data_mean - H0) / (sig / np.sqrt(n))
Z_quantile = norm.ppf(1 - (alpha/2))

# p-wartości
p_g = 1 - norm.cdf(z)
p_neq = 2 * (1 - norm.cdf(abs(z)))
p_l = norm.cdf(z)


# mu != 1.5 <- hipoteza alternatywna
if z <= -Z_quantile or z >= Z_quantile:
    print('Hipoteza mu != 1.5 prawdziwa')
else: 
    print('Hipoteza mu != 1.5 fałszywa')

Z_quantile = norm.ppf(1 - alpha)

# mu > 1.5 <- hipoteza alternatywna
if z > Z_quantile:
    print('Hipoteza mu > 1.5 prawdziwa')    
else:
    print('Hipoteza mu > 1.5 fałszywa')

# mu < 1.5 <- hipoteza alternatywna
if z < -Z_quantile:
    print('Hipoteza mu < 1.5 prawdziwa')    
else:
    print('Hipoteza mu < 1.5 fałszywa')


# x = np.linspace(-4, 4, 1000)
# pdf = norm.pdf(x)
# threshold1 = norm.ppf(1 - alpha)
# plt.plot(x, pdf)
# plt.fill_between(x, pdf, where=(x > threshold1), color='skyblue', alpha=0.5)
# plt.axvline(threshold1, color='red', linestyle='--', label=r'Z = '+str(round(threshold1,3)))
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title(r'Obszar krytyczny - $\mu>1.5$')
# plt.legend()
# plt.grid(True)
# plt.show()
