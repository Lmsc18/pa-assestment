from dotenv import load_dotenv
load_dotenv()
import os
index_name=os.getenv("INDEX")

from typing import Union
import uvicorn
from fastapi import FastAPI
from search import search_file


app = FastAPI()


@app.post("/query")
def inference(input: str):
    docs=search_file(input)
    return {"relevant_documents":docs}


if __name__ == "__main__":
    # Run the FastAPI application using uvicorn
    uvicorn.run(app,host="0.0.0.0", port=8000)