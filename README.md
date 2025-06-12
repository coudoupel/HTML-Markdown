#  HTML ⇄ Markdown Converter (Python CLI)

Ce projet propose un convertisseur **bidirectionnel entre HTML et Markdown**, écrit en Python pur, **sans dépendances externes**.

Il peut être utilisé en ligne de commande pour convertir des fichiers `.html` en `.md`, ou inversement.

---

##  Objectif

Permettre une conversion simple et fiable entre les formats HTML et Markdown, avec :
- une interface en ligne de commande
- un support de base des balises/structures courantes
- aucune bibliothèque externe requise (`html2text`, `markdown`, etc. ne sont pas utilisés)

---

##  Fonctionnalités

- Conversion **HTML → Markdown**
- Conversion **Markdown → HTML**
- Interface CLI (menu interactif)

---

##  Utilisation

1. **Lance le script** :
```bash
python convertisseur.py
```
Choisis une option dans le menu :


```bash
1. Convertir du HTML vers Markdown
2. Convertir du Markdown vers HTML
Saisis le chemin du fichier source.
```

Le fichier converti sera automatiquement créé dans le même dossier :

[nom du fichier]_converted.md ou [nom du fichier]_converted.html

## Exemple :

Le fichier exemple.html peux être utilisé pour réaliser une conversion html->Markdown.

exemple.html
```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Exemple HTML</title>
</head>
<body>
    <h1>Mon Projet</h1>

    <h2>Introduction</h2>
    <p>Bienvenue dans ce document de test HTML. Voici quelques exemples de syntaxe :</p>

    <h2>Mise en forme</h2>
    <p>Texte en <strong>gras</strong>, texte en <em>italique</em>, et un <a href="https://youtube.com">lien vers Youtube</a>.</p>

    <h2>Liste à puces</h2>
    <ul>
        <li>Élément un</li>
        <li>Élément deux</li>
        <li>Élément trois</li>
    </ul>

    <h2>Liste numérotée</h2>
    <ol>
        <li>Étape un</li>
        <li>Étape deux</li>
        <li>Étape trois</li>
    </ol>

    <h2>Code</h2>
    <p>Voici un bloc de code :</p>
    <pre><code>def hello():
    print("Bonjour le monde !")</code></pre>
</body>
</html>
```

Pour que le script fonctionne, on spécifie le chemin du fichier qui va être convertie
[![Image](https://i.goopics.net/ffjp45.png)](https://goopics.net/i/ffjp45)

Le fichier .md peux ensuite être affiché.

[![Image](https://i.goopics.net/5oihps.png)](https://goopics.net/i/5oihps)

Et inversement avec le fichier exemple.md qui peux être convertie en fichier.html

[![Image](https://i.goopics.net/p1hh2f.png)](https://goopics.net/i/p1hh2f)

Le fichier html peux ensuite être affiché sur une page web

[![Image](https://i.goopics.net/c3u6h6.png)](https://goopics.net/i/c3u6h6)

## Résumé

Ce script Python offre une solution légère et efficace pour convertir des fichiers HTML en Markdown, et inversement, sans nécessiter de dépendances externes. Il prend en charge les éléments de base du formatage et propose une interface en ligne de commande intuitive. 


