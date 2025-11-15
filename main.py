import uvicorn
from fastapi import FastAPI
from BankNodes import BankNode
import numpy as np
import pickle
import pandas as pd
app=FastAPI()
pickled_in=open("model.pkl","rb")
model=pickle.load(pickled_in)
@app.get("/")
def index():
    return {"message": "Hello, World!"}
@app.get('/name')
@app.get('/welcome')
def get_name(name:str):
    return {'welcome to krish youtube channel':f'{name}'}
@app.post('/predict')
def predict_species(data:BankNode):
    data=data.dict()
    varience=data['varience']
    skeawness=data['skeawness']
    curtosis=data['curtosis']
    entropy=data['entropy']
    #print(model.predict([[varience,skeawness,curtosis,entropy]]))
    prediction=model.predict([[varience,skeawness,curtosis,entropy]])
    if(prediction[0]>0.5):
        prediction="Fake Bank Note"
    else:
        prediction="Real Bank Note"
    return{'prediction':prediction}
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
#uvicorn main:app --reload