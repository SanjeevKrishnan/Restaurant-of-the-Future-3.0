# Restaurant of the Future(ROTF) 
## Mechanical Stack: AI & Robotics
<p align="center">
<img src="https://github.com/vanshgoyal/rotf-mechanical/blob/main/Assets/full_body.PNG" width="400" height="600">
</p>

We have designed an autnomous restaurant service bot, which can perform various functions including handling of plates, waste cleaning and segregation, taking orders from costumers etc. 
Our Bot has 4 main components-

      1. Omni Chassis
      2. Plate Handling Mechanism
      3. Vacuum Cleaning Mechanism
      4. Dirt Cleaner

## Omni Chassis - 
<p align="center">
<img src="https://github.com/vanshgoyal/rotf-mechanical/blob/main/Assets/Capture3.PNG" width="400" height="400">
</p>

It is a three wheel omni drive that can easily move in any direction at a given instant. Wheels are attached to the base of omni chassis along with two rotatory encoders for providing feedback to the bot.


## Plate Handling Mechanism - 
<p float="center">
  <img src="https://github.com/vanshgoyal/rotf-mechanical/blob/main/Assets/PH1.PNG" width="400" height="250" />
  <img src="https://github.com/vanshgoyal/rotf-mechanical/blob/main/Assets/PH2.PNG" width="400" height="250" /> 
</p>

Our bot can store 3 food trays at a time. With our plate handling mechanism we can lift the plaltes from their position and place them on the table one by one. It consists of a rack and pinion mechanism for forward movement of the plate and a lead screw mechanism for upward and downward movement. It also contains spring tensed holders which can change their orientation when in need.

## Vacuum Cleaning Mechanism
<p align="center">
<img src="https://github.com/vanshgoyal/rotf-mechanical/blob/main/Assets/vaccum.PNG" width="700" height="400">
</p>

Our bot can segregate different kinds of waste using a ML model and we have constituted two vacuum systems to store the waste separately. Vaccum assembly consists of a fan box that will suck air from front and pass it at the back, along with dirt and waste collection box with a vacuum tube fitted at the front for waste collection.

## Dirt Cleaner
<p align="center">
<img src="https://github.com/vanshgoyal/rotf-mechanical/blob/main/Assets/Dirt%20Cleaner.PNG" width="400" height="400">
</p>

Attached at the bottom of the bot this will revolve around its central axis and clean any dirt present on the floor while moving from one location to another.

## Video Explaination

This is the [link](https://drive.google.com/file/d/1RxF6zCxJ6-5i-8JuhSSGZx6DGByoQ6nk/view?resourcekey) for video explaination of our product. Due to time constraint some parts of our are not shown in this video but can be seen in readme and CAD files

### Software Stack: AI & Robotics
To assist the Hospitality & Service Sector in the COVID-19 Era, our team has proposed an Autonomous Bot that'll aid the restaurant personnel with their repetitive work. Our bot is equipped with LiDAR and Depth Cameras for navigation and obstacle-avoidance, powered by multiple micro-processors to drive the 3-wheeled Omni Drive around the restaurant. The bot is also capable of proper waste segregation and management using the latest AI tech. NLP based Chatbot acting as a User Interface backed with a scalable 3 Microservice Architecture at the backend and robust algorithms for navigation and task scheduling will provide the most comfortable and realistic experience for all the customers. 

This repo contains the source code for the different functionalities of our bot. Each folder contains a README.md file describing the tech stack, along with a proper explanation of the file structure and execution steps wherever needed.

The Cost Structure along with a brief explanation of each functionality can be found in our [Idea Phase Submission](https://docs.google.com/presentation/d/1P2Q0Wq7WKdGj4YcQsi9dySMYV8T4TuGq2-vklr7Ctko/edit#slide=id.gd60f7bbaa3_4_8). 
# Control Scripts
LiDAR based [SLAM](https://github.com/theobscuredev/rotf-software/blob/main/control/mapping.m) is used for reactive control following the [G-Mapping](https://openslam-org.github.io/gmapping.html) Strategy.
[Extended Kalman Filter](https://github.com/theobscuredev/rotf-software/blob/main/control/ekf.m) is used to linearize the position and velocity estimates. A [teleop](https://github.com/theobscuredev/rotf-software/blob/main/control/teleop.m) i.e keyboard enabled input method is also provided for manual control.
Combining all these features, the actual [control](https://github.com/theobscuredev/rotf-software/blob/main/control/wapoint_path.m) occurs while tracing the path predicted by PSO.
