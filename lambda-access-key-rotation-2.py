import boto3
import os

def lambda_handler(event, context):
    iam_client = boto3.client('iam')
    sns_client = boto3.client('sns')

    # Get parameters from environment variables
    iam_user_name = os.environ.get('IAM_USER_NAME')
    sns_topic_name = os.environ.get('SNS_TOPIC_NAME')
    
    # Extract the AWS account number and region from the Lambda context
    account_id = context.invoked_function_arn.split(":")[4]
    region = context.invoked_function_arn.split(":")[3]
    
    # Get the current access keys for the user
    access_keys = iam_client.list_access_keys(UserName=iam_user_name)['AccessKeyMetadata']
    
    # Sort access keys by creation date
    sorted_keys = sorted(access_keys, key=lambda x: x['CreateDate'])
    
    # Determine the number of active and deactivated keys
    active_keys = [key for key in sorted_keys if key['Status'] == 'Active']
    deactivated_keys = [key for key in sorted_keys if key['Status'] == 'Inactive']

    # Check conditions and take appropriate actions
    if len(active_keys) == 2:
        iam_client.delete_access_key(UserName=iam_user_name, AccessKeyId=sorted_keys[0]['AccessKeyId'])
    elif len(deactivated_keys) == 2:
        iam_client.delete_access_key(UserName=iam_user_name, AccessKeyId=sorted_keys[0]['AccessKeyId'])
    elif len(deactivated_keys) == 1 and len(active_keys) == 1:
        iam_client.delete_access_key(UserName=iam_user_name, AccessKeyId=deactivated_keys[0]['AccessKeyId'])
    elif len(deactivated_keys) == 1:
        iam_client.delete_access_key(UserName=iam_user_name, AccessKeyId=deactivated_keys[0]['AccessKeyId'])

    # Create a new access key
    new_access_key = iam_client.create_access_key(UserName=iam_user_name)['AccessKey']

    # Send SNS notification
    message = (f"The access key for IAM user '{iam_user_name}' in account {account_id} and region {region} has been rotated.\n"
               f"New Access Key ID: {new_access_key['AccessKeyId']}\n"
               f"New Secret Access Key: {new_access_key['SecretAccessKey']}")
    sns_client.publish(
        TopicArn=f'arn:aws:sns:{region}:{account_id}:{sns_topic_name}',
        Message=message,
        Subject='IAM Access Key Rotation Notification'
    )

    return {
        'statusCode': 200,
        'body': message
    }
