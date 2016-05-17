#!/usr/bin/python
 
import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import palettable
from palettable.colorbrewer.qualitative import Dark2_3 
from argparse import ArgumentParser

# Global matplotlib parameters
params = {
	'axes.labelsize': 16,
	'axes.titlesize': 16,
	'font.size': 18,
	'legend.fontsize': 14,
	'xtick.labelsize': 12,
	'ytick.labelsize': 12,
	'text.usetex': False,
	'figure.figsize': [10.0, 10.0]
}
mpl.rcParams.update(params)

# options handling
parser = ArgumentParser(description="Python version of Scilabus matlab code")
parser.add_argument("--path")
parser.add_argument("--output")
options = parser.parse_args()
print options.path, options.output

# Load data from provided folder
data = []
data.append(np.loadtxt(options.path+'/accXYZ.csv', delimiter=','))
data.append(np.loadtxt(options.path+'/gyrXYZ.csv', delimiter=','))
data.append(np.loadtxt(options.path+'/velXYZ.csv', delimiter=','))
data.append(np.loadtxt(options.path+'/distXYZ.csv', delimiter=','))

timeData = np.loadtxt(options.path+'/time.csv', delimiter=',')

# Prepare arrays for loop plotting
titles=["Acceleration", "Angular speed", "Linear speed", "Distance"]
units=[r"$m/s^2$", r"$\degree/s$", r"$m/s$", r"$m$"]
directions=[r"$x$", r"$y$", r"$z$"]


# Fancy colors :
colors=Dark2_3.mpl_colors

# Create figure with a global subplot to allow a common xlabel
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])
ax.xaxis.labelpad = 20
ax.yaxis.labelpad = 20

# Plot data :
c1 = 0
for d in data:
	ax2 = fig.add_subplot(2,2, c1+1)
	plt.grid()
	c2 = 0
	for l in zip(*d):
		#print l
		plt.plot(timeData, l, color=colors[c2], linewidth=2, label=directions[c2])
		c2+=1
	ax2.set_ylabel(units[c1])
	ax2.set_title(titles[c1])
	if c1 == 0:
		ax2.legend(loc=0)
	c1+=1

ax.set_xlabel("Time (s)")
plt.tight_layout()
plt.subplots_adjust(top=0.90)
plt.suptitle("Data : "+options.path)

# Save figure to pdf file if requested :
if options.output is not None:
	filename = options.output+".pdf"
	print "\033[32mSaving figure to :\033[39m", filename
	fig.savefig(options.output+".pdf", dpi="200")

plt.show()

