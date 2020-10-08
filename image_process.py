import sys
import os

from PIL import Image, ImageFilter
from pathlib import Path

first = sys.argv[1]
second = sys.argv[2]

if not Path(second).is_dir():
    os.mkdir(second)

with os.scandir(first) as myfile:
    for i in myfile:
        img = Image.open(f'{first}{i.name}')
        img.save(f'{second}{i.name[:-4]}.png','png')
