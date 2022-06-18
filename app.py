from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import uvicorn

app = FastAPI(debug=True)

#creating a home route
@app.get('/')
async def Home():
    return {'text': 'Welcome!'}

@app.get('/{name}')
def Info(name:str):
    return {'Welcome {} Check the Bank Customer Prediction App!'.format(name)}

#a route for the model prediction
@app.post('/predict')   
def Customer(CreditScore: int, Geography:int, Gender: int, Age : int, Tenure:int, Balance:int, NumOfProduct:int,HasCrCard:int, IsActiveMember:int, EstimatedSalary:int):
    
    model = pickle.load(open('C:/Users/User/Herokuapp/Customer_chun/chun_model.pkl','rb'))
    make_prediction = model.predict(([[CreditScore,Geography, Gender, Age, Tenure, Balance, NumOfProduct, HasCrCard, IsActiveMember, EstimatedSalary]]))
    result = make_prediction[0]
    if (result > 0.5):
        return {'This Customer will not chun!'}
    else:
        return {'This Customer will leave soon. Please take action!'}
        
    # return {
    #     'The prediction is {}'.format(result)
    # }   
    
if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)

