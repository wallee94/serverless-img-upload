import mimetypes
import uuid

import boto3
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/json/')
def get_json():
    return jsonify({'details': "this is a json"})


@app.route('/presigned/')
def generate_presigned_post():
    # Get the service client
    s3 = boto3.client('s3')
    ext = request.args['ext']
    type_guess, _enc = mimetypes.guess_type(f'file.{ext}')

    if not type_guess:
        response = jsonify({'details': 'unknown extension received'})
        response.status_code = 400
        return response

    if not type_guess.startswith('image'):
        response = jsonify({'details': 'file has to be an image'})
        response.status_code = 400
        return response

    # Make sure everything posted is publicly readable
    fields = {"acl": "public-read"}

    # Ensure that the ACL isn't changed and restrict the user to a length
    conditions = [
        {"acl": "public-read"},
    ]

    # Generate the POST attributes
    post = s3.generate_presigned_post(
        Bucket='flask-serverless-123',
        Key=f'files/{str(uuid.uuid4())}.{ext}',
        Fields=fields,
        Conditions=conditions
    )
    return jsonify({'fields': post['fields'], 'url': post['url']})


if __name__ == '__main__':
    app.run()
