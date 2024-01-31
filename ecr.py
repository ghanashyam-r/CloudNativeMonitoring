
import boto3  # AWS resources in the cloud

# Create an ECR client
ecr_client = boto3.client('ecr')

repository_name = 'my-repocloudnative'
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']

print(repository_uri)
