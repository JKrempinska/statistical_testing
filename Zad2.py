import numpy as np
from scipy.stats import chi2
from urllib.request import urlopen
import matplotlib.pyplot as plt


url = "https://prac.im.pwr.edu.pl/~wyloman/ss_2023_2024/lista8_zad2.txt"
page = urlopen(url)
html_lines = page.readlines()
data = [float(line.decode("utf-8")) for line in html_lines]
np.array(data)

H0 = 1.5
mu = 0.2
n = len(data)
alpha = 0.05

data_std = np.std(data)
x = ((n-1) * (data_std) ** 2) / H0 

X_quantile_low = chi2.ppf(alpha/2, n-1)
X_quantile_high = chi2.ppf(1 - (alpha/2), n-1)

# p-wartości
p_neq = 2 * min(1 - chi2.cdf(x, n-1), chi2.cdf(x, n-1))
p_g = 1 - chi2.cdf(x, n-1)
p_l = chi2.cdf(x, n-1)

# sig2 != 1.5 <- hipoteza alternatywna
if x <= X_quantile_low or x >= X_quantile_high:
    print('Hipoteza sig != 1.5 prawdziwa')
else: 
    print('Hipoteza sig != 1.5 fałszywa')

X_quantile = chi2.ppf(1 - alpha, n-1)

# sig > 1.5 <- hipoteza alternatywna
if x > X_quantile:
    print('Hipoteza sig > 1.5 prawdziwa')    
else:
    print('Hipoteza sig > 1.5 fałszywa')

X_quantile = chi2.ppf(alpha, n-1)

# sig < 1.5 <- hipoteza alternatywna
if x < X_quantile:
    print('Hipoteza sig < 1.5 prawdziwa')    
else:
    print('Hipoteza sig < 1.5 fałszywa')

# # v = np.linspace(700, 1500, 1000)
# # pdf = chi2.pdf(v, n-1)
# # threshold1 = X_quantile_low
# # threshold2 = X_quantile_high
# # plt.plot(v, pdf)
# # plt.fill_between(v, pdf, where=(v < threshold1), color='skyblue', alpha=0.5)
# # plt.axvline(threshold1, color='red', linestyle='--', label=r'$X_{1}$ = '+str(round(threshold1,3)))
# # plt.fill_between(v, pdf, where=(v > threshold2), color='skyblue', alpha=0.5)
# # plt.axvline(threshold2, color='red', linestyle='--', label=r'$X_{2}$ = '+str(round(threshold2,3)))
# # plt.xlabel('x')
# # plt.ylabel('f(x)')
# # plt.title(r'Obszar krytyczny - $\sigma^{2}\neq$ 1.5')
# # plt.legend()
# # plt.grid(True)
# # plt.show()