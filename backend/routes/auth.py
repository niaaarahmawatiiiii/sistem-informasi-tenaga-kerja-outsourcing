from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/login", response_model=schemas.LoginResponse)
def login(request: schemas.LoginRequest, db: Session = Depends(get_db)):
    
    user = db.query(models.User).filter(
        models.User.vendor == request.vendor,
        models.User.pic_name == request.pic,
        models.User.password == request.password
    ).first()

    if not user:
        raise HTTPException(status_code=401, detail="Login gagal")

    return {
    "vendor": user.vendor,
    "pic": user.pic_name,
    "lokasi_gudang": user.lokasi_gudang,
    "status": user.status
    }


# Api Login Admin
@router.post("/login-admin")
def login_admin(

    data: schemas.AdminLogin,

    db: Session = Depends(get_db)
):

    # Cari dari admin
    admin = db.query(
        models.Admin
    ).filter(

        models.Admin.admin_id
        == data.admin_id

    ).first()


    # Jika data pada admin tidak ada
    if not admin:

        return {
            "message":
            "Admin tidak ditemukan"
        }


    # Cek password pada admin
    if admin.password != data.password:

        return {
            "message":
            "Password salah"
        }


    # Sesi Login pada admin
    return {

        "message":
        "Login berhasil",

        "admin_id":
        admin.admin_id,

        "nama":
        admin.nama,

        "lokasi":
        admin.lokasi,

        "jabatan":
        admin.jabatan,

        "shift":
        admin.shift
    }