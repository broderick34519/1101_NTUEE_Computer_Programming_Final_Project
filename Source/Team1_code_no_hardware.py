import time 
import os
import RPi.GPIO as gpio
import webbrowser

# Import from files
import create_bike
import create_user
import borrow
# import gps_and_map
# import motor
# import read_NFC

count = 0

while count < 1:
	
	print("Welcome to our NTU bicycle IOT system! ")
	
	# WAIT FOR CARD
	# print('Please tap your ID card on the NFC reader.')
	# cmd = 'nfc-poll > nfc_output.txt'
	# os.system(cmd)
	
	# motor.main()
	
	
	# Print date and time
	now_time = str(time.ctime())
	print('Time (h:m:s): ' + time.strftime("%H:%M:%S",time.localtime()))
	print('Date (M/D/Y): ' + time.strftime("%m/%d/%y",time.localtime()))
	
	# read_NFC.main(now_time)	
	# gps_and_map.main()
	
	count = count + 1
	
	time.sleep(2)  
	
	
	regORbor = input("Are you registered in our bicycle IOT system ? [Y/N] ")
	while regORbor != "Y" and regORbor != "N":
		temp = input("Invalid input, do you want to exit the system ? [Y/N] ")
		if temp == "Y":
			print("Thank you for your use! Hope to see you again! ")
			exit()
		elif temp == "N":
			regORbor = input("Invalid input, are you registered in our bicycle IOT system ? [Y/N] ")
		else:
			regORbor = "E"

	if regORbor == "N":
		create_user.main()
		create_bike.main()
	else:
		borrow.main() 
