from fastapi import FastAPI, status, HTTPException
from fastapi.logger import logger as fastapi_logger
from fastapi.middleware.cors import CORSMiddleware
import logging
from pydantic import BaseModel
import yaml

# handle different entry points
try:
    from pibloom.model import bloom_model
except ImportError:
    from model import bloom_model

'''
    When running with gunicorn the log handlers get suppressed instead of
    passed along to the container manager. This forces the gunicorn handlers
    to be used throughout the project.
'''
with open('config.yml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    logging.config.dictConfig(config)

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
    '*'
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
        answer = answer.rsplit('.', 1)[0] + '.'
        response = {'data': answer}
    else:
        # return error if no input
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='Empty prompt'
        )
    
    return response