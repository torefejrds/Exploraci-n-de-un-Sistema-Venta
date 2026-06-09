from fastapi import FastAPI
from routes import client_api, location_api
from fastapi import FastAPI
from routes import product_routes, sale_routes

import models

app = FastAPI(title="Sistema de Ventas")
app = FastAPI(
    title = "wholesale Sytem",
    description="API Servicie",
    version="1.0.0"
)

# Endpoint de entrada o de raiz 
@app.get("/")
def read_root():
    return { "Hello": "World"}

app.include_router(client_api.router)
app.include_router(location_api.router)


app.include_router(product_routes.router)
app.include_router(sale_routes.router)

# main.py
from fastapi import FastAPI
from config.database import Base, engine
from routes import product_routes, sale_routes

app = FastAPI(title="Sistema de Ventas con DB")

Base.metadata.create_all(bind=engine)

app.include_router(product_routes.router)
app.include_router(sale_routes.router)
