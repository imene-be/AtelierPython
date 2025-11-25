from PIL import Image
import random

def noir_en_couleur_random(nom_fichier, nom_sortie):
    img = Image.open(nom_fichier).convert("L")
    largeur, hauteur = img.size
    
    color_img = Image.new("RGB", (largeur, hauteur))
    
    for x in range(largeur):
        for y in range(hauteur):
            gray = img.getpixel((x, y))
            
            if gray < 60:          # très sombre
                r = random.randint(30, 70)
                g = random.randint(20, 50)
                b = random.randint(10, 40)
            elif gray < 120:       # sombre
                r = random.randint(100, 150)
                g = random.randint(60, 100)
                b = random.randint(40, 80)
            elif gray < 180:       # clair
                r = random.randint(180, 220)
                g = random.randint(150, 200)
                b = random.randint(130, 180)
            else:                  # très clair
                r = random.randint(230, 255)
                g = random.randint(220, 255)
                b = random.randint(210, 255)
            
            color_img.putpixel((x, y), (r, g, b))
    
    color_img.save(nom_sortie)
    print(f"✔ Image convertie en couleur aléatoire : {nom_sortie}")

noir_en_couleur_random("grenouille_bw.jpg", "grenouille_color_random.jpg")
