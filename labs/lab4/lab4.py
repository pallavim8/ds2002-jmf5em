#!/Users/pallavimamillapalli/.local/share/virtualenvs/ds2002-jmf5em-W2s8803g/bin/python3
import requests
import os
import boto3

def download_file(url, file_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"File downloaded to {file_path}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error downloading: {e}")

image_url = "https://images.pexels.com/photos/414612/pexels-photo-414612.jpeg?cs=srgb&dl=pexels-souvenirpixels-414612.jpg&fm=jpg"
file = "downloaded_image.gif"
path = os.path.join(os.getcwd(), file)
download_file(image_url, path)

s3 = boto3.client('s3')
response = s3.put_object(
	Body = file,
	Bucket = 'ds2002-jmf5em',
	Key = file
)

bucket_name = 'ds2002-jmf5em'
object_name = file
expires_in = 30

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
)

print(response)