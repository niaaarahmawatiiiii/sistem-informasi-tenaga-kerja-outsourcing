from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = (
    "postgresql://"
    "postgres.pmjwgslolhikqxhicwsq:"
    "P180304ilyas"
    "@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres" #menghubungkan ke database bpo_area di supabase
    "?sslmode=require"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()