#####################X######X######################
# Created by:       Javicar31                     #
# On                March 2024                    #
# X-Y servo control with local camera conectivity #
#####################X##X##########################

from adafruit_servokit import ServoKit
import curses
import time
import subprocess

# Initialize the ServoKit instance for 16 channels
kit = ServoKit(channels=16)

def start_camera_stream():
    # The command to start camera streaming
    cmd = ['rpicam-vid', '-t', '0', '--inline', '--listen', '-o', 'tcp://0.0.0.0:8000'] #You would connect to:
    #ffplay tcp://YOURIP:8000-vf "setpts=N/30" -fflags nobuffer -flags low_delay -framedrop
  
    # Starts the camera streaming process in the background
    return subprocess.Popen(cmd)

def smooth_servo_move(servo, target_position, step=1):
    current_position = servo.angle
    if current_position < target_position:
        for pos in range(int(current_position), int(target_position), step):
            servo.angle = pos
            time.sleep(0.02)  # Delay to control the speed of movement
    else:
        for pos in range(int(current_position), int(target_position), -step):
            servo.angle = pos
            time.sleep(0.02)  # Delay to control the speed of movement

def smooth_servo_control(win):
    # Start the camera stream
    camera_process = start_camera_stream()

    # Initial servo positions
    servo1_position = 90
    servo2_position = 90

    # Set initial positions
    kit.servo[0].angle = servo1_position
    kit.servo[2].angle = servo2_position

    win.nodelay(True)
    key = ""
    win.clear()
    win.addstr("Smoothly adjusting servos. Use arrow keys to move and 'q' to exit.")
    step = 1  # Smaller step size for finer control

    try:
        while True:
            try:
                key = win.getkey()
                win.clear()

                if key == 'q':
                    break
                elif key == 'KEY_LEFT':
                    servo1_position = max(0, servo1_position - 5)  # Change of 5 degrees
                    smooth_servo_move(kit.servo[0], servo1_position, step)
                elif key == 'KEY_RIGHT':
                    servo1_position = min(180, servo1_position + 5)  # Change of 5 degrees
                    smooth_servo_move(kit.servo[0], servo1_position, step)
                elif key == 'KEY_UP':
                    servo2_position = max(0, servo2_position - 5)  # Change of 5 degrees
                    smooth_servo_move(kit.servo[2], servo2_position, step)
                elif key == 'KEY_DOWN':
                    servo2_position = min(180, servo2_position + 5)  # Change of 5 degrees
                    smooth_servo_move(kit.servo[2], servo2_position, step)

                status = f"Servo 1 Position: {servo1_position}, Servo 2 Position: {servo2_position}"
                win.addstr(status)

            except Exception as e:
                # Handle case where key press is not recognized
                win.addstr(0, 0, 'Error: ' + str(e))
    finally:
        # Clean up
        camera_process.terminate()

# curses wrapper to initialize the window and clean up properly
curses.wrapper(smooth_servo_control)
