## Native RTDE Docker Container
### Getting Started
The purpose of this sample is to run an RTDE client inside of a Docker container, eliminating the need for an external PC. The sample closely follows the "example control loop" referenced in the RTDE guide on the [Universal Robots Support site](https://www.universal-robots.com/articles/ur/interface-communication/real-time-data-exchange-rtde-guide/ "RTDE Guide"). **Note: users must be running Polyscope 6 or higher for this sample to work.**

The repository has two samples: a socket server and an RTDE client. The steps below reference building and running the client but can be modified to instead build the socket server.
### Building the Docker Image
The Docker image can built by running the following command in the root directory:   
`$ docker build -t rtde-native:latest -f simple-socket/Dockerfile-rtde .`   
*Users wanting to build the socket server image can remove the "-rtde" from the Dockerfile*

From there users can save the built image to a TAR file with the following:   
`$ docker save rtde-native:latest -o rtde-native.tar`

### Loading the Docker Image
At this point the TAR file should be present in the current directory. The file must be transferred over to the robot filesystem. This guide will assume the user is utilizing a USB for the transfer, but most methods (like Secure Copy) should work. Insert the USB containing the TAR file into the robot. It would also be a good idea to copy "rtde_control_loop.urp" located in the root of this repository onto the USB as well.

Connect a USB keyboard and open the Linux terminal on the robot by hitting: CTRL-ALT-F1. This should prompt for a username and password. Enter 'root' as the username and 'easybot' as the password. The terminal should look like so:
```
Linux ur-201950XXXXX 5.15.55-rt48-arnold+ #1 SMP PREEMPT Thu Dec 22 11:56:24 UTC 2022 x86_64
Last login: Thu Jan 19 23:28:23 2023
root@ur-201950XXXXX:~#
```

Enter the following command to load the Docker image:   
`# docker load -i /media/urmountpoint_NuRI1a/rtde-native.tar`

Note that the letters and numbers after "urmountpoint_" will most likely be different as those are generated when the USB is inserted. Users can auto-complete to get the USB name by hitting "Tab". 

After a short delay, the image will be loaded and the user should see "Loaded image: rtde-native:latest". The image can be confirmed by typing "docker images". Sample output should look something like this:
```
root@ur-201950XXXXX:~# docker images
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
rtde-native   latest    aec52a04eb34   8 minutes ago   57MB
urservice     4.0.1     a1ba5777070b   2 weeks ago     22.9MB
root@ur-201950XXXXX:~#
```
### Running the Container and Robot Program
At this point the container can be built and run using the following command:  
`# docker run -it rtde-native`   
This will start the container interactively which will prevent further commands.

Alternatively, the container can be run detached which allows continued use of the terminal:   
`# docker run -itd rtde-native`   

Users can run a "docker ps" command to confirm the container is running. Output should look something like this:
```
root@ur-201950XXXXX:~# docker ps
CONTAINER ID   IMAGE             COMMAND                  CREATED          STATUS                 PORTS
   NAMES
d4872950dd74   rtde-native       "python rtdeControlL…"   30 minutes ago   Up 30 minutes
   affectionate_blackburn
7b473c4acbce   urservice:4.0.1   "./urservice"            3 hours ago      Up 3 hours (healthy)   0.0.0.0:8181->8181/tcp   urservice
root@ur-201950XXXXX:~#
```
At this point the robot program "example control loop.urp" can be opened on the robot TeachPendant. Copy it over from the USB or open straight from it. 

__WARNING:__
When hitting play the robot **will begin moving** towards the first setpoint from the sample. Make sure if running on a physical robot that the area is clear and safe.


### Notes and Known Limitations
URService and containers contributed by URCaps are the only ones which will run when the robot starts up. This means the user will need to enter the "Docker run" command on each boot. It is recommended to create a minimal URCap to work around this limitation.
