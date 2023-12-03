from PIL import Image, ImageDraw
import os

def create_image():
    # Créer une image simple
    image = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(image)

    # Dessiner un rectangle rouge
    draw.rectangle([50, 50, 250, 250], outline="red", width=5)

   # Enregistrez l'image dans le répertoire '/tmp' par exemple
    image_path = os.path.join("/tmp", "output_image.png")
    image.save(image_path)
    return image_path

if __name__ == "__main__":
    image_path = create_image()
    print(f"Image créée avec succès : {image_path}")
