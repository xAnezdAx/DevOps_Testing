from fastapi import FastAPI

app = FastAPI()


#api web que nos permite conservar con el servidor
#estado de la aplicacion
@app.get("/")
def hello():
    return {"message": "Hello World"}