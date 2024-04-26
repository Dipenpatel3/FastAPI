from fastapi import FastAPI
import uvicorn 

app=FastAPI()

@app.get("/")
def index():
    return {'data':{'name':'Dipen Manoj Patel'}}  



@app.get('/about')
def about():
    return {'data':['About the page']}