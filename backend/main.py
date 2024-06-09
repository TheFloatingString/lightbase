from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import subprocess as sp

list_of_hashes = list()

def create_item(item_str):
    resp = sp.run(f'echo {item_str} | ipfs add -q', shell=True, capture_output=True)
    list_of_hashes.append(resp.stdout.decode().replace('\n', ''))
    return resp.stdout.decode().replace('\n', '')

def read_item(ipfs_hash):
    resp = sp.run(f'ipfs cat {ipfs_hash}', shell=True, capture_output=True)
    return resp.stdout.decode().replace('\n', '')

class UserItem(BaseModel):
    data: str

app = FastAPI()
templates = Jinja2Templates(directory='templates')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def root():
    return {'data':'Welcome to Lightbase'}

@app.get('/view', response_class=HTMLResponse)
def view(request: Request):
    return templates.TemplateResponse(
            request=request,
            name='view.html')

@app.get('/read/{ipfs_hash}')
def read(ipfs_hash: str):
    item = read_item(ipfs_hash)
    print(item)
    return {'data':item}

@app.get('/write/{msg}')
def write(msg: str):
    item = create_item(msg)
    return {'data': f'Your msg {msg} was recorded!'}

@app.get('/read_all')
def read_all():
    return_dict = {'data':list()}
    for ipfs_hash in list_of_hashes:
        return_dict['data'].append(read_item(ipfs_hash))
    return return_dict

@app.post('/create')
def create(user_item: UserItem):
    ipfs_hash = create_item(user_item.data)
    return {'data':{
        'userItem':user_item.data,
        'ipfsHash':ipfs_hash}}

