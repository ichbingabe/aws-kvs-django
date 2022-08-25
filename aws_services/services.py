import boto3
import botocore.exceptions
from botocore.exceptions import ClientError


class KinesisVideoStream:
    def __init__(self, channel_name):
        self.channel_name = channel_name
        self.kvs_client = boto3.client('kinesisvideo')

    def describe_chanenel(self):
        try :
            response = self.kvs_client.describe_signaling_chanenel(
                ChannelName=self.channel_name
            )
            return response
        except botocore.exceptions.ClientError as err:
            if err.response['Error']['Code'] == 'ResourceNotFoundException':
                return False
            else:
                raise(err)
        except Exception as er:
            raise(er)

    def create_channel(self):
        client = boto3.client('kinesisvideo')
        try:
            client.create_signaling_channel(
            ChannelName=self.channel_name,
            ChannelType='SINGLE_MASTER',
            SingleMasterConfiguration={
                'MessageTtlSeconds': 15
            }
            )
            return True
        except Exception as er:
            raise(er)

    def delete_channel(self):
        response = self.describe_channel(self.channel_name)
        if response == False:
            return False # this channel not exists
        else:
            channel_info = response['ChannelInfo']
            channel_version = channel_info['Version']
            channel_arn = channel_info['ChannelARN']
            
            try:
                self.kvs_client.delete_signaling_channel(
                ChannelARN=channel_arn,
                CurrentVersion=channel_version
                )
                return True # this channel is deleted
            
            except botocore.exceptions.ClientError as error:
                # this channel is current in use
                if error.response['Error']['Code'] == 'ResourceInUseException':
                    pass
                #    raise(ChannelInUseException)
                else:
                    raise(error)
                
            except Exception as er:
                raise(er)
