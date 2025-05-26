from fastapi import FastAPI

api = FastAPI()


@api.get("/")
async def root():
    """
    Returns a summary of all ML projects hosted in portfolio app.

    :return: Placeholder content that is later queried from a database.
    """
    return {"content": "Sample content for portfolio home page"}


@api.get("/about")
async def about():
    """
    Returns detailed info about site owner's skills, certificates,
    badges, etc.

    :return: Placeholder content that is later queried from a database.
    """
    return {"content": "Sample content for site owner credentials"}
