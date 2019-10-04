# aws-python
Repository for playing around with Python3 and AWS, with some automation to go along

## 1-webotron
A script to sync a local directory to an s3 bucket, with optional R53 and Cloudfront configuration

### Features

Current Webotron features:

- Select AWS profile with --profile=<profile_name>
- List buckets in an account
- List contents of a bucket
- Create and set up a bucket as a hosted website
- Sync directory tree to bucket
- Configure Route53 domain
- Set up Cloudfront CDN and SSL
