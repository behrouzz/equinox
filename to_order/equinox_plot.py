import hypatie as hp
import numpy as np
import matplotlib.pyplot as plt
from astropy.coordinates import Angle
import astropy.units as u


def radec_correction(ra, dec):
    ra_rad = Angle(ra * u.deg).wrap_at(180 * u.deg).radian
    dec_rad = Angle(dec * u.deg).radian
    return -ra_rad, dec_rad


def radec_correction_old(ra, dec):
    ra_ = -np.where(ra>=180, 180-ra, ra) * (np.pi/180)
    dec_ = dec * (np.pi/180)
    return ra_, dec_

markers = [
    (82.11244395876318, 24.017187865322565, '-4000', '-4000'),
    (67.30515645040853, 22.400875278633578, '-3000', '-3000'),
    (52.94041247000641, 19.511255848758573, '-2000', '-2000'),
    (39.101991212026405, 15.559949833427346, '-1000', '-1000'),
    (25.76407698927707, 10.805399597802593, '1', '1'),
    (12.811563024834374, 5.532548754217401, '1000', '1000'),
    (0.0008021574031798603, 0.00042504742866794306, '2000', '2000')]

years = [i[-1][1:]+' BC' if ('-' in i[-1]) else i[-1]+' AD' for i in markers]



RA = np.array([i[0] for i in markers])
DEC = np.array([i[1] for i in markers])

RA, DEC = radec_correction(RA, DEC)
SIZE = len(RA) * [40]


from skychart.load_data import *
from skychart.plotting import *
df = load_hipparcos()
df['ra'], df['dec'] = radec_correction(df['ra'].values, df['dec'].values)


aldeb_ra, aldeb_dec = radec_correction(68.9801627900154, 16.5093023507718)

# constellations
dc_const = load_constellations()
selection = ['Tau', 'Ari', 'Psc', 'Ori']
dc_const = {k:v for k,v in dc_const.items() if k in selection}
edges = create_edges(dc_const)
edges = [i for i in edges if (i[0] in df.index) and (i[1] in df.index)]
edge1 = [i[0] for i in edges]
edge2 = [i[1] for i in edges]
xy1 = df[['ra', 'dec']].loc[edge1].values
xy2 = df[['ra', 'dec']].loc[edge2].values
lines_xy = np.array([*zip(xy1,xy2)])



df = df[df['Vmag']<4]
mag_max = df['Vmag'].max()
size = (1 + mag_max - df['Vmag'].values) ** 2
ra, dec = df['ra'].values, df['dec'].values

ann = [*zip(RA,DEC)]


fig = plt.figure()
ax = fig.add_subplot(111, projection="aitoff")
ax.add_collection(LineCollection(lines_xy, color='cyan', alpha=0.7))

ax.grid(True)
ax.scatter(ra, dec, c='k', s=size)
ax.scatter(RA, DEC, c='r', s=SIZE)
plt.subplots_adjust(top=0.95, bottom=0.0)
plt.xlabel('RA')
plt.ylabel('Dec')
ax.set_xticklabels([])
ax.set_yticklabels([])


for i in range(len(ann)):
    label = years[i]
    ax.annotate(label,
                 (ann[i][0], ann[i][1]),
                 textcoords="offset points",
                 xytext=(0,5),
                 ha='center')
    ax.annotate('Aldebaran\n(Tascheter)',
                xy=(aldeb_ra, aldeb_dec),
                xytext=(aldeb_ra-1.8, aldeb_dec+0.1),
                arrowprops=dict(facecolor='black', shrink=0.03),
                )


plt.show()
