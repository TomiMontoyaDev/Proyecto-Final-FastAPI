from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

# Conexión directa a CockroachDB en la VM
DB_URL = "postgresql://root@192.168.64.2:26257/laboratorio_db"
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Modelo de auditoría
class LoginEvent(Base):
    __tablename__ = "login_events"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    event_type = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Crear tablas si no existen
def init_db():
    Base.metadata.create_all(bind=engine)

# Función inyectora independiente
def inject_login_event(username: str, event: str):
    """
    Registra un evento en CockroachDB de forma independiente.
    """
    db = SessionLocal()
    try:
        new_log = LoginEvent(username=username, event_type=event)
        db.add(new_log)
        db.commit()
    except Exception as e:
        print(f"Error al inyectar evento en CockroachDB: {e}")
    finally:
        db.close()
