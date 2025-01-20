from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/user/admin")
async def admin():
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}") # От 1 до 100
async def user_id(user_id: Annotated[int, Path(gt=0, le=100, description="Enter User ID", example=1)]):
    return {"message": f"Вы вошли как пользователь {user_id}"}


@app.get("/user") # Имя от 5 до 20 (прости, Олег). Возраст от 18 до 120
async def user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]
):
    return {"message": f"Информация о пользователе. Имя: {username}. Возраст: {age}" }


@app.get("/")
async def main():
    return {"message": "Главная страница"}
