
from uvicorn.main import run
if __name__ == "__main__":
    run("main:app", port=8001, reload=True,
        reload_excludes=["node_modules", "assets"])
