# RaspberryPi Wifi Camera
 
Local Network streaming using RaspberryPi 5 and Camera Module 3

STEP 1: Install Lite or desktop version of the latest Pi OS

STEP 2: setup your network 

<img width="200" alt="Screenshot 2024-03-14 at 2 00 08 PM" src="https://github.com/javicar31/RaspberryPi-Wifi-Cam/assets/163356846/17646130-9a16-460b-940b-dd3d42aad1c6">

STEP 3: SSH into your freshly booted Pi, it might take a few minutes to boot.   ~ $ ssh [username]@[hostname].local OR ~ $ ssh [username]@[IP address]

STEP 4:~ $ sudo apt update
~ $ sudo apt full-upgrade

STEP 5: Test camera module:~ $ rpicam-hello

STEP 6: on the RaspberryPi Terminal ~ $ rpicam-vid -t 0 --inline --listen -o tcp://0.0.0.0:8000

STEP 7: assuming you have ffplay on your MAC open terminal ~ % ffplay tcp://'YOUR_RASPBERRY_IP':8000 -vf "setpts=N/30" -fflags nobuffer -flags low_delay -framedrop

Replace 'YOUR_RASPBERRY_IP' with your IP 

PRESS 'Q' on popup window to quit or 'Control-C' on your MAC terminal 


