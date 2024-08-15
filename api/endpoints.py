from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def heatlh_check():
    return {"message": "OK"}
