from baladin import Aladin
import pandas as pd
import spiceypy as sp
from hypatie import car2sph
import os
from urllib.request import urlretrieve

url = 'https://github.com/behrouzz/astrodata/raw/main/equinox/equinox_time.csv'

file = url.split('/')[-1]

if not os.path.isfile(file):
    urlretrieve(url , file)

df = pd.read_csv(file)

adr = 'C:/Moi/_py/Astronomy/Solar System/kernels/'

sp.furnsh(adr+'de441_part-1.bsp')
sp.furnsh(adr+'de441_part-2.bsp')


cal_years = [-4000, -3000, -2000, -1000, -559, -1, 636, 1000, 2000]
df_years = [i+1 if i<=0 else i for i in cal_years]
df = df[df['greg_year'].isin(df_years)]



markers = []
for i in range(len(df)):
    et = df['et'].iloc[i]
    pos, _ = sp.spkez(10, et, 'J2000', 'LT+S', 399)
    ra, dec, _ = car2sph(pos[:3])
    markers.append((ra, dec, str(cal_years[i]), str(cal_years[i])))
    

sp.kclear()


a = Aladin(target='68.9801627900154 16.5093023507718', fov=90)

buttons = [
    ('P/2MASS/color', 'bs 2MASS'),
    ('P/GLIMPSE360', 'bs GLIMPSE 360'),
    ]


a.add_markers(markers)
a.create()
a.save('index.html')

