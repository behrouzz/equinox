import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.collections import LineCollection
from data import markers, years, dc_const
from data import ra_cyrus, dec_cyrus, ra_muslim, dec_muslim
from skychart.load_data import load_hipparcos, create_edges
from annotation import add_annotation
from utils import wrap180, wrap360



RA_cyrus, DEC_cyrus = wrap180(ra_cyrus, dec_cyrus)
RA_muslim, DEC_muslim = wrap180(ra_muslim, dec_muslim)

RA = np.array([i[0] for i in markers])
DEC = np.array([i[1] for i in markers])

RA, DEC = wrap180(RA, DEC)

df = load_hipparcos()
df['ra'], df['dec'] = wrap180(df['ra'].values, df['dec'].values)

# constellations
edges = create_edges(dc_const)
edges = [i for i in edges if (i[0] in df.index) and (i[1] in df.index)]
edge1 = [i[0] for i in edges]
edge2 = [i[1] for i in edges]
xy1 = df[['ra', 'dec']].loc[edge1].values
xy2 = df[['ra', 'dec']].loc[edge2].values
lines_xy = np.array([*zip(xy1,xy2)])

df = df[df['Vmag']<5]
mag_max = df['Vmag'].max()
size = (1 + mag_max - df['Vmag'].values) ** 2
ra, dec = df['ra'].values, df['dec'].values

ann = [*zip(RA,DEC)]

fig = plt.figure()
ax = fig.add_subplot(111, projection="rectilinear")
ax.add_collection(LineCollection(lines_xy, color='cyan', alpha=0.7))

#ax.grid(True)
ax.scatter(ra, dec, c='k', s=size)
ax.scatter(RA, DEC, c='r', s=50)
ax.scatter([RA_cyrus, RA_muslim], [DEC_cyrus, DEC_muslim], c='r', s=20, marker='x')
plt.xlabel('RA')
plt.ylabel('Dec')

ax = add_annotation(ax, ann)

plt.xlim(-1.8, 0.23)
plt.ylim(-0.32, 0.65)

label_format = '{:,.0f}'

ticks_ra = ax.get_xticks().tolist()
ticks_dec = ax.get_yticks().tolist()
ticks_RA, ticks_DEC = wrap360(ticks_ra, ticks_dec)

ax.xaxis.set_major_locator(mticker.FixedLocator(ticks_ra))
ax.set_xticklabels([label_format.format(x) for x in ticks_RA])

ax.yaxis.set_major_locator(mticker.FixedLocator(ticks_dec))
ax.set_yticklabels([label_format.format(x) for x in ticks_DEC])

plt.title('Precession of the Vernal Equinox during the History | AstroDataScience.Net')
plt.show()
