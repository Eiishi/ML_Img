# Projet OpenClassrooms "Classez des images à l'aide d'algorithmes de Deep Learning"
### Sana TAYS

Le but de ce projet est de créer un algorithme capable de prendre une image de chien en entrée et de détecter automatiquement la race de celui-ci.

L'algorithme utilisé ici est un réseau de neurones convolutif dont certains hyperparamètres ont été optimisés. Le modèle pré-entraîné est disponible dans le fichier 'model.h5'.

Ce répertoire contient notamment :

- un fichier app.py à exécuter
- le modèle pré-entraîné model.h5
- un fichier requirements.txt contenant les dépendances à installer
- un dossier data_raw contenant les images du jeu de données

___

Afin de pouvoir utiliser l'algorithme, voici la marche à suivre :

- Téléchargez le code de ce répertoire (soit via une commande `git clone` soit en téléchargement direct)
- Ouvrez une ligne de commande et naviguez jusqu'au dossier créé
- Créez un environnement virtuel conda ou venv (optionnel mais conseillé)
- Tapez la commande `pip install requirements.txt` afin d'installer tous les modules nécessaires au fonctionnement de l'algorithme
- Tapez la commande `python app.py`

Si tout fonctionne, vous voyez s'afficher dans votre terminal une URL où l'app est maintenant active. Ouvrez celle-ci dans votre navigateur, et vous pouvez maintenant déposer une image de chien et demander l'estimation.

Bonne utilisation !