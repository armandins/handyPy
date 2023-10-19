# Raw setup intended for a simple copy-paste from the script to the main code

from matplotlib import font_manager

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