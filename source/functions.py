from pathlib import Path

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
        f.write(text + '\n')

def render_template(template_path: Path, file_path: Path, context):
    '''
    Render a jinja template and returns a markdown text.
    Params:
        - template_path: the path of the jinja template.
        - file_path: the output path.
        - context: the context to render the tamplate.
    Returns:
        - Markdown: the text resulting of the template rendering.
    '''
    pass

def main():
    rute = Path('/home/dracul/programing/python/guis/generador_notas/source/')
    # create_notebook(rute, 'Prueba')
    text = '# Titulo de prueba'
    write_in_note_book(rute / 'Prueba.md', text)

if __name__ == "__main__":
    main()
