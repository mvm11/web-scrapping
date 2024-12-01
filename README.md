# Evidencia de aprendizaje 3: Optimización de procesos de desarrollo

**Autores:**  
Cruz Magdalena Vanegas Correa  
Mateo Valencia Minota  

**Curso:**  
Programación para Análisis de Datos  

**Grupo:**  
PREICA2402B020101  

**Docente:**  
Andrés Felipe Palacio  

**Lugar y Fecha:**  
Medellín - Antioquia  
30/11/2024  

---

## Introducción

La automatización de procesos de desarrollo y despliegue es fundamental para optimizar el ciclo de vida del software. En esta evidencia de aprendizaje, se implementó un flujo de trabajo utilizando GitHub Actions para integrar pipelines de integración continua (CI) y entrega continua (CD). Estas herramientas permitieron automatizar tareas clave como la ejecución de pruebas y el despliegue de una aplicación web que extrae datos de un producto específico en Mercado Libre mediante técnicas de web scraping. Este proyecto consolidó habilidades técnicas en automatización, despliegue y análisis de datos en entornos reales.

---

## Descripción de la página y artículo a analizar

Mercado Libre es una de las plataformas de comercio electrónico más grandes en América Latina, ofreciendo productos en una variedad de categorías. Para este proyecto, se seleccionó la página del producto **"Impresora simple función a color Epson EcoTank L121 110V"** como objeto de análisis.

### Detalles del producto:
- **Nombre:** Impresora simple función a color Epson EcoTank L121 110V  
- **Marca:** Epson  
- **Modelo:** EcoTank L121  
- **Voltaje:** 110V  
- **Color:** Negro  

### Características principales:
- Impresión a color mediante tecnología de inyección de tinta.  
- Capacidad máxima de 100 hojas.  
- Soporta tamaños de papel hasta 215.9 mm x 1.200 mm.  
- Incluye botellas de tinta para recarga.  
- Conectividad a través de puerto USB.  
- Impresión doble faz manual.  

---

## Objetivos

1. Diseñar e implementar un flujo de trabajo DevOps eficiente, integrando control de versiones con Git y automatización mediante GitHub Actions.
2. Crear pipelines de integración continua (CI) que ejecuten pruebas unitarias para garantizar la calidad del código.
3. Configurar pipelines de entrega continua (CD) para desplegar automáticamente la aplicación web en GitHub Pages.
4. Automatizar la extracción de datos del producto seleccionado mediante web scraping usando BeautifulSoup y Requests.
5. Documentar todo el proceso en un repositorio público de GitHub, destacando los aspectos técnicos y los resultados obtenidos.

---

## Metodología

1. **Desarrollo del scraper:** Se utilizó Python con las librerías `BeautifulSoup` y `Requests` para extraer información del producto en Mercado Libre, como el título, precio, descripción y opiniones.
2. **Configuración de GitHub Actions:** Se crearon dos archivos `.yml`:
   - `ci.yml`: Ejecuta pruebas unitarias para validar la funcionalidad del código.
   - `cd.yml`: Despliega automáticamente la aplicación en GitHub Pages.
3. **Automatización del despliegue:** Se generó un archivo HTML con los datos obtenidos mediante el scraper, alojado en el directorio `output`, que se publica automáticamente en GitHub Pages.
4. **Pruebas:** Se desarrollaron pruebas unitarias para validar la funcionalidad del scraper y garantizar su correcto funcionamiento en los pipelines de CI/CD.
5. **Documentación:** Se registraron los pasos y resultados en este repositorio, asegurando una estructura clara y profesional.

---

## Resultados

El proyecto culminó con éxito, logrando:
- La automatización de la extracción y análisis de datos del producto seleccionado.
- La implementación de pipelines de CI/CD funcionales que garantizan la calidad y el despliegue continuo.
- La publicación de los resultados en GitHub Pages, accesibles desde [este enlace](https://mvm11.github.io/web-scrapping/).

---

## Conclusiones

1. GitHub Actions es una herramienta poderosa para automatizar procesos clave en el desarrollo de software, como la ejecución de pruebas y el despliegue continuo.
2. El uso de librerías como `BeautifulSoup` y `Requests` permite implementar soluciones eficaces para la extracción y análisis de datos.
3. La documentación y estructuración del proyecto en un repositorio público mejora la colaboración y facilita su mantenimiento.
4. Este ejercicio fortaleció competencias en DevOps, scraping y despliegue web, mostrando la importancia de integrar herramientas modernas en el ciclo de desarrollo.

---

## Bibliografía

- BeautifulSoup Documentation. (n.d.). *BeautifulSoup: We called him Tidy.* Retrieved from [https://www.crummy.com/software/BeautifulSoup/](https://www.crummy.com/software/BeautifulSoup/)
- GitHub Actions Documentation. (n.d.). *Automate, customize, and execute your software development workflows right in your repository.* Retrieved from [https://docs.github.com/actions](https://docs.github.com/actions)
- Requests Documentation. (n.d.). *Requests: HTTP for Humans.* Retrieved from [https://docs.python-requests.org/](https://docs.python-requests.org/)
- Python Software Foundation. (n.d.). *unittest — Unit testing framework.* Retrieved from [https://docs.python.org/3/library/unittest.html](https://docs.python.org/3/library/unittest.html)
- Peaceiris. (n.d.). *GitHub Pages Deploy Action.* Retrieved from [https://github.com/peaceiris/actions-gh-pages](https://github.com/peaceiris/actions-gh-pages)
