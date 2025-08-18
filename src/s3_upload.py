import os
import boto3

MAX_FILE_SIZE_MB = 100
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

def upload_file_to_s3(file_path, bucket_name):
    if not os.path.exists(file_path):
        print(f"Fehler: Datei '{file_path}' nicht gefunden.")
        return False

    file_size = os.path.getsize(file_path)
    if file_size > MAX_FILE_SIZE_BYTES:
        print(f"Fehler: Datei '{file_path}' ist zu groß ({file_size / (1024 * 1024):.2f} MB).")
        print(f"Das maximale Limit beträgt {MAX_FILE_SIZE_MB} MB. Upload abgebrochen.")
        return False

    s3_client = boto3.client('s3')

    try:
        s3_client.upload_file(file_path, bucket_name, os.path.basename(file_path))
        print(f"Datei '{file_path}' erfolgreich in S3 hochgeladen.")
        return True
    except Exception as e:
        print(f"Fehler beim Upload: {e}")
        return False

BUCKET_NAME = 'datauploadtool'

if __name__ == "__main__":
    local_file_path = r"C:\Users\kurta\Downloads\Screenshot 2025-08-18 150812.png"

    upload_file_to_s3(local_file_path, BUCKET_NAME)