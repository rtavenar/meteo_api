from pydantic import BaseModel


class StationSummary(BaseModel):
    """Résumé d'une station météorologique."""
    id: str
    latitude_centre: float
    longitude_centre: float
    rayon_km: float
    temperature_actuelle: float
    precipitations_24h: float


class StationList(BaseModel):
    """Liste des identifiants de stations."""
    stations: list[str]
