CS 643, Cloud Computing - Programming Assignment 2

Description

Our goal is to develop a wine quality prediction model in Spark over AWS.  In this assignment we have deployed ML model for training and testing of wine quality prediction dataset. There are two phases of this application namely: Training phase and Testing Phase. In the training phase a random forest model is created and trained on given training dataset. Then trained model is saved and loaded into the testing phase to predict and determine efficiency of trained model. Application is deployed into the amazon AWS EC2 instances. Training is done on multiple instances in parallel and testing is performed using single EC2 instance.
How to create Amazon EC2 Instance
To create and deploy model into amazon EC2 instances following steps are performed.
•	Login to Amazon AWS account.
•	Search for EC2 instance by using search console.
•	Press on the EC2 Instance button and then select launch instance button. 
•	After launching the instance, a dialogue will appear to set instance name, number of instances, login details etc.
•	Fill in all the information and press launch button.
•	Click on the launch button to launch the ec2 instances.
•	 From the command line ssh into the ec2 from our local system into the ec2 instance. 
•	Run the command Spark-submit test.py to build the model.
How to deploy Application without docker
To deploy model without docker container following steps are performed.
•	SSH into the EC2 instance.
•	Copy Application files in to EC2 instance by using ‘scp’ command.
•	Run the application by running testmodel.py file.
How to deploy Application within docker
To deploy model within docker container following steps are performed.
•	SSH into the EC2 instance.
•	Install docker into the EC2 instance.
•	Start docker service and run it.
•	After starting the docker build the docker image by using “docker build -t imagename .”
•	When the process is finished run the application using “docker run -p 80:80 imagename . ”


![image](https://user-images.githubusercontent.com/108843070/184054112-617f9fa9-eaab-4447-afff-69dd8b8136e6.png)
