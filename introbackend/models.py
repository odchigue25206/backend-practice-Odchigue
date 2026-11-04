from sqlmodel import Field , SQLModel

class customer(SQLModel, table=True):
    cosid: int | None = Field(default=None, primary_key=True)
    name: str
    order_details: str
    age: int | None = None
    payment: int

class employee(SQLModel, table=True):
    empid: int | None = Field(default=None, primary_key=True)
    name: str
    department: str
    age: int | None = None
    shift: str


class store(SQLModel, table=True):
    store_id: int | None = Field(default=None, primary_key=True)
    name: str
    location: str
    opening_year: int
    items: str

