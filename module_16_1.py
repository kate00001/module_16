from fastapi import FastAPI

app = FastAPI()


@app.get("/user/admin")
async def admin():
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def user_id(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь {user_id}"}


@app.get("/user")
async def user(username: str, age: int) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}. Возраст: {age}" }


@app.get("/")
async def main():
    return {"message": "Главная страница"}
