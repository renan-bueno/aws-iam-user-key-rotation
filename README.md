# AWS Lambda Access Key Rotation Automation

This project automates the rotation of AWS IAM user access keys using AWS Lambda and EventBridge. The Lambda function is triggered every 80 days by an EventBridge scheduler to manage the access keys based on specific conditions.

## Table of Contents

- [Features](#features)
- [Pre-requisites](#pre-requisites)
- [Parameters](#parameters)
- [Installation](#installation)
- [Usage](#usage)
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

## Contributing

Feel free to submit pull requests or report issues to improve the project.

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.
