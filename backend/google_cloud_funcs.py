from google.cloud import storage
import io

project_id = 'light-maker-411721'

def authenticate_implicit_with_adc():
    storage_client = storage.Client(project=project_id)
    buckets = storage_client.list_buckets()
    print("Buckets:")
    for bucket in buckets:
        print(bucket.name)
    print("Listed all storage buckets.")

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"
    storage_client = storage.Client(project=project_id)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    if blob.exists():
        delete_blob('youtube-audio-editor-videos','final.mp4')

    # Optional: set a generation-match precondition to avoid potential race conditions
    # and data corruptions. The request to upload is aborted if the object's
    # generation number does not match your precondition. For a destination
    # object that does not yet exist, set the if_generation_match precondition to 0.
    # If the destination object already exists in your bucket, set instead a
    # generation-match precondition using its generation number.
    generation_match_precondition = 0

    blob.upload_from_filename(source_file_name, if_generation_match=generation_match_precondition)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )

def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"

    storage_client = storage.Client(project=project_id)

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    generation_match_precondition = None

    # Optional: set a generation-match precondition to avoid potential race conditions
    # and data corruptions. The request to delete is aborted if the object's
    # generation number does not match your precondition.
    blob.reload()  # Fetch blob metadata to use in generation_match_precondition.
    generation_match_precondition = blob.generation

    blob.delete(if_generation_match=generation_match_precondition)

    print(f"Blob {blob_name} deleted.")

def upload_blob_from_stream(bucket_name, file_path, destination_blob_name, project_id):
    """Uploads bytes from a stream or other file-like object to a blob."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The stream or file (file-like object) from which to read
    # import io
    file_obj = io.StringIO(file_path)
    # file_obj.write(b"This is test data.")

    # The desired name of the uploaded GCS object (blob)
    # destination_blob_name = "storage-object-name"

    # Construct a client-side representation of the blob.
    storage_client = storage.Client(project_id)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    # Rewind the stream to the beginning. This step can be omitted if the input
    # stream will always be at a correct position.
    file_obj.seek(0)

    # Upload data from the stream to your bucket.
    blob.upload_from_file(file_obj)

    print(
        f"Stream data uploaded to {destination_blob_name} in bucket {bucket_name}."
    )


if __name__ == '__main__':
    authenticate_implicit_with_adc()