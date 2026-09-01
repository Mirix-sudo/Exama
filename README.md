# Exama

Ce projet a été mis en place à partir de zéro en clonant le dépôt, en créant un environnement virtuel, en installant Django, puis en générant la structure du projet et de l'application Django.

## 1. Cloner le dépôt

```bash
git clone <repository-url>
cd Exama
```

## 2. Créer et activer un environnement virtuel

```bash
python -m venv env
```

Sous Windows :

```powershell
.\env\Scripts\Activate.ps1
```

## 3. Installer Django

```bash
pip install django
```

## 4. Créer le projet Django

Depuis la racine du dépôt :

```bash
django-admin startproject exama .
```

Cela crée le projet Django principal avec la structure par défaut :

```text
exama/
    manage.py
    exama/
        __init__.py
        settings.py
        urls.py
        wsgi.py
        asgi.py
```

## 5. Créer l'application

```bash
python manage.py startapp epreuves
```

Cela a créé le dossier de l'application :

```text
exama/
    epreuves/
        __init__.py
        admin.py
        apps.py
        migrations/
        models.py
        tests.py
        views.py
```

## 6. Enregistrer l'application dans le projet

La nouvelle application a été ajoutée au fichier de configuration Django dans `exama/exama/settings.py` dans la liste `INSTALLED_APPS`.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'epreuves',
]
```

## 7. Générer le fichier des dépendances

Pour suivre les packages installés, les dépendances de l'environnement ont été exportées :

```bash
pip freeze > requirements.txt
```

## 8. Lancer le serveur de développement

Pour vérifier que le projet fonctionne :

```bash
python manage.py migrate
python manage.py runserver
```

Ensuite, ouvrez l'URL locale de développement Django dans le navigateur :

```text
http://127.0.0.1:8000/
```

## Résumé du projet

Le projet a été initialisé avec Django, un environnement virtuel a été configuré, le projet `exama` a été créé, et l'application `epreuves` a été ajoutée pour commencer le développement de l'application.
