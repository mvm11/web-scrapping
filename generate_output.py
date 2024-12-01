import os
from main import scrape_product_info

# URL del producto
url = "https://www.mercadolibre.com.co/impresora-simple-funcion-a-color-epson-ecotank-l121-110v/p/MCO24554271?pdp_filters=deal%3AMCO779366-1"

# Obtener datos del producto
product_info = scrape_product_info(url)

# Crear contenido HTML
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Información del Producto</title>
    <script src="https://cdn.jsdelivr.net/npm/tw-elements/dist/js/index.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tw-elements/dist/css/index.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/flowbite/1.6.5/flowbite.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/flowbite/dist/flowbite.min.css" rel="stylesheet" />
    <style>
        body {{
            background-color: #1f2937; /* Fondo oscuro */
            color: #f9fafb; /* Texto claro */
            font-family: 'Arial', sans-serif;
        }}
        h1, h2 {{
            color: #60a5fa; /* Azul claro */
        }}
        .card {{
            background-color: #374151; /* Gris oscuro */
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
    </style>
</head>
<body>
    <div class="container mx-auto p-4">
        <h1 class="text-3xl font-bold mb-4">Información del Producto</h1>
        <div class="card">
            <h2 class="text-2xl font-semibold">{product_info.get("title", "No disponible")}</h2>
            <p><strong>Precio:</strong> {product_info.get("price", "No disponible")}</p>
            <p><strong>Descripción:</strong> {product_info.get("description", "No disponible")}</p>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/tw-elements/dist/js/index.min.js"></script>
</body>
</html>
"""

# Guardar archivo HTML
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as file:
    file.write(html_content)

print("Archivo HTML generado en 'output/index.html'")
