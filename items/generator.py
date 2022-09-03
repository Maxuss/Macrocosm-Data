import os
from concurrent.futures import ThreadPoolExecutor
from urllib import request

import requests
from PIL import Image


def generate():
    """
    Generates high resolution 150x150 minecraft item textures
    :return: void
    """
    if not os.path.exists("temp"):
        os.mkdir("temp")
    if not os.path.exists("generated"):
        os.mkdir("generated")

    textures = requests.get("https://raw.githubusercontent.com/InventivetalentDev/minecraft-assets/1.19.2/assets"
                            "/minecraft/textures/item/_list.json").json()
    with ThreadPoolExecutor(32) as pool:
        pool.map(generate_single, textures["files"])


def generate_single(name: str):
    """
    Modifies a single minecraft image
    :param name: name of file to modify
    :return: void
    """
    print(f"Modifying {name}")
    request.urlretrieve("https://raw.githubusercontent.com/InventivetalentDev/minecraft-assets/1.19.2/assets/"
                        f"minecraft/textures/item/{name}", f"temp/{name}")
    texture = Image.open(f"temp/{name}")
    resized = texture.resize((150, 150), 0)
    resized.save(f"generated/{name}")
    os.remove(f"temp/{name}")


if __name__ == "__main__":
    generate()
