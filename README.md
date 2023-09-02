# CSCI-5410-Serverless-Data-Processing

## Assignments and Topics

1. **[Assignment 1](https://github.com/VikramVenkatapathi/CSCI-5410-Serverless-Data-Processing/tree/main/A1):**
   - **PART A - Provide a summary**:
      - **Thorough Paper Review**: Meticulously examined the paper titled "Mitigating Cold Start Problem in Serverless Computing: A Reinforcement Learning Approach" by P. Vahidinia, B. Farahani, and F. S. Aliee".Focused on understanding the authors' two-layer approach to reducing cold start delays in serverless computing.
      - **Identified Key Issue**: Pinpointed the primary issue addressed in the paper. The paper's main focus is optimizing serverless performance while minimizing memory waste, aiming to overcome the challenges posed by cold start delays.
      - **Detailed Experiment Analysis**: Conducted a comprehensive analysis of the experiments conducted by the authors. The evaluation involved the use of an I/O bound function, and the findings demonstrated the effectiveness of the authors' approach in mitigating cold start issues and improving resource utilization.
   - **PART B - AWS S3 experiment**:
      - **Implemented AWS S3 Bucket Creation**: Successfully implemented Java code to programmatically create an AWS S3 bucket.
      - **Handled Errors Effectively**: Implemented error handling mechanisms to efficiently manage situations where the specified bucket name already exists, ensuring uninterrupted execution.
      - **Developed File Upload Functionality**: Developed a method to seamlessly upload the 'index.html' file into the S3 bucket, enabling smooth integration between local files and cloud storage.
      - **Ensured Secure AWS Access**: Utilized the ProfileCredentialsProvider to guarantee secure access to AWS services by effectively managing AWS Access Key ID and Secret Access Key.
      - **Thoroughly Documented Codebase**: Meticulously documented the codebase and provided references to official AWS SDK documentation, enhancing overall codebase clarity and transparency.
      - **Enabled Static Website Hosting**: Configured static website hosting for an AWS S3 bucket by enabling it, specifying the index file, and saving the changes.
      - **Adjusted Permissions**: Modified bucket permissions to allow public read access by editing the bucket policy and disabling "Block all public access."
      - **Confirmed Website Availability**: Successfully accessed and viewed the 'index.html' file on the website endpoint after making the necessary configurations, ensuring proper setup.
      - **Gained Valuable Experience**: This assignment equipped me with valuable hands-on experience in AWS S3 and Java programming, establishing a robust foundation in serverless computing and cloud storage services.
   - **Keywords: AWS S3, Serverless Computing, AWS SDK for Java, Reinforcement Learning, Long Short-Term Memory (LSTM), GitLab, Maven, HTML, Cold Start Problem, Resource Utilization, Access Control, and Cloud Computing**

2. **[Assignment 2](https://github.com/VikramVenkatapathi/CSCI-5410-Serverless-Data-Processing/tree/main/A2):**
   -  **PART A - Provide a summary**:
      - **Thorough Paper Review**: In-depth analysis and review of the paper titled "Performance Evaluation of Distributed Systems in Multiple Clouds using Docker Swarm" authored by N. Naik. The review aimed to comprehend the paper's content, particularly its exploration of Docker Swarm-based distributed systems in multi-cloud environments.
      -  **Identified Key Issue**: The primary issue addressed in the paper is the efficient design and performance evaluation of distributed systems across multiple cloud platforms. It emphasizes the challenges of provisioning, configuration management, load balancing, and migration in such multi-cloud setups.
      -  **Detailed Experiment Analysis**: Extensive examination of the experiments carried out in the paper. The experiments involved setting up a test environment with multiple cloud providers, deploying a distributed application using Docker Swarm, and evaluating various performance metrics. These experiments validated the effectiveness of the proposed framework in terms of resource utilization, fault tolerance, and scalability.
   -  **PART B - Containerized Application Deployment using GCP**:
      - **Efficient AWS S3 Bucket Creation**: Successfully created an AWS S3 bucket programmatically while effectively handling existing bucket name errors.
      - **Streamlined File Upload**: Developed a seamless file upload mechanism for 'index.html' into the S3 bucket, ensuring smooth local-to-cloud integration.
      - **Secure AWS Access Management**: Ensured secure AWS access using ProfileCredentialsProvider for managing Access Key ID and Secret Access Key.
      - **Documentation and Transparency**: Thoroughly documented the codebase, referencing official AWS SDK documentation for code clarity and transparency.
      - **Static Website Hosting**: Configured static website hosting for the S3 bucket, adjusting permissions to enable public read access and confirming website availability, gaining valuable AWS and Java programming experience. 
   - **Keywords: GCP, Containerized Application, Firestore, Microservices, Docker Images, Artifact Registry, Cloud Run, AWS Lex, Chatbot, Intents, Slots, Fulfillment Logic, Self-Drive, Taxi Service, User Interaction.**

3. **[Assignment 3](https://github.com/VikramVenkatapathi/CSCI-5410-Serverless-Data-Processing/tree/main/A3):**
   - **PART A - Explore & Build a Use Case**:
      - **Scenario**: Utilizing AWS Kinesis, we transform inventory management at Atlantic Superstore, enhancing accuracy and customer satisfaction
      - **Use Case**: Real-time data from IoT devices and POS systems is streamed through Kinesis, enabling demand forecasting, automated reordering, and sentiment analysis via AWS services.
      - **Architecture**: The system includes IoT Core, Kinesis Data Streams, Analytics, Lambda, Comprehend, DynamoDB, and QuickSight, ensuring real-time insights.
      - **Benefits**: Precise inventory control minimizes wastage, stockouts, and manual efforts, leading to improved customer satisfaction and operational efficiency.
      - **AWS Services**: AWS Kinesis, IoT Core, Lambda, Comprehend, DynamoDB, and QuickSight power this innovative solution. 
   - **PART B - Event-driven serverless application using AWS Lambda**:
      - Bucket Creation: Created S3 buckets (SampleDataB00936916 and TagsB00936916) for data storage.
      - Lambda Functions: Implemented two Lambda functions, "extractFeatures" and "accessDB," for data processing and database updates.
      - DynamoDB Integration: Utilized DynamoDB to store named entities and their frequencies.
      - Event Trigger: Configured S3 event notifications to trigger Lambda functions upon file uploads.
      - Data Processing: Extracted named entities from uploaded files, generated JSON data, and updated DynamoDB records accordingly.
      - Serverless Framework: Utilized [Serverless Framework](https://www.serverless.com/) to deploy and manage AWS resources and Lambda functions for this project. 
   - **PART C - Use AWS Lambda-SQS-SNS**:
      - **Designed AWS Architecture**: Created an AWS architecture using Lambda, SQS, and SNS services to simulate an online car delivery service for HalifaxTaxi.
      - **Role and Resource Setup**: Established IAM roles with necessary permissions, and utilized the Serverless Framework to configure resources and deploy Lambda functions.
      - **Lambda Functions**: Developed two Lambda functions, one to generate random car order details and publish them to an SNS topic, and another to consume messages from an SQS queue and send order details via email using SNS.
      - **Event Triggering**: Employed CloudWatch Events Rules to trigger the Lambda function periodically every 2 minutes, and ensured proper message flow between SNS topics and SQS queues.
      - **Testing and Validation**: Conducted testing to verify message generation, publication, consumption, and email notification functionalities, ensuring a robust and functional online car delivery system. 
   - **Keywords: AWS Lambda, S3, DynamoDB, Serverless Framework, SNS, SQS, IAM Role, Event-Driven, CloudWatch, Amazon RDS.**
