from fastapi import FastAPI


app = FastAPI()


@app.get("/users")
def get_users() -> dict:
    return {
        "users": [
            {"username": "Alice"},
            {"username": "Bob"},
        ]
    }
