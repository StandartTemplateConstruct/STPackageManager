# STTouchscreenDeviceHost
A hardware touchscreen device authomatizer


# Device

## Touchscreen clicker 

built on the CNC like rail

webcam attached over the screen of **hosted device** stream

controlled by Raspberry Pi running ROS node

Raspberry Pi is connected to **hosted device** as a ghost keyboard/mouse over USB and/or bluetooth

Additional Raspberry Pi with public ssh access is provided. USB flash storage is connected to both it and **hosted device** - selected by a ROS command from a first switch

# Software 

## Remote control server

Runs on the first Raspberry pi.

 - control of the autoclicker
 - webcam translation
 - HTTP API
   - clicking
   - keyboard input
   - usb switch
 - Web Interface  
   - viewing the camera  
   - clicking
   - keyboard input
   - usb switch
