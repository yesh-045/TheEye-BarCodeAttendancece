from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.admin import Admin
from app.services.auth import AuthService
from datetime import datetime

class AdminService:
    @staticmethod
    def create_admin(db: Session, admin_data):
        # Check if email already exists
        if db.query(Admin).filter(Admin.email == admin_data.email).first():
            raise HTTPException(status_code=400, detail="Email already registered")
        
        # Create new admin
        hashed_password = AuthService.get_password_hash(admin_data.password)
        db_admin = Admin(
            email=admin_data.email,
            username=admin_data.username,
            hashed_password=hashed_password,
            is_superuser=admin_data.is_superuser
        )
        db.add(db_admin)
        db.commit()
        db.refresh(db_admin)
        return db_admin

    @staticmethod
    def authenticate_admin(db: Session, email: str, password: str):
        admin = db.query(Admin).filter(Admin.email == email).first()
        if not admin:
            return None
        if not AuthService.verify_password(password, admin.hashed_password):
            return None
        
        # Update last login
        admin.last_login = datetime.utcnow()
        db.commit()
        return admin

    @staticmethod
    def get_admin_by_email(db: Session, email: str):
        return db.query(Admin).filter(Admin.email == email).first()

    @staticmethod
    def get_all_admins(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Admin).offset(skip).limit(limit).all() 