import unittest
from main import scrape_product_info, scrape_reviews

class TestScraper(unittest.TestCase):

    def test_scrape_product_info(self):
        url = "https://www.mercadolibre.com.co/impresora-simple-funcion-a-color-epson-ecotank-l121-110v/p/MCO24554271?pdp_filters=deal%3AMCO779366-1"
        result = scrape_product_info(url)
        self.assertIsInstance(result, dict, "La salida debe ser un diccionario")
        self.assertIn('title', result, "El diccionario debe contener la clave 'title'")
        self.assertIn('price', result, "El diccionario debe contener la clave 'price'")
        self.assertIn('description', result, "El diccionario debe contener la clave 'description'")

    def test_scrape_reviews(self):
        url = "https://www.mercadolibre.com.co/impresora-simple-funcion-a-color-epson-ecotank-l121-110v/p/MCO24554271?pdp_filters=deal%3AMCO779366-1"
        result = scrape_reviews(url)
        self.assertIsInstance(result, dict, "La salida debe ser un diccionario")
        self.assertIn('avg_rating', result, "El diccionario debe contener la clave 'avg_rating'")
        self.assertIn('num_reviews', result, "El diccionario debe contener la clave 'num_reviews'")
        self.assertIn('rating_counts', result, "El diccionario debe contener la clave 'rating_counts'")
        self.assertIn('positive_percentage', result, "El diccionario debe contener la clave 'positive_percentage'")
        self.assertIn('reviews', result, "El diccionario debe contener la clave 'reviews'")
        self.assertIsInstance(result['reviews'], list, "La clave 'reviews' debe contener una lista")

if __name__ == '__main__':
    unittest.main()
