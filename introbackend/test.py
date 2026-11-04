from fastapi import FastAPI
from sqlmodel import Session , select
from contextlib import asynccontextmanager
from database import create_db_and_tables, engine

from models import customer, employee, store

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)



@app.get("/")
async def root():
    return {"message": "Hello customers welcoem to the store man o0f nigs"}


@app.get("/customer/{id}")
async def read_customer(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        emp = session.get(customer, id)
        return {"message": emp}
    

@app.post("/customer")
async def root(customer  : customer):
    with Session(engine) as session:
        session.add(customer)
        session.commit()
        session.refresh(customer)

        return {"message": 'created'}



@app.get("/employee/{id}")
async def read_employee(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        emp = session.get(employee, id)
        return {"message": emp}
    

@app.post("/employee")
async def root(employee  : employee):
    with Session(engine) as session:
        session.add(employee)
        session.commit()
        session.refresh(employee)

        return {"message": 'created'}


@app.get("/store/{id}")
async def read_store(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        emp = session.get(store, id)
        return {"message": emp}
    

@app.post("/store")
async def root(store  : store):
    with Session(engine) as session:
        session.add(store)
        session.commit()
        session.refresh(store)

        return {"message": 'created'}