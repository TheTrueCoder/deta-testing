from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({"message": "Hello, world!"})


# notice that the app instance is called `app`, this is very important.
app = Starlette(debug=True, routes=[
    Route('/', homepage),
])
