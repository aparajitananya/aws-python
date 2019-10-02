#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Webotron: Deploy websites with aws.

Webotron automates the process of deploying static websites
- Configures AWS S3 buckets
    - Creates them
    - Sets up static website hosting
    - Deploys local files
- Configure DNS with R53
- Configure a CND and SSL with Cloudfront
"""

import boto3
import click

from bucket import BucketManager

session = None
bucket_manager = None

@click.group()                    # decorator
@click.option('--profile', default=None, help="Use an AWS profile.")
def cli(profile):
    """Webotron deploys websites to AWS."""
    global session, bucket_manager

    session_cfg = {}
    if profile:
        session_cfg['profile_name'] = profile
    session = boto3.Session(**session_cfg)
    bucket_manager = BucketManager(session)
    pass


@cli.command('list-buckets')      # now this command falls under our group
def list_buckets():
    "List all buckets."
    for bucket in bucket_manager.all_buckets():
        print(bucket)


@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    """List objects in an S3 bucket."""
    for obj in bucket_manager.all_objects(bucket):
        print(obj)


@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    """Create and configure an S3 bucket."""
    s3_bucket = bucket_manager.init_bucket(bucket)
    bucket_manager.set_policy(s3_bucket)
    bucket_manager.configure_website(s3_bucket)

    return


@cli.command('sync')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucket')
def sync(pathname, bucket):
    """Sync contents of PATHNAME to BUCKET."""
    bucket_manager.sync(pathname, bucket)
    print(bucket_manager.get_bucket_url(bucket_manager.s3.Bucket(bucket)))


if __name__ == '__main__':
    cli()
