from baladin import Aladin
from radec import get_equinox_radec


cal_years = [-4000, -3000, -2000, -1000, -559, -1, 636, 1000, 2000]
#kernel_fol = 'C:/Moi/_py/Astronomy/Solar System/kernels/'
kernel_fol = 'C:/Users/H21/Desktop/Desktop/Behrouz/Astronomy/kernels/'

dc = get_equinox_radec(cal_years, kernel_fol)

markers = []
for k,v in dc.items():
    markers.append((v[0], v[1], str(k), str(k)))

a = Aladin(target='68.9801627900154 16.5093023507718', fov=90)

buttons = [
    ('P/2MASS/color', 'bs 2MASS'),
    ('P/GLIMPSE360', 'bs GLIMPSE 360'),
    ]


a.add_markers(markers)
a.create()
a.save('index.html')

