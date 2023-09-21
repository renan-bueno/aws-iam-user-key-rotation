# AWS Lambda Access Key Rotation Automation

This project automates the rotation of AWS IAM user access keys using AWS Lambda and EventBridge. The Lambda function is triggered every 80 days by an EventBridge scheduler to manage the access keys based on specific conditions.

## Table of Contents

- [Features](#features)
- [Pre-requisites](#pre-requisites)
- [Parameters](#parameters)
- [Installation](#installation)
- [Usage](#usage)
- [Custom S3 Bucket](#custom-s3-bucket)
- [Important Note](#important-note)
- [Contributing](#contributing)
- [License](#license)

## Features

The Lambda function operates under the following conditions:

### First Condition
- **Scenario**: 2 Active Access Keys
- **Action**: Deactivate and delete the oldest one, then create a new one.

### Second Condition
- **Scenario**: 2 Deactivated Access Keys
- **Action**: Delete the oldest key and create a new one.

### Third Condition
- **Scenario**: 1 Deactivated and 1 Active Access Key
- **Action**: Delete the deactivated one and create a new access key.

### Fourth Condition
- **Scenario**: 1 Active Access Key
- **Action**: Create a new access key.

### Fifth Condition
- **Scenario**: 1 Deactivated Access Key
- **Action**: Delete the deactivated one and create a new access key.

## Pre-requisites

- An existing IAM user whose keys will be rotated.
- An SNS topic with a confirmed email subscription.

## Parameters

- **IAM User Name**: The name of the IAM user whose keys you want to rotate.
- **SNS Topic Name**: The name of the SNS topic where notifications will be sent.

## Installation

1. Clone this repository.
2. Deploy the CloudFormation template.
3. Confirm the SNS email subscription.

## Usage

1. Update the IAM User Name and SNS Topic Name parameters in the CloudFormation template.
2. Deploy the CloudFormation stack.
3. The Lambda function will automatically be triggered every 80 days to manage the access keys.

## Custom S3 Bucket

The Python code for this Lambda function is fetched from a public S3 bucket. If you wish to use your own bucket:

1. Upload the file `lambda-access-key-rotation-3.zip` to your S3 bucket and make it public.
2. Update the `S3Bucket` and `S3Key` parameters in the CloudFormation template to point to your custom bucket and file.

## Important Note

If you have only one active access key, the Lambda function will create a new access key but won't delete the old one. This is to prevent breaking any applications that might be using the old key. You should manually delete the old key after updating your applications with the new key in an asynchronous manner.

## Contributing

Feel free to submit pull requests or report issues to improve the project.

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.
