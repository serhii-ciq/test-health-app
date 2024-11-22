import boto3

# Replace these with your actual AWS credentials
ACCESS_KEY = "AKIASLQ33UGG26QZFSW5"
SECRET_KEY = "eaM3kjbrbrWCBXXiwVivGcQMBP+4M4kLXfssbYGJ"

def list_s3_buckets(access_key, secret_key):
    # Create an S3 client using the provided access and secret keys
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )
    
    # Retrieve and print the list of S3 buckets
    response = s3_client.list_buckets()
    buckets = response.get("Buckets", [])
    
    print("S3 Buckets:")
    for bucket in buckets:
        print(f"  - {bucket['Name']}")

# Call the function
list_s3_buckets(ACCESS_KEY, SECRET_KEY)


