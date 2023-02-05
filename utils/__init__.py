

import bcrypt
from deta import Deta
from starlite import UploadFile
import uuid
import mimetypes
from PIL import Image
import io

async def save_file(deta: Deta, file: UploadFile, directory: str = "photos", encrypted: bool = False):
    filename: str = file.filename
    if encrypted:
        filename = f"{directory}_{uuid.uuid4().hex}.{file.filename.split('.')[-1]}"
    
    mime = mimetypes.MimeTypes().guess_type(filename)
    content: bytes = await file.read()
    if mime != None:
        filemile = mime[0]
        if filemile.startswith('image') :
            try:
                image: Image  = Image.open(file.file)
                image.thumbnail((100,90))
                img_byte_arr = io.BytesIO()
                image.save(img_byte_arr, format='PNG')
                content = img_byte_arr.tobytes()
            except Exception as e :
                pass
    drive = deta.Drive(directory)
    drive.put(filename, content)
    return filename


def hash_pasword(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
