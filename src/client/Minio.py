import os

from minio import Minio
from minio.error import S3Error

from env_config import MINIO_CONFIG

MINIO_URL = str(MINIO_CONFIG["MINIO_ENDPOINT"]) + ":" + str(MINIO_CONFIG["MINIO_PORT"])

minio_client = Minio(
    endpoint=MINIO_URL,
    access_key=str(MINIO_CONFIG["MINIO_ACCESS_KEY"]),
    secret_key=str(MINIO_CONFIG["MINIO_SECRET_KEY"]),
    secure=bool(MINIO_CONFIG["MINIO_USE_SSL"]),
)


def put_in_minio_by_file_object(object_name, file_object):
    try:
        result = minio_client.put_object(
            bucket_name=MINIO_CONFIG["MINIO_BUCKET_NAME"],
            object_name=object_name,
            data=file_object,
            length=-1,
            part_size=5 * 1024 * 1024  # 5MB
        )
        return f"/{result.bucket_name}/{result.object_name}"
    except S3Error as exc:
        print("error occurred.", exc)


def put_in_minio_by_file_path(object_name, file_path):
    try:
        result = minio_client.fput_object(
            bucket_name=MINIO_CONFIG["MINIO_BUCKET_NAME"],
            object_name=object_name,
            file_path=file_path,
        )
        return f"/{result.bucket_name}/{result.object_name}"
    except S3Error as exc:
        print("error occurred.", exc)


if __name__ == "__main__":
    try:
        current_directory = os.getcwd()
        print(f"Current directory: {current_directory}")
        # change directory
        print("Changing directory to the root of the project")
        os.chdir("../../")
        current_directory = os.getcwd()
        print(f"Current directory: {current_directory}")

        result = put_in_minio_by_file_path("image.jpg", "src/service/result/image.jpg")
        print(result.etag)
    except S3Error as exc:
        print("error occurred.", exc)
