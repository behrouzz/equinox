import hypatie as hp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.collections import LineCollection
from astropy.coordinates import Angle
import astropy.units as u


def wrap180(ra, dec):
    ra_rad = -Angle(ra * u.deg).wrap_at(180 * u.deg).radian
    dec_rad = Angle(dec * u.deg).radian
    return ra_rad, dec_rad


def wrap360(ra, dec):
    ra = -Angle(ra * u.rad).wrap_at(360 * u.deg).degree % 360
    dec = Angle(dec * u.rad).degree
    return ra, dec


markers = [
    (82.11244395876318, 24.017187865322565, '-4000', '-4000'),
    (67.30515645040853, 22.400875278633578, '-3000', '-3000'), #Elamite Kingdom / Invention of writing
    (52.94041247000641, 19.511255848758573, '-2000', '-2000'),
    (39.101991212026405, 15.559949833427346, '-1000', '-1000'),
    (25.76407698927707, 10.805399597802593, '1', '1'),
    (12.811563024834374, 5.532548754217401, '1000', '1000'),
    (0.0008021574031798603, 0.00042504742866794306, '2000', '2000')]

years = [i[-1][1:]+' BC' if ('-' in i[-1]) else i[-1]+' AD' for i in markers]

#(33.161615897177576, 13.544914103494255, '-559', '-559') #Kingdom of Cyrus the Great
#(17.499042382107994, 7.496435624803013, '636', '636') #Muslim invasion

ra_cyrus, dec_cyrus = 33.161615897177576, 13.544914103494255
RA_cyrus, DEC_cyrus = wrap180(ra_cyrus, dec_cyrus)

ra_muslim, dec_muslim = 17.499042382107994, 7.496435624803013
RA_muslim, DEC_muslim = wrap180(ra_muslim, dec_muslim)


RA = np.array([i[0] for i in markers])
DEC = np.array([i[1] for i in markers])

RA, DEC = wrap180(RA, DEC)
#SIZE = len(RA) * [50]


from skychart.load_data import *
df = load_hipparcos()
df['ra'], df['dec'] = wrap180(df['ra'].values, df['dec'].values)


aldeb_ra, aldeb_dec = wrap180(68.9801627900154, 16.5093023507718)

# constellations
dc_const = load_constellations()
selection = ['Tau', 'Ari', 'Psc', 'Ori']#, 'Gem']
dc_const = {k:v for k,v in dc_const.items() if k in selection}
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

ax.grid(True)
ax.scatter(ra, dec, c='k', s=size)
ax.scatter(RA, DEC, c='r', s=50)
ax.scatter([RA_cyrus, RA_muslim], [DEC_cyrus, DEC_muslim], c='r', s=20, marker='x')
#plt.subplots_adjust(top=0.95, bottom=0.0)
plt.xlabel('RA')
plt.ylabel('Dec')


for i in range(len(ann)):
    label = years[i]
    ax.annotate(label,
                 (ann[i][0], ann[i][1]),
                 textcoords="offset points",
                 xytext=(0,5),
                 ha='center')
    ax.annotate('Aldebaran',
                xy=(aldeb_ra, aldeb_dec),
                xytext=wrap180(67,12),
                arrowprops=dict(arrowstyle='->', color='g', shrinkB=3, lw=2),
                ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.2', fc='white', alpha=0.3),
                )
    ax.annotate('Pleiades',
                xy=wrap180(56.601-0.25,24.114),
                xytext=wrap180(50,27),
                arrowprops=dict(arrowstyle='->', color='g', shrinkB=3, lw=2),
                ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.2', fc='white', alpha=0.3),
                )

    ax.annotate('Elamite Kingdom\nInvention of writing',
                xy=wrap180(*markers[1][:2]),
                xytext=wrap180(67,33),
                arrowprops=dict(facecolor='black', shrink=0.2),
                horizontalalignment='center',
                verticalalignment='center',
                bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3),
                )
    ax.annotate('Kingdom of\nCyrus the Great',
                xy=(RA_cyrus, DEC_cyrus),
                xytext=wrap180(40,-5),
                arrowprops=dict(facecolor='black', shrink=0.05),
                horizontalalignment='left',
                verticalalignment='bottom',
                bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3),
                )
    ax.annotate('Muslim invasion',
                xy=(RA_muslim, DEC_muslim),
                xytext=wrap180(17.5,-5),
                arrowprops=dict(facecolor='black', shrink=0.05),
                horizontalalignment='center',
                verticalalignment='center',
                bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3),
                )

#plt.xlim(-2, 0.32)
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


plt.show()
