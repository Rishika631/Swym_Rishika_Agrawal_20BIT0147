# Swym_Rishika_Agrawal_20BIT0147
# Video link: 
https://drive.google.com/file/d/1FJeEKaJZ_r9b4pya05wnQe0jnX51H-v-/view?usp=sharing
## RailTrack: Railway Timetable Analysis and Query System
This is a web application built using Flask and MongoDB to analyze and query Indian Railways train timetable data. The app allows users to perform various queries and obtain insights from the timetable data.

# Features
Trains at Midnight: Lists trains that arrive at a station at midnight.

Halt Statistics: Provides statistics on maximum, minimum, and average halt times for trains.

Trains Between Stations: Determines the number of trains passing between two specified stations in one direction.

# Requirements
-Python 3.x
-Flask
-MongoDB
-pandas

# Installation
 
Clone this repository to your local machine.
 ```ruby
git clone https://github.com/yourusername/railway-timetable-app.git
```
Install the required packages using pip.

 ```ruby
pip install pymongo flask pandas
'''
Populate MongoDB with data and Ensure MongoDB is running.
Update the MongoDB connection string in populate_mongo.py with your credentials.
Run the script to load the data.

 ```ruby
python populate_mongo.py
'''
Run the Flask app.

```ruby
python app.py
'''
Access the app in your browser by running index.html file in swym frontend folder

Usage
Visit the app homepage to explore the available queries.
Perform the desired queries by clicking on the respective links.
View the query results and insights presented in a user-friendly format.

Question asked in the problem statement pdf:
How you would approach this problem if the data volume were 10 times the rows in
this CSV. Would you change your approach in any way?

Handling a data volume that is 10 times larger than the initial CSV presents significant challenges. To address this, we may consider many solutions including changes in technologies. Here are some potential solutions:
1.	Database Technology:
•	Change to a Distributed Database: Consider using databases designed for massive scalability, such as Apache Cassandra or Amazon DynamoDB, which are well-suited for handling large amounts of data across multiple nodes.
•	Big Data Solutions: Explore technologies like Apache Hadoop or Apache Spark for distributed data processing and storage.
2.	Backend Technology:
•	Microservices Architecture: Decompose your backend into microservices, each responsible for specific functionality. This can help with scalability and maintenance.
•	Serverless Architecture: Use serverless computing platforms like AWS Lambda or Azure Functions to automatically scale based on demand.
3.	Message Queues and Asynchronous Processing:
•	Message Brokers: Implement message queues like RabbitMQ or Apache Kafka for managing asynchronous tasks and processing data in a distributed manner.
4.	Frontend Technology:
•	Client-Side Rendering (CSR): Consider using frameworks like React or Angular for client-side rendering, which can improve the user experience and reduce server load.
•	Progressive Web Apps (PWAs): Develop PWAs for efficient caching and offline access to data, enhancing frontend performance.
5.	Infrastructure and Deployment:
•	Containerization: Use Docker for packaging applications and Kubernetes for orchestrating containers, enabling easy scaling and management.
•	Cloud Services: Leverage cloud services like AWS, Google Cloud, or Azure to scale resources up or down based on demand.
6.	Optimized Queries and Indexing:
•	Query Optimization: Review and optimize your database queries for improved performance, and consider using query optimization tools.
•	Indexing Strategies: Utilize advanced indexing techniques provided by your chosen database technology to speed up data retrieval.
7.	Data Partitioning and Sharding:
•	Horizontal Sharding: Implement data partitioning and distribute data across multiple database instances or clusters to balance the load.
