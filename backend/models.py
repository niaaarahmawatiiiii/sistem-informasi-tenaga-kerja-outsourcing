from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from .database import Base
from sqlalchemy import DateTime
from datetime import datetime

#menghubungkan ke table users
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    vendor = Column(String)
    pic_name = Column(String)
    password = Column(String)
    lokasi_gudang = Column(String)
    status = Column(String, default="active")


#menghubungkan ke table workers
class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String)
    nik = Column(String)
    no_kk = Column(String)
    jenis_kelamin = Column(String)
    alamat = Column(String)
    email = Column(String)
    no_hp = Column(String)
    vendor = Column(String)
    posisi = Column(String)
    nama_rekening = Column(String)
    no_rekening = Column(String)
    bank = Column(String)
    tipe_kontrak = Column(String)

#menghubunkan modle class dengan table workers
class WorkerID(Base):
    __tablename__ = "worker_ids"

    id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(Integer, ForeignKey("workers.id"))
    id_pekerja = Column(String)
    status = Column(String, default="inactive")

#menghubungkan ke table worker_placments
class WorkerPlacement(Base):
    __tablename__ = "worker_placements"

    id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(Integer, ForeignKey("workers.id"))
    placement_id = Column(Integer)
    start_date = Column(DateTime)   
    end_date = Column(DateTime)     

#menghubungkan ke table palacments
class Placement(Base):
    __tablename__ = "placements"

    id = Column(Integer, primary_key=True)
    nama_penempatan = Column(String)

#menghubungkan ke table activities
class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True)
    worker_id = Column(Integer, ForeignKey("workers.id"))
    activity_type = Column(String)
    status = Column(String)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


#menghubungkan model ke table worker_plans
class WorkerPlan(Base):
    __tablename__ = "worker_plans"
    id = Column(Integer, primary_key=True, index=True)
    tanggal = Column(String)
    shift = Column(String)
    lokasi = Column(String)
    total_barang = Column(Integer)
    total_kebutuhan = Column(Integer)
    vendor_a_need = Column(Integer)
    vendor_b_need = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)


class WorkerAttendance(Base):

    __tablename__ = "worker_attendances"

    id = Column(Integer, primary_key=True, index=True)

    worker_id = Column(
        Integer,
        ForeignKey("workers.id")
    )
    id_pekerja = Column(String)
    tanggal = Column(String)
    shift = Column(String)
    vendor = Column(String)
    lokasi = Column(String)
    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
    attendance_type = Column(String)


class Admin(Base):

    __tablename__ = "admins"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    admin_id = Column(String)
    nama = Column(String)
    lokasi = Column(String)
    jabatan = Column(String)
    shift = Column(String)
    password = Column(String)

# menghubungkan ke table disable workers
class DisabledWorker(Base):

    __tablename__ = (
        "disabled_workers"
    )

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    id_pekerja = Column(
        String,
        nullable=False
    )

    nama_pekerja = Column(
        String,
        nullable=False
    )

    vendor = Column(
        String,
        nullable=False
    )

    disabled_by = Column(
        String,
        nullable=False
    )

    disabled_at = Column(
        DateTime,
        default=datetime.utcnow
    )