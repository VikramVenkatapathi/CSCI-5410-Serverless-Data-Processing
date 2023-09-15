    Name        : Vikram Venkatapathi
    Banner ID   : B00936916
    Assignment documentation for Term_2 : CSCI 5410 Serverless Data Processing(Summer'23)

## Assignment 2
   -  ### PART A - Provide a summary:
      - **Thorough Paper Review**: In-depth analysis and review of the paper titled ["Performance Evaluation of Distributed Systems in Multiple Clouds using Docker Swarm"](https://ieeexplore.ieee.org/abstract/document/9447123) authored by N. Naik. The review aimed to comprehend the paper's content, particularly its exploration of Docker Swarm-based distributed systems in multi-cloud environments.
      -  **Identified Key Issue**: The primary issue addressed in the paper is the efficient design and performance evaluation of distributed systems across multiple cloud platforms. It emphasizes the challenges of provisioning, configuration management, load balancing, and migration in such multi-cloud setups.
      -  **Detailed Experiment Analysis**: Extensive examination of the experiments carried out in the paper. The experiments involved setting up a test environment with multiple cloud providers, deploying a distributed application using Docker Swarm, and evaluating various performance metrics. These experiments validated the effectiveness of the proposed framework in terms of resource utilization, fault tolerance, and scalability.
   -  ### PART B - Containerized Application Deployment using GCP:
        
          Keywords: GCP, Containerized Application, Firestore, Microservices, Docker Images, Artifact Registry, Cloud Run
      - **Configured Environment**: Prepared Docker images for backend and front-end components, ensuring access to Firestore using Google Cloud service account keys.
      - **Artifact Repository Setup**: Created separate repositories for each container image in Artifact Registry and pushed the images to their respective repositories.
      - **Cloud Run Deployment**: Deployed container images as services on Google Cloud Run, configuring appropriate ports and settings.
      - **User Registration and Authentication**: Implemented user registration and authentication logic in Container-1 and Container-2, respectively, securely storing user data in Firestore collections.
      - **Session Management**: Container-3 managed user sessions, updated user state (online/offline) in the Firestore database, and provided real-time information on online users.
      - #### Architecture
      ![Architecture](https://github.com/VikramVenkatapathi/CSCI-5410-Serverless-Data-Processing/blob/main/A2/Part%20B/Screenshots/Flowchart.png)
   - **PART C - Building a Chatbot: Using AWS Lex**:
      - **Create Chatbot**: Utilized AWS Lex to build a chatbot for a Taxi and Car rental service, designing it to handle user requests for both taxi rides and self-drive rentals.
      - **Intents and Sample Utterances**: Defined two intents, "TaxiRequest" and "SelfDriveRequest," with appropriate sample utterances to capture user requests accurately.
      - **Slot Configuration**: Set up slots to gather essential information from users, such as pickup address, pickup date, pickup time, vehicle type, and the number of vehicles. Configured prompts for each slot to guide user input.
      - **Confirmation Prompts**: Implemented confirmation prompts with variable placeholders to confirm user requests, ensuring accuracy before proceeding.
      - **Fulfillment Logic**: Established fulfillment logic for both intents, providing success and failure messages to acknowledge user requests and handle potential issues.

            Keywords: AWS Lex, Chatbot, Intents, Slots, Fulfillment Logic, Self-Drive, Taxi Service, User Interaction  
   
