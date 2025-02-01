from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.services.admin import AdminService
from app.schemas.admin import AdminCreate

def create_superuser():
    db = SessionLocal()
    try:
        admin_data = AdminCreate(
            email="admin@theeye.com",
            username="superadmin",
            password="your-secure-password",
            is_superuser=True
        )
        admin = AdminService.create_admin(db, admin_data)
        print(f"Superuser created successfully: {admin.email}")
    except Exception as e:
        print(f"Error creating superuser: {str(e)}")
    finally:
        db.close()

if __name__ == "__main__":
    create_superuser() 