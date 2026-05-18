import math

def geodist(lat1, lon1, lat2, lon2):
    grad_rad = 0.01745329
    rad_grad = 57.29577951

    longitud = lon1-lon2
    val = (math.sin(lat1*grad_rad)*math.sin(lat2*grad_rad)) \
    + (math.cos(lat1*grad_rad)* math.cos(lat2*grad_rad)*math.cos(longitud*grad_rad))
    return (math.acos(val)*rad_grad)*111.32