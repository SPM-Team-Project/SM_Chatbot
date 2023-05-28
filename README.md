
# SE 403 01 Software Project Management

    Instructor: Ensar GÜL
________________________________________________________________________________

# Name of project:

    Shop Chatbot 

________________________________________________________________________________

# Project Team Members :

•	Mohamed Amin Hejazi - 190706806 (Project Scrum Master)

•	Musa Alaboud – 190706822

•	ibrahim alroubh – 190706815

•	Abdulhamid Barakat – 190706817

•	Meaad Farag Bayuosef - 190706821

________________________________________________________________________________

# About the project:

# project subject and aim of the project:

We have chosen to develop a chatbot dedicated to help manage an online store that sells its products (store to selling bags and shoes) and we aim to help the store to record user information, display products, register invoices, interact with customers by responding to them and perform some services for them. 
our project will generally be able to help the store To carry out many functions and facilitate the management of the store. 

________________________________________________________________________________

# Framework and background development language and tools used :

•	we choose flask as a framework since flask is best for small apps that could get big quickly.

•	We decide to choosing python for backend development, Having many advantages from the ease of learning to a large number of frameworks that simplify the development process, Python is often used for backend web application development. In addition, Python is well-equipped to work with analytics, calculations, AI and ML, and statistics.

•	We use sendPulse as a tool to interact with the store's messenger, SendPulse is a versatile marketing automation tool that combines multiple communication channels to help businesses engage with their audience and streamline their marketing campaigns. and offers a chatbot builder that enables you to create AI-powered chatbots for your website or messenger platforms. You can design interactive chat flows, set up automated responses, and provide personalized customer support using chatbots.

•	Mysql PHP admin used for the database of the program

•	As a team we used trello to arrange our tasks for evry iteration.

•	Our team work together on project files and cod by using github.

_______________________________________________________________________________

# Functionality of the project (Requirements):

Since this project was developed by using scrum method 
the software's features was being available incrementally.

a) the functions available at the beginning of the project:

•	The software have access to specific information in account databases, enabling it to provide customers with information    they need to know, such as product availability, price, etc. 

•	The program able to record user data.

b) functions added during the development:

•	The program able to generate invoices.

•	The software able to send products to customers.

•	The program able to responding and interacting with clients.

•	It can automatically execute a specific set of orders based on customer requests.

________________________________________________________________________________

# Missing parts:
Our team was planning to add an interactive chatbot feature, not only to the store's chat, but we also wanted to add an interactive chatbot to the store's Instagram account, but it was agreed not to include this feature, because the tool used to create the interactive chatbot can't work on more than one platform at the same time, so currently this feature has been canceled, but we may think about adding it if we need development in the future and we find appropriate tool to add it.
________________________________________________________________________________

# Schemas and design documents relevant to project:

Database ERD 

Database Schema with arrows

Use case diagram  

Activity diagram

*all upload on this repository


________________________________________________________________________________

# Deployment:
As for running the software, we uploaded the data on Render.com , after we upload the data on the site, connect it and put the sql code, we upload the Python code to get hub and render will be taking the code from github, and from Render we do a deploy the software with the String Connection in the environment , then the Flask code It will work as an api, and this is how we have uploaded the data and flask code and networked them together. The chat bot is requesting an api request as a Jason file and it is receiving and sending a Jason file.

________________________________________________________________________________

# The tasks and responsibilities for each iteration:

# Link for our tasks board on Trello:
https://trello.com/invite/b/7hO1F9dJ/ATTI7e5e87dd3896725abbe8cdbbaaf0a778A55B6321/shopchatbot

________________________________________________________________________________


# Risks and challenges encountered during development and how they were resolved:

•	One of the problems that our team faced during the development was related to flask struct since we are making a special api for a specific project, so flask strict is not one thing and then we had to do a restruct several times until the problem was solved.


•	Another problem that we encountered during the development of the project was about the modules. Since initially we put each class separately from the other, the code gave us an error warning but the problem was solved when we re-created the modules together.


•	We also went through problem while uploading the project to the online server due to problems related to render, so we added several classes that solved the problem.


•	One of the most important challenges our team faced while developing the project was that we decided to use Mobile Monkey as an facebook chatbot But when we started working on it, we found that its ability to analyze messages was weak, and the most important thing is that they stopped the communication service between MobileMonkey and any other site via api, which forced us to search for another tool suitable for our project and this was available in the sendPulse tool that we used.


 
•	Another challenge we faced was about how to connect the database to Flask, but after lengthy research and trying many solutions, we succeeded in making the connection by adding the Flask alchemy library to the code and making a config for the database address.


