from sys import argv
import numpy as np
from PIL import Image
import json

png = Image.open(argv[1])
arr = np.array(png)
lst = [[tuple(rgb[:3]) for rgb in row] for row in arr.tolist()]

with open(argv[2], 'w') as file:
    file.write(json.dumps(lst))