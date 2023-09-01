package org.example;

import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
import software.amazon.awssdk.core.exception.SdkException;
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
    // AWS access key ID and secret access key
    static String accessKeyId = "AKIAQ3KTZMQAZETL43FI";
    static String secretAccessKey = "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";

    static String bucketName = "b00936916-a1";

    /**
     * Main method to create S3 client and call necessary functions.
     *
     * @param args Command line arguments
     * @throws URISyntaxException If the resource file URI is invalid
     */
    public static void main(String[] args) throws URISyntaxException {
        // Create AWS credentials using access key ID and secret access key
        AwsBasicCredentials myAwsCredentials = AwsBasicCredentials.create(accessKeyId, secretAccessKey);

        // Specify the AWS region
        Region region = Region.US_EAST_1;

        // Create an S3 client with the provided credentials and region
        S3Client s3Client = S3Client.builder()
                .region(region)
                .credentialsProvider(StaticCredentialsProvider.create(myAwsCredentials))
                .build();

        // Call the method to create an S3 bucket
        createS3Bucket(s3Client);

        // Call the method to upload a file to S3
        uploadFiletoS3(s3Client);
    }

    /**
     * Uploads a file to the specified S3 bucket.
     *
     * @param s3Client The S3 client
     * @throws URISyntaxException If the resource file URI is invalid
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
}
