from PIL import Image
from collections import Counter

def rgb_to_col(image_entree, image_sortie):
    img = Image.open(image_entree)
    pixels = img.load()

    largeur, hauteur = img.size

    couleurs = []
    for y in range(hauteur):
        for x in range(largeur):
            couleurs.append(pixels[x, y])
    couleur_dominante = Counter(couleurs).most_common(1)[0][0]

    for y in range(hauteur):
        for x in range(largeur):
            r, g, b = pixels[x, y]


            if (r, g, b) == couleur_dominante:
                continue

            voisin_blanc = False
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue

                    nx, ny = x + dx, y + dy
                    if 0 <= nx < largeur and 0 <= ny < hauteur:
                        nr, ng, nb = pixels[nx, ny]

                        if (nr, ng, nb) == couleur_dominante:
                            voisin_blanc = True
                            break
                if voisin_blanc:
                    break

            if voisin_blanc:
                pixels[x, y] = (255, 0, 0)


    img.save(image_sortie)
    print("Image convertie :", image_sortie)

rgb_to_col("noel.jpg", "noel_contour.png")