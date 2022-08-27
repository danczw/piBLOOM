from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# handle different entry points
try:
    from pibloom.model import bloom_model
except ImportError:
    from model import bloom_model

# load BLOOM model from local files
bloom = bloom_model()

# set request and response models
class DataIn(BaseModel):
    content: str

class DataOut(BaseModel):
    data: str

# init app
app = FastAPI()

# define CORS allowed origins
origins = [
    "http://localhost:5050"
    , "http://127.0.0.1:5050"
    , "http://localhost:8080"
    , "http://127.0.0.1:8080"
]

# set CORS policy
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# root path request
@app.get('/', status_code=status.HTTP_200_OK)
async def root():
    response = {'data': 'Hello World!'}
    return response

# bloom model inference request
@app.post('/chat/', response_model=DataOut, status_code=status.HTTP_200_OK)
async def chat_with_bot(data_in: DataIn):
    if data_in.content:
        # generate BLOOM model response
        answer = bloom.predict(content=data_in.content)
        response = {'data': answer[0]['generated_text']}
    else:
        # return error if no input
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='Empty prompt'
        )
    
    return response