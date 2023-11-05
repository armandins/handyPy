# -----------------------------------------------------------
# This script compares the growth of three functions
# which is a calc. question in using growth rule for
# computation of limits in infinity.
# In order to have a better comparison, natural logs
# of these functions are plotted instead of the original ones.
# Arman Dindar Safa
# 11 / 5 / 2023
# Question from Masoud Aghasi Calc1 book.
# Limits chapter, solved example for limits in infinity section.
# -----------------------------------------------------------

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

# Latex font setup
# -----------------------------------------------------------
font_dirs = ['C:\Windows\Fonts']
font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
 
for font_file in font_files:
    font_manager.fontManager.addfont(font_file)

plt.rcParams['font.family'] = 'Latin Modern Roman'
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Latin Modern Roman'
plt.rcParams['mathtext.it'] = 'Latin Modern Roman:italic'
plt.rcParams['mathtext.bf'] = 'Latin Modern Roman:bold'
plt.rcParams['font.size'] = '12'

# -----------------------------------------------------------
# setting up functions 
x = np.linspace(0, 150, 450)
y1 = (np.log(x)) ** 2
# z is used as an auxilary function
z = np.log(x) 
y2 = x * np.log(z)
y3 = x * np.log(4)
# -----------------------------------------------------------

# -----------------------------------------------------------
# Plot the data
plt.plot(x, y1, label = "$f(x) = x ^ ln(x)$", color = 'cyan', linestyle = '--')
plt.plot(x, y2, label = "$f(x) = (ln(x))^x$", color = 'red', linestyle = '-.')
plt.plot(x, y3, label = "$f(x) = 4^x$", color = 'black', linestyle = ':')
plt.xlabel("x")
plt.ylabel("Natural Log of y function")
plt.title("Growth comparison of three functions")
plt.legend()
# Generates plots in the existing directory 
plt.savefig("InfGrowthRuleComp.pdf")
plt.savefig("InfGrowthRuleComp.eps")
plt.savefig("InfGrowthRuleComp.png", dpi = 300)
plt.show()
# -----------------------------------------------------------