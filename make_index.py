#!/usr/bin/env python3
import os

def create_index_html(path):
    with open(os.path.join(path, 'index.html'), 'w') as index_file:
        index_file.write('<html>\n')
        index_file.write('<body>\n')
        index_file.write('<ul>\n')

        for name in sorted(os.listdir(path)):
            # Skip .git directories and index.html files
            if name == ".git" or name == "index.html" or name == "make_index.py" or name == "_headers":
                continue

            full_path = os.path.join(path, name)
            if os.path.isdir(full_path):
                create_index_html(full_path)
                index_file.write(f'<li><a href="{name}/index.html">{name}/</a></li>\n')
            else:
                index_file.write(f'<li><a href="{name}">{name}</a></li>\n')

        index_file.write('</ul>\n')
        index_file.write('</body>\n')
        index_file.write('</html>\n')

if __name__ == "__main__":
    create_index_html('.')
