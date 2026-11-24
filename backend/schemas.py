from pydantic import BaseModel

# AUTHENTICATION

# Request login untuk PIC Vendor
class LoginRequest(BaseModel):
    vendor: str
    pic: str
    password: str

# Response setelah login berhasil
class LoginResponse(BaseModel):
    vendor: str
    pic: str
    lokasi_gudang: str
    status: str

# DATA PEKERJA

# Schema untuk membuat data pekerja baru
class CreateWorker(BaseModel):
    nama: str
    nik: str
    no_kk: str
    jenis_kelamin: str
    alamat: str
    email: str
    no_hp: str
    vendor: str
    departemen: str
    nama_rekening: str
    no_rekening: str
    bank: str
    tipe_kontrak: str

# AKTIVASI DAN MUTASI PEKERJA

# Schema untuk aktivasi ID pekerja ke suatu penempatan
class ActivateWorker(BaseModel):
    id_pekerja: str
    placement_id: int

# Schema untuk mutasi pekerja ke penempatan lain
class MutasiWorker(BaseModel):
    id_pekerja: str
    placement_id: int

# PERUBAHAN DATA KONTRAK

# Schema untuk mengubah tipe kontrak dan departemen pekerja
class EditContract(BaseModel):
    id_pekerja: str
    tipe_kontrak: str
    departemen: str

# ADMIN GUDANG
# Schema untuk membuat rencana kebutuhan tenaga kerja
class CreateWorkerPlan(BaseModel):
    tanggal: str
    shift: str
    lokasi: str
    total_barang: int
    total_kebutuhan: int
    vendor_a_need: int
    vendor_b_need: int


# Schema untuk mencatat kehadiran pekerja yang masuk bekerja
class CreateWorkerAttendance(BaseModel):
    tanggal: str
    shift: str
    vendor: str
    lokasi: str
    worker_ids: list[str]

# Schema untuk mencatat pekerja yang dikeluarkan dari shift
class TakeoutWorker(BaseModel):
    tanggal: str
    shift: str
    vendor: str
    id_pekerja: str


# Schema untuk menonaktifkan ID pekerja
class NonaktifkanWorker(BaseModel):
     id_pekerja: str

# LOGIN ADMIN
class AdminLogin(BaseModel):
    admin_id: str
    password: str

# BUFFER ATTENDANCE

# Schema untuk menyimpan data buffer attendance
class CreateBufferAttendance(BaseModel):

    tanggal: str

    shift: str

    vendor: str

    lokasi: str

    worker_ids: list[str]