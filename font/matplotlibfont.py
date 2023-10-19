import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager
import matplotlib

# --------------------------------------------------------
# ------------- Font setup -------------------------------

# Path to the fonts directory, default setup for win 10 
# To find the path on your system: Win + E -> shell:fonts   
font_dirs = ['C:\Windows\Fonts']
font_files = font_manager.findSystemFonts(fontpaths=font_dirs)

for font_file in font_files:
    font_manager.fontManager.addfont(font_file)

# Latin Modern Roman if you want a LaTeX look in your final doc. 
plt.rcParams['font.family'] = 'Latin Modern Roman'
plt.rcParams['font.size'] = '12' # default == 14

# ---------- End of font setup --------------------------
# -------------------------------------------------------

x1 = [0, 1, 2, 3, 4, 5]
y1 = [0, 6, 3, 8, 7, 5]

plt.title('title')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.plot(x1, y1)
plt.show()
