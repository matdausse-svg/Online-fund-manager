# Gestionnaire de cagnottes en ligne / Online Fund Manager

🇫🇷 [Français](#-français) · 🇬🇧 [English](#-english)

---

## 🇫🇷 Français

Application console en Python de gestion de cagnottes en ligne, avec comptes utilisateurs et sauvegarde des données.

**Contexte** : projet individuel réalisé en première année d'école d'ingénieur, au second semestre 2023, sur une durée de 2 mois.

### Fonctionnalités

- Inscription et connexion avec vérification des identifiants
- Création d'une cagnotte : nom, date, événement, cadeau prévu, participation libre ou fixe, nominative ou anonyme
- Ajout d'une liste de participants autorisés (détection des doublons d'adresse mail)
- Contribution d'un invité à une cagnotte via son adresse mail
- Gestion des commentaires, annulation et suppression de cagnottes
- Sauvegarde persistante des données dans des fichiers JSON

### Compétences mises en œuvre

Python · structures de données (listes, dictionnaires) · fonctions · manipulation de fichiers JSON · validation des saisies utilisateur · conception de menus interactifs

### Lancer le programme

Prérequis : Python 3, aucune bibliothèque externe (uniquement `os` et `json`, inclus avec Python).

```bash
python cagnotte_FR.py      # version française
python fund_manager_EN.py  # English version
```

Les fichiers de données (`.json`) sont créés automatiquement au premier lancement et mis à jour à la sortie du programme (choix « Sortir du site »).

### Fichiers

| Fichier | Description |
|---|---|
| `cagnotte_FR.py` | Version originale, en français |
| `fund_manager_EN.py` | Version anglaise (textes, variables et fonctions traduits, logique identique) |

### Pistes d'amélioration

- Remplacer les fichiers JSON par une base de données
- Découper le code en modules plus courts
- Ne pas stocker les mots de passe en clair

---

## 🇬🇧 English

Python console application for managing online funds (group gift pots), with user accounts and data persistence.

**Context**: individual project completed in the first year of engineering school, in the second semester of 2023, over a period of 2 months.

### Features

- Registration and login with credential checks
- Fund creation: name, date, event, planned gift, free or fixed contribution, named or anonymous
- List of authorised participants (duplicate email detection)
- Guest contribution to a fund via email address
- Comment management, cancellation and deletion of funds
- Persistent data storage in JSON files

### Skills applied

Python · data structures (lists, dictionaries) · functions · JSON file handling · user input validation · interactive menu design

### Running the program

Requirements: Python 3, no external library (only `os` and `json`, included with Python).

```bash
python cagnotte_FR.py      # French version
python fund_manager_EN.py  # English version
```

The data files (`.json`) are created automatically on first launch and saved when the program exits (choose "Exit the site").

### Files

| File | Description |
|---|---|
| `cagnotte_FR.py` | Original version, in French |
| `fund_manager_EN.py` | English version (text, variables and functions translated, same logic) |

### Possible improvements

- Replace the JSON files with a database
- Split the code into shorter modules
- Do not store passwords in plain text
