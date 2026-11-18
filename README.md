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

### Experiment 6 – Familiarization and Usage of Cloud Services Using AWS and Open-Source Cloud Tools

- Updated Ubuntu Linux and installed basic utilities using the terminal.
- Created a private Amazon S3 bucket with public access blocked and default encryption enabled.
- Uploaded, downloaded, verified, and deleted a sample file using the AWS Management Console.
- Explored AWS IAM roles, policies, users, and root access management.
- Explored Amazon EC2 instance configuration without launching an instance.
- Explored Amazon VPC components, including subnets, route tables, internet gateways, and security groups.
- Explored Amazon CloudWatch metrics and alarms.
- Used AWS CloudShell and AWS CLI to create an S3 bucket, upload, list, download, and verify a file.
- Deleted the test S3 object and bucket to avoid unnecessary resource usage.

**Report:** [Lab_6_Report.pdf](Lab_6_Report.pdf)

### Experiment 7 – Familiarization and Usage of Collaborative Applications (SaaS)

- Studied the Software as a Service (SaaS) cloud service model and its features.
- Created and shared a collaborative document using Google Docs.
- Performed real-time collaborative editing, commenting, and version history operations.
- Created a spreadsheet using Google Sheets with student records.
- Performed calculations using SUM, AVERAGE, MAX, and MIN functions.
- Shared the spreadsheet and performed collaborative data entry and cell commenting.
- Created a four-slide presentation using Google Slides.
- Shared the presentation and performed collaborative editing and commenting.
- Explored online communication and collaboration platforms, including Google Meet, Microsoft Teams, and Zoom.

**Report:** [Lab_7_Report.pdf](Lab_7_Report.pdf)

### Experiment 8 – Implementing Applications Using a Platform as a Service (PaaS) – Flask Web Application Deployed on a Cloud Platform

- Studied the Platform as a Service (PaaS) cloud computing model.
- Created a project folder named `Cloud-lab8`.
- Developed a simple web application using Python and Flask.
- Created `main.py` and `requirements.txt` for the application.
- Installed Flask and Gunicorn and tested the application locally on port 8080.
- Uploaded the project to GitHub and connected the repository to Render.
- Configured and deployed the Flask application using Render's free web service.
- Accessed the deployed application through its public URL.
- Explored deployment history, application logs, and service settings.
- Modified and redeployed the application through GitHub commits.
- Verified automatic deployment by successfully deploying Application Versions 2 and 3.

**Report:** [Lab_8_Report.pdf](Lab_8_Report.pdf)

### Experiment 9 – Develop MapReduce Application Using Hadoop Cluster Setup

- Installed and configured OpenJDK 17 and Apache Hadoop 3.4.2 on Ubuntu Linux.
- Configured Hadoop environment variables and XML configuration files.
- Set up a single-node pseudo-distributed Hadoop cluster.
- Configured SSH for passwordless localhost communication.
- Formatted the HDFS NameNode and started Hadoop services.
- Verified NameNode, DataNode, SecondaryNameNode, ResourceManager, and NodeManager using `jps`.
- Created directories in HDFS and uploaded sample input data.
- Developed a WordCount application using Java and the Hadoop MapReduce framework.
- Compiled the Java program and created the `wordcount.jar` file.
- Executed the MapReduce job using Hadoop and YARN.
- Verified the successful execution and word frequency output.
- Explored the Hadoop NameNode and ResourceManager web interfaces.
- Examined HDFS file blocks using the `hdfs fsck` command and verified filesystem health.

**Report:** [Lab_9_Report.pdf](Lab_9_Report.pdf)

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
- Amazon Web Services (AWS)
- Amazon S3
- AWS IAM
- Amazon EC2
- Amazon VPC
- Amazon CloudWatch
- AWS CLI
- Software as a Service (SaaS)
- Platform as a Service (PaaS)
- Flask
- Gunicorn
- Render
- Apache Hadoop 3.4.2
- Hadoop Distributed File System (HDFS)
- Hadoop YARN
- MapReduce
- Git & GitHub
- Google Docs, Google Sheets and Google Slides
- Google Meet, Microsoft Teams and Zoom

## Repository Structure

```text
Cloud-Computing-Lab/
│
├── README.md
├── Lab1_Report.pdf
├── Lab2_Report.pdf
├── Lab3_Report.pdf
├── Lab4_SDN_Report.pdf
├── Lab5_Cloud_Scheduling_Report.pdf
├── Lab_6_Report.pdf
├── Lab_7_Report.pdf
├── Lab_8_Report.pdf
├── Lab_9_Report.pdf
│
└── Cloud-lab8/
    ├── main.py
    └── requirements.txt
```
