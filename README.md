# fra

The goal of Francy is to convert photos of book pages into text files as Word, Txt and Pdf. \
The following [video](https://www.youtube.com/watch?v=hNaIh87OFi4) explains the project. \
The software is tested on **Nvidia Jetson Nano** and **Raspberry Pi 3 Model B**.
## Setup
Install docker on your device.
To Install Samba on your device following the instructions on [link](https://ubuntu.com/tutorials/install-and-configure-samba#1-overview).
Copy the following code in your *smb.conf* file:
``` Samba
[FRA]
  workgroup=WORKGROUP
  comment = Photos
  browseable = yes
  read only = no
  guest ok = no
  path = PHOTOS_PATH
```
## Run Software
To install the docker files use:
``` Shell
cd tmp
docker build -t ait_base:latest .
cd ..
docker compose build ait
docker compose up ait
```


