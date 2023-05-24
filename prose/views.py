import filetype

from uuid import uuid4
from datetime import datetime

from django.core.files.storage import default_storage
from django.http import JsonResponse

from prose import settings


def validate_file(file):
    file_type = filetype.guess(file).mime
    file_size = file.size / 1024 / 1024
    if (
        file_type in settings.ALLOWED_ATTACHMENT_FILE_TYPES
        and file_size <= settings.ALLOWED_ATTACHMENT_FILE_SIZE
    ):
        return True
    return False


def upload_attachment(request):
    if request.method == "POST":
        attachment = request.FILES["file"]
        if not validate_file(attachment):
            return JsonResponse({"error": "File type or size not allowed"}, status=400)
        key = f"{datetime.now().strftime('%Y/%m/%d')}/{uuid4()}.{attachment.name.split('.')[-1]}"
        path = f"prose/{key}"
        default_storage.save(path, attachment)
        payload = {
            "url": default_storage.url(path),
        }
        return JsonResponse(payload, status=201)
