from fastapi import FastAPI
from app.config import settings
from app.routers import routes  # Asegúrate de tener el archivo de rutas creado

app = FastAPI(title="Microservicio de Gestión de Rutas")

# Incluir las rutas (routers)
app.include_router(routes.router)

# Punto de inicio para pruebas de carga de configuraciones
@app.get("/config")
async def get_config():
    return {
        "GOOGLE_MAPS_API_KEY": settings.GOOGLE_MAPS_API_KEY,
        "DATABASE_URL": settings.DATABASE_URL,
        "REDIS_URL": settings.REDIS_URL,
    }
