#!/usr/bin/python
 
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import palettable
#from palettable.colorbrewer.sequential import Greys_9, Greys_9_r, Reds_9, Reds_9_r, YlOrRd_9, YlOrRd_9_r, Greens_9 
from palettable.colorbrewer.qualitative import Dark2_3 
from argparse import ArgumentParser
 
#from os import listdir
#from os.path import isfile, join

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

titles=["Acceleration", "Angular speed", "Linear speed", "Distance"]
units=[r"$m/s^2$", r"$\degree/s$", r"$m/s$", r"$m$"]
directions=[r"$x$", r"$y$", r"$z$"]

timeData = np.loadtxt(options.path+'/time.csv', delimiter=',')

colors=Dark2_3.mpl_colors

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

if options.output is not None:
	filename = options.output+".pdf"
	print "\033[32mSaving figure to :\033[39m", filename
	fig.savefig(options.output+".pdf", dpi="200")

plt.show()

#runData = options.dataPath + "/" + poseOverTime
#fichier1=np.genfromtxt(runData)
#with open(options.dataPath+"/"+mapsOverTime[-1]) as f:
#	for line in f:
#		try:
#			(key, val) = line.split(":")
#		except ValueError:
#			break
#		paramDict[key] = val[1:].strip('\n')
#
#paramGlobalDict = {}
#with open(options.dataPath+"/"+expGlobalParam) as f:
#	for line in f:
#		try:
#			(key, val) = line.split(":")
#		except ValueError:
#			break
#		paramGlobalDict[key] = val[1:].strip('\n')
#		#print key, val
#
#img=mpimg.imread(options.dataPath+"/"+paramDict['image'])
#resolution = float(paramDict['resolution'])
##offset = ((paramDict['origin'][1:(len(paramDict['origin'])-1)].strip(" ")).split(','))
#offset = ((paramDict['origin'][1:(len(paramDict['origin'])-1)]).replace(" ","")).split(',')
#offset = [float(i) for i in offset]
##print offset
#
#
#clk_fichier=fichier1[:,0]	
#x_fichier=fichier1[:,1]
#y_fichier=fichier1[:,2]
#
#duree=(clk_fichier.max()-clk_fichier.min())/60
#tronc1=round(duree,1)
#titre=options.dataPath+"\n"+str(tronc1) + " min of simulation ;" + ''.join([' %s: %s ;' % (key, value) for (key, value) in paramGlobalDict.items()])
##titre=str(tronc1) + " min of simulation, " + str(paramGlobalDict).strip("{}'`")
#np.random.seed(0)
#
#
#x = x_fichier
#y = y_fichier
#
#xmin = (x.min() - offset[0]) / resolution
#xmax = (x.max() - offset[0]) / resolution
#ymin = (y.min() - offset[1]) / resolution
#ymax = (y.max() - offset[1]) / resolution
#xv = (x - offset[0]) / resolution
#yv = (y - offset[1]) / resolution
#xc = (fichier2[:,1] - offset[0]) / resolution
#yc = (fichier2[:,2] - offset[1]) / resolution
#pointsForVoronoi = zip(xc, yc)
##print zip(xc, yc)
##print xv[0],yv[0]
#vor = Voronoi(pointsForVoronoi)
#
##fig = plt.figure()
#fig = voronoi_plot_2d(vor)
##plt.subplot(1,1,1)
## Background:
#plt.imshow(img, cmap=Greys_9_r.mpl_colormap, zorder=0, alpha=1.0, label="Map")
##plt.imshow(img, cmap=Greys_9_r.mpl_colormap, zorder=0, alpha=0.3)
## Visits:
#plt.hexbin(xv, yv, bins='log', cmap=Greens_9.mpl_colormap, gridsize=20, alpha=0.5, zorder=1, label="time spent in areas")
#cb = plt.colorbar(orientation='horizontal', fraction=0.05)
## Path:
#plt.plot(xv, yv, color="k", marker="o", alpha=0.3)
## Centers:
#plt.scatter(xc, yc, c='r', s=100, zorder=3, label="States")
#plt.plot(xv[0], yv[0], c='b', marker ='o', markersize=20, zorder=2, label="Starting position")
#plt.axis([xmin-10, xmax+10, ymin-10, ymax+10])
#plt.title(titre)
#plt.legend(loc=0)
##plt.legend(loc=4, bbox_to_anchor=(0.5, -1))
##plt.gca().invert_yaxis()
#cb.set_label('# positions in area / log10(N)')
#print options.dataPath
#print options.outputPath
#fig.savefig("./"+options.outputPath+".pdf", format="pdf", dpi=600)
#fig.savefig("./"+options.outputPath+".png", format="png", dpi=600)
##fig.savefig("./aggregMaps/"+options.dataPath+".pdf", format="pdf", dpi=600)
##fig.savefig("./aggregMaps/"+options.dataPath+".png", format="png", dpi=600)
#
##voronoi_plot_2d(vor)
##plt.imshow(img, cmap=Greys_9_r.mpl_colormap)
##plt.imshow(img, cmap=Greys_9_r.mpl_colormap, alpha=0.5)
#
##plt.show()
