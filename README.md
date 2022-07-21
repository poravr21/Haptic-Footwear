# Haptic-Footwear
The "Haptic Footwear" project was conducted by the Electronics Club, under the Science and Technology Council of IIT Kanpur. The essential aim of the project is to build smart shoes through which you will be able to save your valuable time through hassle-free navigation, track and analyze your activity levels and stop tripping over objects. These shoes would help the disabled navigate and abled emancipate themselves from bulky and inaccurate electronic devices.

Smartphone GPS facilities are used to provide turn-by-turn routing information through Bluetooth to the microcontroller in the shoe, which is communicated via Vibration Actuators.

<p align = "center">
  <img src="https://user-images.githubusercontent.com/97837018/180019309-cd439e3b-34f3-402b-9a2e-2c5ed44fe0ac.png" width="350" height="300" />
</p>
The shoe has pressure sensors and an accelerometer which will provide us with data.

A smartphone performs real-time fall risk estimation through signal processing, pattern recognition, and classification. 

<p align = "center">
  <img src="https://user-images.githubusercontent.com/97837018/180019054-eaa105e3-ed8d-464a-9d20-eea4fd864764.png" width="600" height="500" />
</p>

The main learning outcomes from this project were:

--> **Understanding Arduino and other microcontrollers:** Arduino was used by us, in building an LED Circuit as well as a controllable RGB Light. We used Arduino Pro Mini in the shoes, to track user data without being a hindrance to the mobility of the user.

--> **Used a WiFi controlled Node MCU for glowing a LED bulb:** We developed an App on MIT App Inventor which communicated with NODE-MCU to wirelessly control an LED. NodeMCU is a low-cost open source IoT platform. It includes firmware which runs on the ESP8266 Wi-Fi SoC from Espressif Systems, and hardware which was based on the ESP-12 module. This app runs on a device connected to the same network as the Node-MCU  and is used to communicate specific instructions to it as per the input from the user.

--> **Used MIT App Inventor to make a mobile App which Uses Bluetooth to communicate with Arduino:** We build an app on MIT App Inventor  in order to wirelessly control an LED through a smartphone using Arduino and Bluetooth Modules. This app sends an input as per the button pressed through the Bluetooth client to the Bluetooth module and thus to the microcontroller which then identifies the input and performs the defined task of turning on or turning off the LED. 

--> **Used HC05 Bluetooth Module and MIT App Inventor to toggle an LED and count steps via a force sensor.** Using the pressure sensors available, we built a simple circuit that could help us count the number of steps taken by the person who wears the shoes. This step counter app was built via MIT App Inventor.

 
<p align = "center">
  <img src="https://user-images.githubusercontent.com/107315402/180048899-94bd5ddd-f2b0-4696-b10b-244f30d44cba.jpeg" width="550" height="400" />
</p>


<p align = "center">
  <img src="https://user-images.githubusercontent.com/97837018/180020216-1b32721d-4505-4813-9361-b05705d02f15.png" width="550" height="400" />
</p>

--> **Used Ultrasonic and IR Sensors for Obstacle detection:** The ultrasonic sensor and IR sensor was successfully put to use using the in-built functions in Arduino IDE. The circuits were built using Arduino UNO connected to a laptop along with a breadboard. It could give approximate distances to major obstacles which was further put to use for computations/algorithms that help in fall prevention.

--> **Learned about various Graph Algorithms to find shortest paths:** We learnt various Graph Algorithms which aim to find the shortest path between two nodes of a graph. Through this, we essentially try to model a path where we receive the start and the end nodes as the current and the destination locations of the user and our footwear uses these algorithms to help the user with the navigation. We used Dijikstra's Algorithm for navigation, but also learnt about Floyd Warshall's algorithm and spanning trees as well.

--> **Read various research papers on performing fall prevention via LIDAR/ Stereo Cameras and performing obstacle detection algorithms with the data recieved:** We learnt how camera-based line-laser obstacle detection system is useful for designing fall prevention shoes for users. Also, we learned how Radar could be useful for measuring gait parameters and performing fall risk-assessment using statistical methods and could also be used to monitor obstacles in real-time (explained in the below research paper)

[Fall Prevention Shoes Using Camera-Based Line-Laser Obstacle
Detection System.pdf](https://github.com/himanshujindal20/Haptic-Footwear/files/9151532/8264071.1.pdf)

<p align = "center">
  <img src="https://user-images.githubusercontent.com/97837018/180020749-19d43cc5-2351-4a79-a8c3-2035b981cb16.png" width="600" height="500" />
</p>


--> **Learnt about and used various APIs provided by Google for navigation purposes:** To perform navigation, we used the inbuilt directions API provided by Google. We give the current location and the destination as inputs to the code, using which we recieve the latitudes and longitudes of interest (i.e the turning points). With this list of latitudes and longitudes, and the current location of the user: we can accordingly provide the directions to the user. This was done via a Web Application coded in JavaScript.

--> **Learnt soldering, to connect all the various components mentioned above**

<p align = "center">
  <img src="https://user-images.githubusercontent.com/97837018/180019816-24ca0b36-7d8f-4ba4-b8ef-7ae6db967092.png" width="450" height="400" />
    <img src="https://user-images.githubusercontent.com/97837018/180019875-91630966-2ecf-452e-ba8f-8f854552520e.png" width="450" height="400" />
</p>






