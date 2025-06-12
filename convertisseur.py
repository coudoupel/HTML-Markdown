
import re
from html.parser import HTMLParser
import os

class HTMLToMarkdownParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.output = ''
        self.href = None
        self.current_tags = []
        self.list_level = 0
        self.in_code_block = False

    def handle_starttag(self, tag, attrs):
        self.current_tags.append(tag)
        if tag == 'br':
            self.output += '  \n'
        elif tag == 'p':
            self.output += '\n\n'
        elif tag.startswith('h') and tag[1:].isdigit():
            self.output += '\n\n' + '#' * int(tag[1]) + ' '
        elif tag in ('strong', 'b'):
            self.output += '**'
        elif tag in ('em', 'i'):
            self.output += '*'
        elif tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.href = attr[1]
        elif tag in ('ul', 'ol'):
            self.list_level += 1
        elif tag == 'li':
            indent = '  ' * (self.list_level - 1)
            bullet = '*' if 'ul' in self.current_tags else '1.'
            self.output += f'\n{indent}{bullet} '
        elif tag == 'pre':
            self.output += '\n\n```'
            self.in_code_block = True
        elif tag == 'code' and self.in_code_block:
            self.output += 'python\n'

    def handle_endtag(self, tag):
        if tag in ('strong', 'b'):
            self.output += '**'
        elif tag in ('em', 'i'):
            self.output += '*'
        elif tag == 'a' and self.href:
            self.output += f']({self.href})'
            self.href = None
        elif tag in ('ul', 'ol'):
            self.list_level -= 1
        elif tag == 'pre':
            self.output += '\n```\n'
            self.in_code_block = False
        if tag in self.current_tags:
            self.current_tags.remove(tag)

    def handle_data(self, data):
        if 'a' in self.current_tags and self.href:
            self.output += f'[{data}'
        else:
            self.output += data

    def get_markdown(self):
        return self.output.strip()


def html_to_markdown(html):
    parser = HTMLToMarkdownParser()
    parser.feed(html)
    return parser.get_markdown()


def markdown_to_html(md):
    html = md

    # Bloc de code ```lang
    html = re.sub(r'```(\w+)?\n(.*?)```',
                  lambda m: f"<pre><code>{m.group(2)}</code></pre>",
                  html, flags=re.DOTALL)

    html = re.sub(r'###### (.*)', r'<h6>\1</h6>', html)
    html = re.sub(r'##### (.*)', r'<h5>\1</h5>', html)
    html = re.sub(r'#### (.*)', r'<h4>\1</h4>', html)
    html = re.sub(r'### (.*)', r'<h3>\1</h3>', html)
    html = re.sub(r'## (.*)', r'<h2>\1</h2>', html)
    html = re.sub(r'# (.*)', r'<h1>\1</h1>', html)
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', html)
    html = html.replace('  \n', '<br>\n')
    html = re.sub(r'(?m)^\s*\*\s+(.*)', r'<ul><li>\1</li></ul>', html)
    html = re.sub(r'(?m)^\s*1\.\s+(.*)', r'<ol><li>\1</li></ol>', html)

    lines = html.split('\n')
    new_lines = []
    for line in lines:
        if line.strip() and not re.match(r'<(h\d|ul|ol|li|br|a|strong|em|pre|code)>', line.strip()):
            new_lines.append(f'<p>{line.strip()}</p>')
        else:
            new_lines.append(line)
    html = '\n'.join(new_lines)
    html = re.sub(r'(</ul>\s*<ul>)', '', html)
    html = re.sub(r'(</ol>\s*<ol>)', '', html)
    return html.strip()


def main():
    print("=== Convertisseur HTML ↔ Markdown ===")
    while True:
        print("\nQue veux-tu faire ?")
        print("1. Convertir du HTML vers Markdown (depuis un fichier)")
        print("2. Convertir du Markdown vers HTML (depuis un fichier)")
        print("3. Quitter")
        choice = input("Ton choix (1/2/3) : ").strip()

        if choice in ('1', '2'):
            file_path = input("\nChemin du fichier à lire : ").strip()
            if not os.path.isfile(file_path):
                print("Fichier introuvable.")
                continue

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            if choice == '1':
                result = html_to_markdown(content)
                out_path = file_path.rsplit('.', 1)[0] + '_converted.md'
            else:
                result = markdown_to_html(content)
                out_path = file_path.rsplit('.', 1)[0] + '_converted.html'

            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(result)

            print(f"\n Conversion terminée ! Résultat écrit dans : {out_path}")

        elif choice == '3':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Réessaie.")

if __name__ == "__main__":
    main()
