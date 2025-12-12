---
title: Documentation de l'API Stations Météorologiques
layout: default
---

# Documentation de l'API Stations Météorologiques

Bienvenue — cette documentation décrit l'API fournie par le service pour consulter les données des stations météorologiques.

## Endpoints principaux

- `GET /stations`
  - Description : retourne la liste des identifiants de toutes les stations météorologiques.
  - Réponse (200) : JSON avec la clé `stations` (liste d'identifiants de stations).
  - Exemple :

    ```
    https://meteo-api-vcvp.onrender.com/stations
    ```

- `GET /stations/{station_id}`
  - Description : retourne les détails complets d'une station météorologique.
  - Paramètre : `station_id` doit être exactement un identifiant de station listé par `GET /stations`.
  - Réponse (200) : JSON décrivant les détails de la station (voir section ci-dessous).
  - Erreurs : 404 si la station n'existe pas.
  - Exemple :

    ```
    https://meteo-api-vcvp.onrender.com/stations/METEO_RENNES_01
    ```


## Schéma de réponse pour `GET /stations/{station_id}` (champs exposés)

- `id` : identifiant unique de la station (string)
- `latitude_centre` : latitude du centre de la zone de couverture en degrés (float)
- `longitude_centre` : longitude du centre de la zone de couverture en degrés (float)
- `rayon_km` : rayon de la zone de couverture circulaire en kilomètres (float)
- `temperature_actuelle` : température actuelle en degrés Celsius (float)
- `precipitations_24h` : précipitations sur les dernières 24 heures en millimètres (float)

Remarque : chaque station possède une zone de couverture circulaire définie par sa position GPS (latitude_centre, longitude_centre) et son rayon_km. Pour vérifier si une position GPS est couverte par une station, calculez la distance entre la position et le centre de la station, puis comparez-la au rayon_km.

