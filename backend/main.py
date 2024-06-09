from fastapi import FastAPI
import subprocess as sp

def create_item(item_str):
    resp = sp.run(f'echo {item_str} | ipfs add -q', shell=True, capture_output=True)
    return resp.stdout.decode().replace('\n', '')

def read_item(ipfs_hash):
    resp = sp.run(f'curl https://ipfs.io/ipfs/{ipfs_hash}', shell=True, capture_output=True)
    return resp

app = FastAPI()

@app.get('/')
def root():
    return {'data':'Welcome to Lightbase'}

@app.get('/read/{ipfs_hash}')
def read(ipfs_hash: str):
    resp = read_item(ipfs_hash)
    print(resp)
    return {'data':'200'}


