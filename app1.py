import streamlit as st
import joblib
import os
import pandas as pd
import boto3
import seaborn as sns

sns.set_style('darkgrid')

# ml_model_path = r'C:\Users\lenovo\Documents\Cyber-MADS\pull-three\Cyber_MADS\model_joblib'
# ml_model = joblib.load(os.path.expanduser(ml_model_path))

bucket_name = 'cyber-mads-2'

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


def ml_model():
    mj=joblib.load('model_joblib_real')
    df = pd.read_csv('x_test_amex_real.csv')
    
    for i in range(1, 21):
        d=df.iloc[i-1:i]
        st.write("\n")
        st.write("\n")
        st.write(d)
        port = d['Destination Port']
        val = mj.predict(d)
        if val == 0:
            st.success("Benign network, NORMAL TRAFFIC detected!")
        elif val == 1:
            st.error("DDoS attack detected! IP address 205.174.165.73 blocked for next 15 seconds ".format(port.to_string(index=False)))
        elif val == 2: 
            st.error("PortScan attack detected! IP address 205.174.165.73 blocked for next 15 seconds  ".format(port.to_string(index=False)))
        elif val == 3:
            st.error("Bot attack detected! IP address 205.174.165.73 blocked for next 15 seconds ".format(port.to_string(index=False)))
        elif val == 4: 
            st.error("Infiltration attack detected! IP address 205.174.165.73 blocked for next 15 seconds ".format(port.to_string(index=False)))
        elif val == 5: 
            st.error("Web attack (Brute Force) detected! IP address 205.174.165.73 blocked for next 15 seconds ".format(port.to_string(index=False)))
        elif val == 6:
            st.error("Web attack (XSS) detected! IP address 205.174.165.73 blocked for next 15 seconds ".format(port.to_string(index=False)))
        elif val == 7:
            st.error("Web attack (SQL Injection) detected! IP address 205.174.165.73 blocked for next 15 seconds ".format(port.to_string(index=False)))
        else:
            st.error("FTP-Patator attack detected! IP address 205.174.165.69 blocked for next 15 seconds ".format(port.to_string(index=False)))


def app():
    st.title('Dashboard')

    # filename = st.text_input("Name of the file with the extension")
    # st.write("Choose whether you want to download or stream the file")
    # download_location = 'C:/Users/lenovo/Downloads/{}'.format(filename)
    # if st.button("Download"):
    #     client.download_file('cyber-mads-2', filename, download_location)
    #     st.success("File must have been downloaded!")
    #     ml_model()
    # if st.button("Stream"):
    #     obj = client.get_object(Bucket=bucket_name, Key=filename)
    #     st.write(obj['Body'])
    #     ml_model()
    ml_model()
    


'''
    sns.countplot(x=df['Destination Port'], data=df, hue=df['Label'])
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
'''