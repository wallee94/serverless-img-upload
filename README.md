# Serverless Image Upload

This is an example app to show how to upload an image (o any file)
to an s3 bucket from client-side, avoiding the duplicate
process of uploading the image to a middleware server first.

Here I use s3 presigned urls to give access to the client to write
to the bucket.

Upload validations and url exchange are done using flask. Zappa 
is used to turn the wsgi into serverless lambda functions 
and handle the s3 and API gateway configs.

Form submit is handled using pure javascript.

## Website

Try a deployed version in:
https://iqvgcod8hi.execute-api.us-west-1.amazonaws.com/dev

## Run the example

To run it using your own AWS creds:
- Install the requirements `pip install -r requirements.txt`
- Set your AWS credentials
```bash
#!/bin/bash
export AWS_ACCESS_KEY_ID=<access-key>
export AWS_SECRET_ACCESS_KEY=<secret-key>
``` 
- Update your upload bucket name in `app.py` and `index.html`
- Start and deploy your zappa application `zappa init`
- In the new `zappa_settings.json` and a new `aws_region` key with your AWS region
- Deploy your app `zappa deploy <stage-name>`