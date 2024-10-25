from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Crear el motor de la base de datos usando la URL de conexión
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Crear una sesión asíncrona para manejar las operaciones en la base de datos
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Función para obtener una sesión de base de datos
async def get_db():
    async with async_session() as session:
        yield session
