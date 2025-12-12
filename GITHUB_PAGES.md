# Publication sur GitHub Pages

Pour publier la documentation sur GitHub Pages :

## Méthode 1 : Configuration manuelle (recommandée)

1. **Commiter et pousser votre code** sur GitHub (branche `main` ou `master`)

2. **Aller dans les Settings de votre repository** :
   - Cliquez sur "Settings" dans le menu du repository
   - Allez dans la section "Pages" (dans le menu de gauche)

3. **Configurer la source** :
   - Sous "Source", sélectionnez "Deploy from a branch"
   - Choisissez la branche `main` (ou `master`)
   - Sélectionnez le dossier `/docs`
   - Cliquez sur "Save"

4. **Attendre quelques minutes** pour que GitHub Pages se déploie

5. **Accéder à votre documentation** :
   - L'URL sera : `https://[votre-username].github.io/[nom-du-repo]/`
   - Par exemple : `https://rtavenar.github.io/meteo_api/`

## Méthode 2 : GitHub Actions (automatique)

Si vous avez créé le fichier `.github/workflows/pages.yml`, la documentation sera automatiquement déployée à chaque push sur la branche `main` qui modifie le dossier `docs/`.

Dans ce cas :
1. Commiter et pousser le code
2. Aller dans Settings → Pages
3. Sélectionner "GitHub Actions" comme source
4. La documentation sera automatiquement déployée

## Vérification

Pour vérifier que tout fonctionne :
- La documentation Markdown sera convertie en HTML par Jekyll
- Les liens et le formatage seront préservés
- La page sera accessible publiquement

## Notes

- La première publication peut prendre quelques minutes
- Les modifications ultérieures sont généralement déployées en moins d'une minute
- Jekyll supporte nativement le Markdown, donc votre fichier `docs/index.md` sera automatiquement rendu

