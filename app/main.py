from fastapi import FastAPI
from app.database.base import Base
from app.database.session import engine
from app.routers import events, members, attendance, dashboard
from fastapi.middleware.cors import CORSMiddleware
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Attendance System API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(events.router, prefix="/api/events", tags=["events"])
app.include_router(members.router, prefix="/api/members", tags=["members"])
app.include_router(attendance.router, prefix="/api/attendance", tags=["attendance"])
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["dashboard"])

@app.get("/")
def read_root():
    return {"message": "Attendance System API"}