import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/')
def start_page() -> HTMLResponse:
    return HTMLResponse('<h1>Rekruto! Давай дружить!</h1>')


@app.get('/name={name}message={message}')
def second_page(name: str, message: str) -> HTMLResponse:
    return HTMLResponse(f'<h1>Hello, {name}! {message}!</h1>')


if __name__ == '__main__':
    uvicorn.run(app, port=8080)
