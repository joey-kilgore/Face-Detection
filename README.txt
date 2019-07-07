# Face-Detection  

Utilize a Raspberry pi and camera along with a 7segment display to count the number of faces in the image.  
Note you need cv2 on the pi, which takes a long time to setup.  
The wiring for the display is as follows:  
The GPIO pins are shown next to each of the display segments  
   2  
  ---
7| 8 |3  
  ---  
6|   |4 
  ---  
   5  
Use 1kOhm resistors between the pins and the input for the display. 
test.py is meant to take 10 photos, 10 seconds apart. At any point hit ctrl+c to kill the program and 
then you can open the result.jpg with the command 'fim result.jpg'
