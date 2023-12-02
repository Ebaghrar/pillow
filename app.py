from PIL import Image, ImageDraw
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    image_path = create_image()
    return render_template('index.html', image_path=image_path)

def create_image():
    # Créer une image simple
    image = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(image)

    # Dessiner un rectangle rouge
    draw.rectangle([50, 50, 250, 250], outline="red", width=5)

    # Enregistrer l'image
    image_path = os.path.join(os.getcwd(), "static", "output_image.png")
    image.save(image_path)
    return image_path

if __name__ == "__main__":
    app.run(debug=True)
