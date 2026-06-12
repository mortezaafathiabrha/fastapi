from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def hello_world():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World - FastAPI</title>
        <style>
            body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); }
            .container { text-align: center; color: white; }
            h1 { font-size: 3em; margin: 0; }
            p { font-size: 1.2em; margin-top: 10px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello World!</h1>
            <p>Welcome to FastAPI</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
