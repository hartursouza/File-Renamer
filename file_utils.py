import os


def get_unique_filename(folder: str, filename: str) -> str:
    """
    Retorna um nome de arquivo único no padrão do Windows:
    arquivo.ext
    arquivo (2).ext
    arquivo (3).ext
    ...
    """
    name, ext = os.path.splitext(filename)
    candidate = filename
    counter = 2

    while os.path.exists(os.path.join(folder, candidate)):
        candidate = f"{name} ({counter}){ext}"
        counter += 1

    return candidate
