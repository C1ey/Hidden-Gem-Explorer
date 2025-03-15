from fastapi import FastAPI
from app.routes import locations, auth, users, interactions

app = FastAPI()

# Register API Routes
app.include_router(locations.router, prefix="/api/locations")
app.include_router(auth.router, prefix="/api/auth")
app.include_router(users.router, prefix="/api/users")
app.include_router(interactions.router, prefix="/api/interactions")

@app.get("/")
async def root():
    return {"message": "Hidden Gem Explorer API is running!"}
