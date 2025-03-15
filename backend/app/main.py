from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import auth, locations, users, interactions, websocket

app = FastAPI(title="Hidden Gem Explorer API")

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all routers
app.include_router(auth.router)
app.include_router(locations.router)
app.include_router(users.router)
app.include_router(interactions.router)
app.include_router(websocket.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Hidden Gem Explorer API"}
