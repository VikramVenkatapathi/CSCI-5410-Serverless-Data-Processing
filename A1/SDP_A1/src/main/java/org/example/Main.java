package org.example;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.core.sync.RequestBody;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.CreateBucketRequest;
import software.amazon.awssdk.services.s3.model.CreateBucketResponse;
import software.amazon.awssdk.services.s3.model.PutObjectRequest;
import software.amazon.awssdk.services.s3.model.S3Exception;

import java.io.File;
import java.net.URISyntaxException;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Main {
    private static String bucketName = "b00936916-a1";
    private static String region = "us-east-1";

    /**
     * Main method to create an S3 bucket and upload a file to it.
     *
     * @param args Command-line arguments
     * @throws URISyntaxException If the file path is not a valid URI
     */
    public static void main(String[] args) throws URISyntaxException {
        // Create the credentials provider
        //Retrieve the AWS Access Key ID & AWS Secret Access Key from ./aws/credentials file
        ProfileCredentialsProvider credentialsProvider = ProfileCredentialsProvider.create();

        // Create the S3 client
        S3Client s3Client = S3Client.builder()
                .region(Region.of(region))
                .credentialsProvider(credentialsProvider)
                .build();

        // Call the method to create an S3 bucket
        createS3Bucket(s3Client);

        // Call the method to upload a file to S3
        uploadFiletoS3(s3Client);
    }

    /**
     * Creates an S3 bucket with the specified bucket name.
     *
     * @param s3Client The S3 client
     */
    private static void createS3Bucket(S3Client s3Client) {
        try {
            // Create a request to create an S3 bucket with the specified bucket name
            CreateBucketRequest createBucketRequest = CreateBucketRequest.builder()
                    .bucket(bucketName)
                    .build();

            // Send the create bucket request to the S3 service
            CreateBucketResponse createBucketResponse = s3Client.createBucket(createBucketRequest);
        } catch (S3Exception e) {
            if (e.awsErrorDetails().errorCode().equals("BucketAlreadyExists")) {
                System.err.print("Failed to create bucket. Bucket name already exists");
            }
        }
    }

    /**
     * Uploads a file to the S3 bucket.
     *
     * @param s3Client The S3 client
     * @throws URISyntaxException If the file path is not a valid URI
     */
    private static void uploadFiletoS3(S3Client s3Client) throws URISyntaxException {
        // Obtain the file name and path
        String fileName = "index.html";
        Path resourcePath = Paths.get(Main.class.getClassLoader().getResource(fileName).toURI());
        String filePath = resourcePath.toString();

        // Create a request to put the object in the S3 bucket
        PutObjectRequest putObjectRequest = PutObjectRequest.builder()
                .bucket(bucketName)
                .key(filePath)
                .build();

        // Upload the file to S3
        s3Client.putObject(putObjectRequest, RequestBody.fromFile(new File(filePath)));
    }
}

/** References : 
* Code snippets were referred from official AWS SDK documentation:

@see <a href="https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-s3-buckets.html ">Create S3 bucket</a>
@see <a href="https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-s3-objects.html">PUT object in S3 bucket</a>
*/
