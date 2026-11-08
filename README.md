# Cloud Computing Lab

This repository contains the laboratory experiments and reports completed as part of the Cloud Computing course.

## Experiments

### Experiment 1 – Installation of Hypervisor and Virtual Machine

- Installed Oracle VirtualBox as the hypervisor.
- Created and configured an Ubuntu Linux virtual machine.
- Configured CPU, RAM, storage, and network settings.
- Installed Ubuntu using an ISO image.
- Installed the required build tools and Linux kernel headers.
- Verified the working of the virtual machine.

**Report:** [Lab1_Report.pdf](Lab1_Report.pdf)

### Experiment 2 – TCP Client-Server Communication

- Created two Ubuntu virtual machines using VirtualBox.
- Configured an internal network between the virtual machines.
- Assigned static IP addresses.
- Implemented TCP client-server communication using Python socket programming.
- Tested two-way communication between the client and server.

**Report:** [Lab2_Report.pdf](Lab2_Report.pdf)

### Experiment 3 – Creation of a Simple Network Topology Using Open-Source Network Virtualization Tools

- Installed and configured Mininet on Ubuntu Linux.
- Created a `single,3` topology with one switch and three hosts.
- Verified the topology using Mininet networking commands.
- Tested communication using `pingall`.
- Created a `tree,3` topology with eight hosts and seven switches.
- Verified communication between the virtual network nodes.
- Used basic Linux networking commands such as `ifconfig`.
- Cleaned up and stopped the Mininet network after completion.

**Report:** [Lab3_Report.pdf](Lab3_Report.pdf)

### Experiment 4 – Software-Defined Networking (SDN) Using Mininet, Open vSwitch and Ryu Controller

- Installed and configured Mininet and Open vSwitch.
- Installed and configured the Ryu SDN Controller.
- Created a `single,3` topology with three hosts and one switch.
- Connected Mininet to the remote Ryu controller using OpenFlow 1.3.
- Tested network connectivity using `pingall`.
- Inspected OpenFlow flow tables using `ovs-ofctl`.
- Implemented traffic filtering using a high-priority drop rule.
- Removed flow rules and cleaned up the Mininet network.

**Report:** [Lab4_SDN_Report.pdf](Lab4_SDN_Report.pdf)

### Experiment 5 – Implementation of Various Scheduling Mechanisms Using CloudSim Plus

- Set up Java 17, Maven, and Git on Ubuntu.
- Created a Maven project using the CloudSim Plus simulator.
- Simulated a datacenter with one host, two virtual machines, and four cloudlets.
- Implemented and compared four scheduling combinations:
  - VM SpaceShared + Cloudlet SpaceShared.
  - VM SpaceShared + Cloudlet TimeShared.
  - VM TimeShared + Cloudlet SpaceShared.
  - VM TimeShared + Cloudlet TimeShared.
- Successfully compiled and executed all four scheduling scenarios.

**Report:** [Lab5_Cloud_Scheduling_Report.pdf](Lab5_Cloud_Scheduling_Report.pdf)

## Technologies Used

- Oracle VirtualBox
- Ubuntu Linux
- Python
- Java 17
- Apache Maven
- CloudSim Plus
- TCP/IP
- Socket Programming
- Mininet
- Open vSwitch
- Ryu Controller
- OpenFlow 1.3
- Git & GitHub

## Repository Structure

```text
Cloud-Computing-Lab/
│
├── README.md
├── Lab1_Report.pdf
├── Lab2_Report.pdf
├── Lab3_Report.pdf
├── Lab4_SDN_Report.pdf
└── Lab5_Cloud_Scheduling_Report.pdf
```
