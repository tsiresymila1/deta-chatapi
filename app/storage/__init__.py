from starlite import get, NotFoundException
from starlite.response import StreamingResponse
from deta import Deta

from app.auth.middleware import jwt_auth


@get('/storage/private/{name:str}', include_in_schema=False, middleware=[jwt_auth.middleware])
async def download(name: str, deta: Deta) -> StreamingResponse:
    names = name.split('_')
    if len(names) >= 2:
        store = ''.join(filter(str.isalnum, names[0]))
        drive = deta.Drive(store)
        res = drive.get(name)
        if res != None:
            return StreamingResponse(res.iter_chunks(1024))

    raise NotFoundException()
