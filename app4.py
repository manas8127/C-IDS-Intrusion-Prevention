# This page is used to uppload a csv file to our Amazon S3 bucket 

import boto3
import streamlit as st
# from aws import *


NEW_AWS_ACCESS_KEY_ID = "AKIAWUZ42VJKZJRRTH2M"
NEW_AWS_SECRET_ACCESS_KEY = "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"

client = boto3.client(
	"s3",
    aws_access_key_id = NEW_AWS_ACCESS_KEY_ID,
    aws_secret_access_key = NEW_AWS_SECRET_ACCESS_KEY,
    region_name = 'ap-south-1'
)

s3 = boto3.resource(
	's3',
    aws_access_key_id = NEW_AWS_ACCESS_KEY_ID,
    aws_secret_access_key = NEW_AWS_SECRET_ACCESS_KEY,
    region_name = 'ap-south-1'
)

def app():
	st.title("Upload your Data")


	chosen_file = st.file_uploader("Choose a file", type=['csv','xlsx'])

	if chosen_file is None: 
		st.write("No file is chosen at the present moment!")
	else: 
		st.write("The name of the chosen file is {}".format(chosen_file.name))
		
		path = st.text_input("Specify the file path")

		path = r'{}'.format(path)
		# try:  
		if path is not None or path is not '':
			s3.meta.client.upload_file(path, 'cyber-mads-2', chosen_file.name)
			st.success("The file must have uploaded!")