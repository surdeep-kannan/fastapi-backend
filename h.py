from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# allow React Native app to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # or list specific URLs later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend connected to React Native!"}
