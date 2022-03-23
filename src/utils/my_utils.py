import pandas as pd
import numpy as np
from shapely import wkb


def haversine(lat1, lon1, lat2, lon2, to_radians=True, earth_radius=6371):
    '''
    Computes the distance between two points on a sphere given their longitudes and latitudes.
    
    Parameters
    ----------
    
    lat1
    lon1
    lat2
    lon2
    to_radians
    earth_radius
    
    '''
    if to_radians:
        lat1, lon1, lat2, lon2 = np.radians([lat1, lon1, lat2, lon2])

    a = np.sin((lat2 - lat1) / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin((lon2 - lon1) / 2.0) ** 2

    return earth_radius * 2 * np.arcsin(np.sqrt(a))


def convert_wkb_to_lat_lon(hex_point):
    '''
    Converts a point in WKB format to a GPS location.
    
    Parameters
    ----------
    
    hex_point : str
        location in hexadecimal (format wkb) as string
        example: "01010000009BBBA7BC674E21C0139447DC08524440"
    
    '''
    
    point = wkb.loads(hex_point, hex=True)
    lon = point.x
    lat = point.y
    return lat, lon


def build_posts_ids(ids):
    '''
    Convert list of short ids to list of long ids.
    
    Parameters
    ----------
    
    ids: list
        RSU's ids
    '''
    return ['urn:ngsi-ld:Values:aveiro_cam:' + pid for pid in ids]
