Smart IoT Platform for Bicycle Sharing & Management, Code Package - version 1.0
Final project for the course 110-1 Computer Programming at NTUEE

Chou-Wei Kiang, Chung-Ting Wang, and Yu-Chia Liu, Jan. 2022.
Department of Electrical Engineering, National Taiwan University
E-mail: b07611026@ntu.edu.tw, b07611008@ntu.edu.tw, b07504016@ntu.edu.tw

1. Please first cd to the directory '....../Team1_code'
2. To initiate server locally, cd to './localliabrary'
3. Use the command: 'python3 manage.py runserver'
   Browsing http://127.0.0.1:8000/catalog/ for frontend page
   Browsing http://127.0.0.1:8000/admin/ for backend page
4. If with hardware, please execute 'python3 Team1_code.py'
   If without hardware, please execute 'python3 Team1_code_no_hardware.py'

* For more details on server setup and modification, 
please read the instructions in 'server_detail.pdf' under 'Team1_code' directorys

Main functions:
  
  Team1_code.py             => Main function of the project
  Team1_code_no_hardware.py => Main function of the project, can be run with no hardware

Lower level functions:
  
  borrow.py       =>  Guide users to fill up information needed and borrow a bicycle, with Selenium used to upload data to the server
  create_bike.py  =>  Guide users to fill up information needed and register data for a bicycle, with Selenium used to upload data to the server
  create_user.py  =>  Guide users to fill up information needed and create user account, with Selenium used to upload data to the server
  gps_and_map.py  =>  To read GPS data (longitude and latitude) and show location on Google Map
  gps_test.sh     =>  Shell file to capture GPS data streamed from Android phone through Wi-fi, save data in 'gps_lon.txt' and 'gps_lat.txt'
  motor.py        =>  To control and actuate the motor through H-bridge
  read_NFC.py     =>  To poll the NFC/RFID module to read the card number (hexadecimal) and save data in 'nfc_output.txt' and 'card_ID.txt'

Other files:

  requirement.txt     =>  Details on environment, software, and hardware setup and requirements
  pin_assignment.jpg  =>  Details on hardware wiring
  server_detail.pdf   =>  Details on server setup and modification