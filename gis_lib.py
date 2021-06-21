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
	north_err = (true[0] - reading[0])
	east_err = (true[1] - reading[1])
	total_error = np.sqrt(north_err**2 + east_err**2)
	print('Coordinate error of ' + str(north_err) + ' ft north and ' + str(east_err) + ' ft east.')


#railroad
#true_lat = 30.484588316
#true_lon = 90.952812394

#railroad
#reading_lat = 30.48458833
#reading_lon = 90.95281300




#overpass
#true_lat =  30.45703143
#true_lon = -90.94661762

#overpass
#reading_lat = 30.45703150
#reading_lon = -90.94661733

#Y-4 Corner (raw)
#true_lat =  30.483614905
#true_lon = -90.930939159

#Y-4 Corner (EPSG:3857 to EPSG:4326)
#true_lat =  30.4845937472222
#true_lon = -90.9528201361111

#Y-4 Corner
#reading_lat =  30.484588316
#reading_lon = -90.952812394

#test true
true_lat =  30.4853601690098
true_lon = -90.931335658468


#test reading
reading_lat =  30.48534917
reading_lon = -90.93133617

print(errordist())
