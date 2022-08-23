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


# set cross-origin resource sharing
origins = [
    "http://localhost:5050"
    , "http://127.0.0.1:5050"
]

# init app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/', status_code=status.HTTP_200_OK)
async def root():
    response = {'data': 'Hello World!'}
    return response

@app.post('/chat/', response_model=DataOut, status_code=status.HTTP_200_OK)
async def chat_with_bot(data_in: DataIn):
    if data_in.content:
        answer = bloom.predict(content=data_in.content)
        response = {'data': answer[0]['generated_text']}
    else:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='Empty prompt'
        )
    
    return response