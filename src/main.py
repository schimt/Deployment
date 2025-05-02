from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import debugpy

debugpy.listen(("0.0.0.0", 5678))
# debugpy.wait_for_client()

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




# Define the API endpoints
@app.get('/')
def health():
    return {
        "message": "sup"
    }



#implement routes for each of the steps: paper retrieval, etc.