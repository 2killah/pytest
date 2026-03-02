from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Salem"}

@app.get('/sum')
def get_sum(a: int, b: int):
    return {"result": a + b}

