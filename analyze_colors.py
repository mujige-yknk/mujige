from PIL import Image
from collections import Counter

img = Image.open(r'C:\Users\daich\gitrepo\yakiniku-hp\IMG_2654.jpeg').convert('RGB')
w, h = img.size
colors = Counter()
for x in range(0, w, 20):
    for y in range(0, h, 20):
        colors[img.getpixel((x, y))] += 1
for color, count in colors.most_common(12):
    print(color, count)