•	Also, identifying the right task for the right person while managing the project team was a real challenge It was exceeded by increasing the team's communication with the leader, which led to the leader understanding the way each member of the team works and assigning him the appropriate task.


•	Also, using traditional research methods while working on the project to find solutions was useless and a waste of time with no return. Learning new research methods accelerated work on the project and solved the problems that we faced as a team.

________________________________________________________________________________

# Software Testes:
Several programs have been tried to test programs, but what worked perfectly is the manual test, because there are some tools that did not work properly. We used the unittest library in Python, which worked correctly for flask testing. Also, the Framework Flask Testing were used.

________________________________________________________________________________

# Experience gained:

# a) experience gained as a group:


•	Collaboration and Teamwork: Working in a development group provides ample opportunities to collaborate with other team members. You learn how to communicate effectively, share ideas, and work together towards a common goal. Collaboration helps improve problem-solving skills and fosters a supportive and productive work environment.


•	Agile Methodologies: Many software development groups adopt agile methodologies such as Scrum or Kanban. These methodologies focus on iterative development, regular feedback, and continuous improvement. Through working in an agile environment, you gain experience in sprint planning, daily stand-ups, backlog grooming, and retrospectives, which enhances your ability to deliver high-quality software in a structured and efficient manner.


•	Version Control and Collaboration Tools: Version control systems like Git and collaboration tools like JIRA and Confluence are integral to software development groups. Through their usage, you gain experience in managing code repositories, branching, merging, issue tracking, and knowledge sharing. These tools enhance team productivity and ensure smooth collaboration.


•	Problem Solving and Troubleshooting: Software development often involves solving complex problems and debugging issues. Being part of a development group exposes you to various challenges that require critical thinking and analytical skills. You learn how to identify and resolve bugs, optimize code performance, and address technical issues effectively. 


•	Quality Assurance and Testing: Software development groups emphasize the importance of quality assurance and testing. You gain experience in writing and executing test cases, performing unit tests, integration tests, and user acceptance tests. This experience helps you deliver software with fewer defects and ensures its reliability and robustness.


•	Learning and Adaptability: The software development landscape is constantly evolving, with new technologies and frameworks emerging regularly. Being part of a development group requires continuous learning and adaptability. You gain experience in staying up-to-date with industry trends, exploring new technologies, and acquiring new skills to remain competitive in the field.


•	Project Management: In a software development group, you may have opportunities to take on project management responsibilities, such as leading a development team, managing timelines and resources, and coordinating with stakeholders. This experience enhances your organizational and leadership skills, preparing you for future roles with more significant responsibilities.


•	Overall, being part of a software development group offers valuable experiences that encompass technical skills, collaboration, problem-solving, and project management. These experiences contribute to your professional growth and make you a well-rounded software developer. 



# b) experience gained as individuals:

•	Mohamed Amin Hejazi (Project Scrum Master):

I learned from this project several things, one of which is how to upload the project to a public API and test it, how to upload the database to a public API and try it, and also how to deal with the API in general, and I learned a general idea about Flask alchemy which is generally considered a database manager, also my skill increased In the research, and as I'm the Project Scrum Master of my group I learned how to make a plan for the team, manage it, distribute tasks, and follow up on the progress of work on the project.


•	Musa Alaboud:

First, I gained a lot of experience in this project, most notably dealing with different environments and how to link them. I also tested that there are problems that may occur because there are programs that are not compatible with other programs, and it will be useful if having a general background about the various environments and whether they are compatible with each other or not. I also learned how to do a project test and find defects in the program to fix them.


•	ibrahim alroubh: 

I gained value experiences one of them how to work with a group on the same code easily and without problems by using git and github. I also learned to use a new tool for data base which is pgadmin. I also learned how to upload the project and upload the data base separately, and then link them, which enabled us to use the API and this was my first time that I have uploaded a project to the Internet and tested it.



•	Abdulhamid Barakat: 

  By doing this project, I learned many experiences, the most important  that I learned to deal with chatbots, which was a new and useful experience for me. I learned how to train chatbots and how to make it as realistic as possible, and working on Flask and databases increased my knowledge and skills about them. 


•	Meaad Farag Bayuosef: 

First of all being a part of a software development team allows me to collaborate with others on projects and I learn how to communicate effectively, share ideas, and work together to achieve common goals.
Secondly, I increased my skills in analyzing and solving problems by helping to find solutions to the problems that our team faced during development and applying these solutions.
I also learned to work with Flask which was a unique addition to my knowledge, and I used the Flask alchemy library for managing database and I learned how to connect Flask with databases by add Flask alchemy library to the code and making a config for the database address. 


________________________________________________________________________________







