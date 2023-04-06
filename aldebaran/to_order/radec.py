import os
from urllib.request import urlretrieve
import pandas as pd
import spiceypy as sp
from hypatie import car2sph


def get_equinox_radec(cal_years, kernel_fol):

    url = 'https://github.com/behrouzz/astrodata/raw/main/equinox/'
    file = 'equinox_time.csv'

    if not os.path.isfile(file):
        urlretrieve(url+file , file)
        print(f'{file} downloaded.\n')

    df = pd.read_csv(file)

    df_years = [i+1 if i<=0 else i for i in cal_years]
    df = df[df['greg_year'].isin(df_years)]

    sp.furnsh(kernel_fol+'de441_part-1.bsp')
    sp.furnsh(kernel_fol+'de441_part-2.bsp')

    dc = {}
    for i in range(len(df)):
        et = df['et'].iloc[i]
        pos, _ = sp.spkez(10, et, 'J2000', 'LT+S', 399)
        ra, dec, _ = car2sph(pos[:3])
        dc[cal_years[i]] = (ra, dec)
        
    sp.kclear()
    return dc

