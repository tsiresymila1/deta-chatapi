

import bcrypt
from deta import Deta
from starlite import UploadFile
import uuid


async def save_file(deta: Deta, file: UploadFile, directory: str = "photos", encrypted: bool = False):
    filename: str = file.filename
    if encrypted:
        filename = f"{directory}_{uuid.uuid4().hex}.{file.filename.split('.')[-1]}"
    content: bytes = await file.read()
    drive = deta.Drive(directory)
    drive.put(filename, content)
    return filename


def hash_pasword(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
