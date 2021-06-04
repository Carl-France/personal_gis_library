from pyproj import Transformer
import numpy as np

def crs_converter (coord1, coord2, EPSGin, EPSGout):
	transformer = Transformer.from_crs(EPSGin, EPSGout, always_xy=True)
	lonlat = transformer.transform(coord1, coord2)
	return lonlat

def WGS84toSPCS (lat, lon):
	transformer = Transformer.from_crs("EPSG:4326", "EPSG:6479", always_xy=True)
	cartesian = transformer.transform(lon, lat)
	east = cartesian[0]
	north = cartesian[1]
	return [north, east]

def errordist():
	true = WGS84toSPCS(true_lat, true_lon)
	reading = WGS84toSPCS(reading_lat, reading_lon)
	north_err = (true[0] - reading[0]) * 12
	east_err = (true[1] - reading[1]) * 12
	total_error = np.sqrt(north_err**2 + east_err**2)
	print('Coordinate error of ' + str(north_err) + ' inch north and ' + str(east_err) + ' inch east.')


#railroad
#true_lat = 30.484588316
#true_lon = 90.952812394

#railroad
#reading_lat = 30.48458833
#reading_lon = 90.95281300




#overpass
true_lat =  30.45703143
true_lon = -90.94661762

#overpass
reading_lat = 30.45703150
reading_lon = -90.94661733


print(crs_converter(30.45703143, -90.94661762, 'EPSG:6319', 'EPSG:4326'))








print(errordist())

"""
without houston rtk:
30.48459683 -90.95282300
 3.27 ft north
-3.16 ft east

with houston rtk:
	30.48459150 -90.95281133 
-0.35 feet north
-1.15 east

""" 