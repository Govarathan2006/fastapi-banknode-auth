from pydantic import BaseModel

class BankNode(BaseModel):
    varience: float
    skeawness: float
    curtosis: float
    entropy: float