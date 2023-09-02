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
      - **Configured Environment**: Prepared Docker images for backend and front-end components, ensuring access to Firestore using Google Cloud service account keys.
      - **Artifact Repository Setup**: Created separate repositories for each container image in Artifact Registry and pushed the images to their respective repositories.
      - **Cloud Run Deployment**: Deployed container images as services on Google Cloud Run, configuring appropriate ports and settings.
      - **User Registration and Authentication**: Implemented user registration and authentication logic in Container-1 and Container-2, respectively, securely storing user data in Firestore collections.
      - **Session Management**: Container-3 managed user sessions, updated user state (online/offline) in the Firestore database, and provided real-time information on online users.  
   -  **PART C - Building a Chatbot: Using AWS Lex**:
      - **Create Chatbot**: Utilized AWS Lex to build a chatbot for a Taxi and Car rental service, designing it to handle user requests for both taxi rides and self-drive rentals.
      - **Intents and Sample Utterances**: Defined two intents, "TaxiRequest" and "SelfDriveRequest," with appropriate sample utterances to capture user requests accurately.
      - **Slot Configuration**: Set up slots to gather essential information from users, such as pickup address, pickup date, pickup time, vehicle type, and the number of vehicles. Configured prompts for each slot to guide user input.
      - **Confirmation Prompts**: Implemented confirmation prompts with variable placeholders to confirm user requests, ensuring accuracy before proceeding.
      - **Fulfillment Logic**: Established fulfillment logic for both intents, providing success and failure messages to acknowledge user requests and handle potential issues.  
   - **Keywords: GCP, Containerized Application, Firestore, Microservices, Docker Images, Artifact Registry, Cloud Run, AWS Lex, Chatbot, Intents, Slots, Fulfillment Logic, Self-Drive, Taxi Service, User Interaction.**

3. **[Assignment 3](https://github.com/VikramVenkatapathi/CSCI-5410-Serverless-Data-Processing/tree/main/A3):**
   - **PART A - Provide a summary**:
   - **PART B - **:
   - **PART C - **:
   - **Keywords: **
