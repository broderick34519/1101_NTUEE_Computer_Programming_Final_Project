import os
import webbrowser


def main():
	cmd2 = 'sh gps_test.sh'
	os.system(cmd2)
	Lon_file = 'gps_lon.txt'
	Lat_file = 'gps_lat.txt'
	Long = ''
	Lati = ''
	with open(Lat_file,'r') as f3:
		Lati = f3.readline().replace('\n','') + ' N'
	with open(Lon_file,'r') as f2:
		Long = f2.readline().replace('\n','') + ' E'
	print("Current Location (Lat, Lon): (" + Lati + ', ' + Long + ')')

	map_string = Lati + ', ' + Long
	webbrowser.open('https://www.google.com/maps/place/' + map_string)
