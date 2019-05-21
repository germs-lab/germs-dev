from matplotlib import pyplot as plt
import pandas as pd
import sys

dat = pd.read_csv(sys.argv[1], sep=" ", header=None)
dat.columns = ["reference", "index", "count"]
dat.plot(x='index',y='count', style='o', markersize=1, legend = None)
plt.xlabel("Location")
plt.ylabel("Total Number of Mapped Reads")
plt.savefig("/Users/adinahowe/Downloads/" + str(dat.iloc[0,0]) + '.png')

