from starlite import MediaType, get, NotFoundException
from starlite.response import Response
from deta import Deta
# import magic
import mimetypes
from app.auth.middleware import jwt_auth


@get('/storage/private/{name:str}', include_in_schema=False, middleware=[])
async def download(name: str, deta: Deta) -> Response:
    names = name.split('_')
    mime = mimetypes.MimeTypes().guess_type(name)
    if mime != None:
        filemime = mime[0]
    else:
        filemime = "image/*"
    if len(names) >= 2:
        store = ''.join(filter(str.isalnum, names[0]))
        drive = deta.Drive(store)
        res = drive.get(name)
        
        if res != None:
            return Response(res.read(),media_type=filemime)

    raise NotFoundException()
