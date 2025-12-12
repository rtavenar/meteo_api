from pathlib import Path
from fastapi import FastAPI, HTTPException
from .schemas import StationList, StationSummary
import json

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
STATIONS_FILE = DATA_DIR / "stations.json"

app = FastAPI(
    title="Stations Météorologiques API",
    version="0.1.0",
    description=(
        "API pour consulter les données des stations météorologiques. "
        "Chaque station possède une zone de couverture circulaire définie par "
        "sa position GPS (latitude, longitude) et un rayon en kilomètres. "
        "Les données incluent la température actuelle et les précipitations sur 24h."
    ),
    contact={"name": "Meteo API Maintainer", "email": "dev@example.com"},
    license_info={"name": "MIT"},
)


def _load_stations() -> dict:
    """Charge les données des stations depuis le fichier JSON."""
    if not STATIONS_FILE.exists():
        return {}
    try:
        data = json.loads(STATIONS_FILE.read_text(encoding="utf-8"))
        return data
    except Exception:
        return {}


@app.get("/")
def root():
    """Point d'entrée de l'API."""
    return {
        "message": "Stations Météorologiques API",
        "version": "0.1.0",
        "endpoints": {
            "stations": "/stations",
            "station_details": "/stations/{station_id}",
            "docs": "/docs"
        }
    }


@app.get(
    "/stations",
    response_model=StationList,
    summary="Liste des identifiants de stations",
    responses={
        200: {
            "description": "Liste des identifiants de toutes les stations météorologiques",
            "content": {
                "application/json": {
                    "example": {
                        "stations": ["METEO_RENNES_01", "METEO_PARIS_01", "METEO_LYON_01"]
                    }
                }
            },
        }
    },
)
def get_stations():
    """Retourne la liste des identifiants de toutes les stations météorologiques."""
    stations_data = _load_stations()
    return {"stations": sorted(list(stations_data.keys()))}


@app.get(
    "/stations/{station_id}",
    response_model=StationSummary,
    summary="Détails d'une station météorologique",
    responses={
        200: {
            "description": "Détails complets de la station",
            "content": {
                "application/json": {
                    "example": {
                        "id": "METEO_RENNES_01",
                        "latitude_centre": 48.1173,
                        "longitude_centre": -1.6778,
                        "rayon_km": 15.0,
                        "temperature_actuelle": 12.5,
                        "precipitations_24h": 3.2
                    }
                }
            },
        },
        404: {"description": "Station non trouvée"},
    },
)
def get_station(station_id: str):
    """Renvoie les détails complets d'une station météorologique.
    
    — `station_id` doit correspondre exactement à un identifiant listé par `GET /stations`.
    """
    stations_data = _load_stations()
    if station_id not in stations_data:
        raise HTTPException(status_code=404, detail="Station not found")
    
    station = stations_data[station_id]
    return StationSummary(**station)
