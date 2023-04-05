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
