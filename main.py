import requests
from bs4 import BeautifulSoup
from collections import Counter

# Encabezados para simular un navegador real
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def scrape_reviews(url):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Calificación promedio
        avg_rating_tag = soup.find('p', class_='ui-review-capability__rating__average')
        avg_rating = avg_rating_tag.text.strip() if avg_rating_tag else "No disponible"

        # Número de calificaciones
        num_reviews_tag = soup.find('p', class_='ui-review-capability__rating__label')
        num_reviews = num_reviews_tag.text.strip() if num_reviews_tag else "No disponible"

        reviews = []
        # Seleccionar todos los artículos que contienen comentarios
        review_elements = soup.find_all('article', class_='ui-review-capability-comments__comment')

        for element in review_elements:
            # Calificación individual
            rating_tag = element.find('p', class_='andes-visually-hidden')
            rating_text = rating_tag.text.strip() if rating_tag else "No disponible"
            rating_value = int(rating_text.split()[1]) if "Calificación" in rating_text else 0

            # Fecha de la reseña
            date_tag = element.find('span', class_='ui-review-capability-comments__comment__date')
            review_date = date_tag.text.strip() if date_tag else "No disponible"

            # Texto de la reseña
            review_tag = element.find('p', class_='ui-review-capability-comments__comment__content')
            review_text = review_tag.text.strip() if review_tag else "No disponible"

            # Sentimiento basado en calificación
            sentiment = 'Positiva' if rating_value >= 4 else 'Negativa'

            reviews.append({
                'rating': rating_value,
                'review': review_text,
                'date': review_date,
                'sentiment': sentiment
            })

        # Contar distribuciones de calificaciones
        rating_counts = Counter([review['rating'] for review in reviews])
        positive_reviews = sum(1 for review in reviews if review['sentiment'] == 'Positiva')
        positive_percentage = (positive_reviews / len(reviews)) * 100 if reviews else 0

        return {
            'avg_rating': avg_rating,
            'num_reviews': num_reviews,
            'rating_counts': rating_counts,
            'positive_percentage': positive_percentage,
            'reviews': reviews
        }

    except Exception as e:
        print("Error al extraer datos:", e)
        return {
            'avg_rating': "No disponible",
            'num_reviews': "No disponible",
            'rating_counts': {},
            'positive_percentage': 0,
            'reviews': []
        }



def scrape_product_info(url):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        title_tag = soup.find('h1', class_='ui-pdp-title')
        price_tag = soup.find('span', class_='andes-money-amount__fraction')
        description_tag = soup.find('p', class_='ui-pdp-description__content')

        title = title_tag.text.strip() if title_tag else "No disponible"
        price = price_tag.text.strip() if price_tag else "No disponible"
        description = description_tag.text.strip() if description_tag else "No disponible"

        return {
            'title': title,
            'price': price,
            'description': description
        }

    except requests.exceptions.RequestException as e:
        print("Error al hacer la solicitud:", e)
        return None
    except AttributeError as e:
        print("Error al extraer información del producto:", e)
        return None

# URL de ejemplo
url = "https://www.mercadolibre.com.co/impresora-simple-funcion-a-color-epson-ecotank-l121-110v/p/MCO24554271?pdp_filters=deal%3AMCO779366-1"

# Obtener la información del producto
product_info = scrape_product_info(url)

# Obtener las reseñas
reviews_data = scrape_reviews(url)

# Mostrar los resultados
if product_info:
    print(f"Título: {product_info['title']}")
    print(f"Precio: {product_info['price']}")
    print(f"Descripción: {product_info['description']}")

if reviews_data:
    print(f"\nCalificación promedio: {reviews_data['avg_rating']}")
    print(f"Número de calificaciones: {reviews_data['num_reviews']}")
    print(f"Distribución de calificaciones: {reviews_data.get('rating_counts', 'No disponible')}")
    print(f"Porcentaje de opiniones positivas: {reviews_data.get('positive_percentage', 0):.2f}%")

    print("\nOpiniones destacadas:")
    for review in reviews_data['reviews']:
        print(f"Fecha: {review['date']}")
        print(f"Calificación: {review['rating']}")
        print(f"Sentimiento: {review['sentiment']}")
        print(f"Reseña: {review['review']}\n")