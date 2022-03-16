# ls-tf-ga-test

## Setup environment
```
python3 -m venv ./venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Start LocalStack and setup resources necessary resources for local testing
Starting LocalStack
```
localstack start -d
localstack status services
```

### Basic S3 cp example
#### Setup Terraform
Setup the AWS provider
[provider.tf](./terraform/provider.tf)

Add some resources to Terraform config
[main.tf](./terraform/main.tf)

Run Terraform
```
terraform init
terraform apply
```

#### Add a test resource
```
awslocal s3 ls
awslocal s3 ls my-bucket
awslocal s3 cp ../README.md s3://my-bucket/
awslocal s3 ls my-bucket
```

Remove an object from S3
```
awslocal s3api delete-object --bucket my-bucket --key file.txt
```

#### Run unittest
```
cd python/
python3 -m unittest
awslocal s3 ls my-bucket
```

## Resources
https://docs.localstack.cloud/ci/
https://hands-on.cloud/testing-python-aws-applications-using-localstack/
