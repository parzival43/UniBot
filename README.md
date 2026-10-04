# UniBot — Distributed Swarm Robotics

> **What if a robot didn't have to be powerful to be useful?**

UniBot is an experimental platform for building **small, wireless, cooperative robots**.

The core idea: instead of putting every capability into one complex robot, distribute simple capabilities across a **swarm of inexpensive robots** and let them communicate and coordinate.

This project began as an exploration of miniature robotics and has evolved into a platform for experimenting with **distributed robotics, wireless coordination, autonomous docking, and collective behavior**.

**As each robot can independently reorient its drive assemblies, multiple UniBots can potentially reconfigure their collective geometry and movement direction. This creates the possibility of using the same population of robots for different formations and tasks rather than designing a separate robot for each task.**

UniBot is a continuing experiment rather than a finished product.



## V1 Demonstration

[Watch the original V1 demonstration](https://github.com/parzival43/UniBot/blob/master/Photos/Demonstration.mp4?raw=true)

![UniBot prototype](https://raw.githubusercontent.com/parzival43/UniBot/refs/heads/master/Photos/UniBot.jpg)


## About V1 Prototype

The current UniBot prototype demonstrates:

* Wireless communication over Wi-Fi
* two-axis articulated locomotion mechanism
* Python-based control software

The current prototype is extremely simple and stable. It serves as a foundation for experimenting with autonomous collective behavior.

The current prototype is only the first step.

The central question is:

> **How much collective capability can emerge from many extremely simple robots?**


## The Idea

A single small robot has obvious limitations: Specfic functionality, portability, scale, and physical capability.

A group of tiny robots can be different.

If individual robots can communicate and coordinate, the swarm can potentially:

* divide tasks between robots
* adapt when individual robots fail
* form different configurations for different tasks
* share information
* operate using inexpensive hardware
* recharge autonomously and continue operating

**The goal is not to make one tiny robot extremely capable.
The goal is to make many simple robots capable of working together.**



## Hardware

The current prototype is built around:

* ESP8266
* N20 DC motors and AD002 Servos
* WI-FI communication
* Custom miniature mechanical platform

The architecture is intentionally designed around **low-cost and accessible components**, allowing multiple units to be constructed efficiently.


## Software

### Robot

* MicroPython
* ESP8266
* TCP/WebSocket communication

### Control System

* Python
* Socket networking
* Pynput

## Next Steps

The next generation focuses on moving beyond individual control toward **collective autonomy**:

1. Robot-to-robot communication
2. Shared state
3. Autonomous navigation
4. Task allocation
5. Formation/collective movement
6. Autonomous docking
7. Fault-tolerant swarm behavior


## Project Report

For the engineering documentation and development process:

[Read the UniBot Project Report](https://github.com/parzival43/UniBot/blob/master/UniBot%20Project%20Report.pdf)


## Team

**Knight Labs**

* Senthil Arasu J — Team Lead
* Sahithian TR
* Muhammad Fayaazullah F


## Project Status

**Experimental / Research Prototype**

UniBot is an ongoing exploration of miniature distributed robotics. The current implementation demonstrates the basic platform; future versions will focus increasingly on autonomous coordination and collective behavior.
