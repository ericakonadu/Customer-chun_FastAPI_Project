from pydantic import BaseModel
from typing import List
class Customer(BaseModel):
    CreditScore:int
    Geography: int
    Gender: int
    Age: int
    Tenure: int
    Balance: float
    NumOfProduct: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float
    
    
    