from PIL import Image 

def convertir_noir_blanc(nom_fichier, nom_sortie):

    img = Image.open(nom_fichier).convert("RGB")
    
    largeur, hauteur = img.size
    bw_img = Image.new("L", (largeur, hauteur))  
    
    for x in range(largeur):
        for y in range(hauteur):
            r, g, b = img.getpixel((x, y))
            gray = (r + g + b) // 3  
            bw_img.putpixel((x, y), gray)
    
    bw_img.save(nom_sortie)
    print(f"✔ Image convertie en noir et blanc : {nom_sortie}")

convertir_noir_blanc("noelhi.jpg", "noelhi_bw.jpg")
