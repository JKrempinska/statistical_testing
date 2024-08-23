import numpy as np
import scipy.stats as stats
from urllib.request import urlopen
import matplotlib.pyplot as plt


url = "https://prac.im.pwr.edu.pl/~wyloman/ss_2023_2024/lista8_zad1.txt"
page = urlopen(url)
html_lines = page.readlines()
data = [float(line.decode("utf-8")) for line in html_lines]
np.array(data)


print(stats.chisquare(data))

