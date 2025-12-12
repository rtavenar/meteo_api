# Stations Météorologiques API

Petit projet Python pour exposer des données de stations météorologiques avec des zones de couverture géographiques.

Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Démarrage (local)

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Endpoints principaux

- `GET /stations` : liste des identifiants de toutes les stations météorologiques
- `GET /stations/{station_id}` : détails complets d'une station (position GPS, rayon de couverture, température actuelle, précipitations sur 24h)

La documentation interactive (OpenAPI/Swagger) est disponible après démarrage à `http://127.0.0.1:8000/docs`.

Structure des données

Chaque station possède :
- `id` : identifiant unique de la station
- `latitude_centre` : latitude du centre de la zone de couverture (en degrés)
- `longitude_centre` : longitude du centre de la zone de couverture (en degrés)
- `rayon_km` : rayon de la zone de couverture circulaire (en kilomètres)
- `temperature_actuelle` : température actuelle (en °C)
- `precipitations_24h` : précipitations sur les dernières 24 heures (en mm)

Notes

- Les données des stations sont stockées dans `data/stations.json`.
- L'API n'autorise que les identifiants de stations listés dans ce fichier.

