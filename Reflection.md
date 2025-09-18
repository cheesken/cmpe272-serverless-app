# What I learnt

## General Learning:
### AWS Lambda
AWS Lambda is a serverless compute service that runs code without managing servers (Nn OS to manage, automatic scaling, no capacity planning, no maintenance & pay per execution). Its like a  function that wakes up only when triggered, does its job, then go back to sleep.

### DynamoDB
Amazon's NoSQL database service ie there is no schema needed (fields of a db, etc). It's fast, scalable, and fully managed. Unlike traditional SQL databases, it stores data in key-value pairs and is perfect for applications that need quick data access.

### API Gateway
It is the front door for the application. It receives HTTP requests from clients (web browsers, mobile apps) and routes them to Lambda functions. It handles things like authentication, rate limiting, and request/response transformation.

### How they work together
Client → API Gateway → Lambda Function → DynamoDB

## Challenges faced:
1. I spent significant time searching for how to add Permissions to Lambda. A lot of the videoes I was watching were outdated. 
2. I learnt how to use API Gateway and Lambda and DynamoDB to make this serverless application. It also made me realise how easy it is to make applications if you have unlimited money because Amazon takes care of most of the maintenance work. I worked with NoSQL Databease which meant I could introduce as many fields as I wanted whenever which is so useful and makes things so easy.

## Screeshots Explained

### 1.png
POST request successful.

### 2.png
DynamoDB Table with the newly created entries

### 3.png
GET failed due to student_id being absent in the query

### 4.png
GET successful for student_id = 456

### 5.png
PATCH request for updating an entry that is already present. 

### 6.png
The result of the previous update (5.png)

### 7.png
DELETE successful for student_id = 1998

### 8.png
Further proof of delete being successful since GET failed due to no record being present for studen_id = 1998