from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
import yaml

def create_notebook(path: Path, n_name: str):
    '''
    Creates a notebook (notebook.md).
    Params:
        - path: rute from the dir
        - n_name: name of the notebook
    Returns
        None
    '''
    file = path / f'{n_name}.md'
    file.touch()

def write_in_note_book(file_path: Path, text: str):
    '''
    Write text in the given file.
    Params:
        - file_path: path of the file
        - text: the text to add in the file
    Returns:
        None
    '''
    with open(file_path, "a+") as f:
        f.write('\n' + text )

def render_template(template_path: Path,f_name: str, file_path: Path, context):
    '''
    Render a jinja template and returns a markdown text.
    Params:
        - template_path: the path of the jinja template.
        - file_path: the output path.
        - context: the context to render the tamplate.
    Returns:
        - Markdown: the text resulting of the template rendering.
    '''
    content = read_template(template_path,f_name,context)
    with open(file_path, 'w') as f:
        f.write(content)

def read_template(template_path: Path, f_name, context):
    environment = Environment(loader=FileSystemLoader(template_path))
    template = environment.get_template(f'{f_name}.jinja')
    content = template.render(context)
    return content
    

def load_yaml(config_path):
    '''
    Resive and a yaml file_path and returns the content
    '''
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f) # el safe loada nos siver para llamar un archivo que solo tiene un bloque yml
    return config

def main():
    rute = Path('/home/dracul/programing/python/guis/generador_notas/')
    # create_notebook(rute, 'Prueba')
    # text = '# Titulo de prueba'
    # write_in_note_book(rute / 'Prueba.md', text)
    # today = date.today()
    # today = today.__format__('%d-%m-%Y')
    # render_template(rute / 'templates','cuaderno',rute / 'source/Prueba.md',{'fecha':today, 'tema': 'Prueba'})
    data = load_yaml(rute / 'source/c_prueba.yaml')
    data['author'] = 'mi verga'
    print(data)

if __name__ == "__main__":
    main()
