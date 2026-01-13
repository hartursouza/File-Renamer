import os


def get_desktop_path():
    """
    Retorna o caminho da Área de Trabalho do usuário,
    considerando ambientes com OneDrive.
    """
    home_path = os.path.expanduser("~")

    onedrive_desktop = os.path.join(home_path, "OneDrive", "Desktop")
    default_desktop = os.path.join(home_path, "Desktop")

    if os.path.exists(onedrive_desktop):
        return onedrive_desktop

    return default_desktop
