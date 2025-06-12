import html2text
import sys
import os

def html_file_to_markdown(input_path, output_path=None):
    # Lire le contenu HTML
    with open(input_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Convertir HTML en Markdown
    markdown_content = html2text.html2text(html_content)

    # Déterminer le chemin de sortie
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".md"

    # Écrire le Markdown
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    print(f"Markdown généré : {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python html_to_markdown.py fichier.html [fichier.md]")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        html_file_to_markdown(input_file, output_file)
