# MLProject - Diabetes Predictor

Cette application Streamlit prédit la probabilité de diabète à partir de quelques paramètres médicaux.

## Contenu

- `app.py` : application Streamlit pour saisir les données et afficher la prédiction.
- `diabetes_model.pkl` : modèle entraîné utilisé par l'application.
- `Diabetes_Predict.ipynb` : notebook Jupyter utilisé pour l'analyse et la construction du modèle.

## Installation

1. Créez un environnement virtuel :
   ```bash
   python -m venv venv
   ```
2. Activez l'environnement :
   - Windows : `venv\Scripts\activate`
   - macOS/Linux : `source venv/bin/activate`
3. Installez les dépendances :
   ```bash
   pip install streamlit pandas scikit-learn
   ```

## Utilisation

Lancez l'application Streamlit :

```bash
streamlit run app.py
```

Puis ouvrez le lien affiché dans votre navigateur.

## Fichiers à ignorer

Le dossier `venv/`, les fichiers Python compilés et les checkpoints Jupyter sont exclus du dépôt.
