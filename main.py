from fastapi import FastAPI
import uvicorn 

app=FastAPI()

@app.get("/")
def index():
    return {'data':{'name':'Dipen Manoj Patel'}}  

@app.get('/about')
def about():
    return {'data':['About the page']}

@app.get('/personal')
def personal():
    return {'Details':{'Phone Number':'+1857-230-7571'}}

@app.get('/hello')