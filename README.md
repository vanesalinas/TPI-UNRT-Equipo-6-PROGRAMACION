TPI-UNRT-Equipo-6
# <p align=center>Proyecto "SmartRoast S.A."<br>Experiencia del Usuario Final</p>

## 1. Contexto del negocio

**SmartRoast S.A.** es una empresa global de tecnología e integración logística B2B2C (Business-to-Business-to-Consumer) enfocada en el nicho del café de especialidad. Su modelo de negocio se basa en unificar y trazar toda la cadena de valor del café: desde que la cereza se cosecha en las fincas de altura, pasando por los tostaderos y redes de distribución internacionales, hasta llegar a la taza del consumidor final.

La gerencia ha decidido desarrollar "SmartRoast Core", un ecosistema digital integral que solucione los problemas de la industria del cafe desde el origen de la produccion hasta la llegada al publico.

El módulo desarrollado por el Equipo 6 interviene en el último eslabón de esa cadena: **la experiencia del usuario final en su hogar.**

---

## 2. ¿Qué es el café de especialidad?

El **café de especialidad** es la categoría de mayor calidad dentro de la industria, es aquel que obtiene **80 puntos o más sobre 100** en la escala de evaluación de la [Specialty Coffee Association (SCA)](https://sca.coffee). Solo entre el 5% y el 10% de todo el café producido en el mundo alcanza ese puntaje.

Lo que lo hace diferente del café de supermercado no es solo el sabor — es la **trazabilidad**. Cuando comprás un café de especialidad, sabés de qué país viene, de qué región, de qué finca, qué variedad botánica es y cómo fue procesado después de la cosecha. Cada uno de esos factores influye directamente en lo que vas a sentir en la taza.

### Los perfiles que trabaja este proyecto

Los 8 cafés del catálogo provienen de tostaderías argentinas reales con trazabilidad completa:

| # | Café | Tostadería[^1][^2] | Origen | Proceso | SCA | Notas de sabor |
|---|------|-----------|--------|---------|-----|----------------|
| 1 | Kenia SL28 — Embu | Café Cumbal (Mendoza) | Embu, Kenia | Lavado | 85 | Té negro, pomelo, vainilla |
| 2 | Colombia Caturra — Honey | Café Cumbal (Mendoza) | Huila, Colombia | Honey | 84.75 | Chocolate, caramelo, cítrico, miel |
| 3 | Etiopía Heirloom — Oromia | Café Cumbal (Mendoza) | Oromia, Etiopía | Lavado | 84 | Cacao, pasas, especias rojas |
| 4 | El Salvador Montealegre | John & Joe (Buenos Aires) | Volcán Tecapa, El Salvador | Natural | 85 | Piña, uva roja, dátiles, dulzor marcado |
| 5 | Colombia Supremo | John & Joe (Buenos Aires) | Nariño, Huila, Antioquia | Lavado | 85 | Almendras tostadas, chocolate, suave |
| 6 | Brazil Santos Cerrado | John & Joe (Buenos Aires) | Cerrado Mineiro, Brasil | Natural | 84 | Frutos secos, chocolate, gran cuerpo |
| 7 | Bolivia Yanaloma | John & Joe (Buenos Aires) | Apolo, La Paz | Lavado | 84.5 | Chocolate suave, frutos secos, manjar |
| 8 | Brazil Amarelo Santos | John & Joe (Buenos Aires) | Brejetuba, Espíritu Santo | Lavado | 85 | Frutilla, mora, azúcar mascabo |

> 💡 **¿Qué es el proceso?** Después de cosechar la cereza de café, hay distintas formas de separar el grano de la fruta. El **proceso natural** seca la cereza entera, lo que genera sabores frutales intensos. El **lavado** remueve toda la pulpa antes de secar, produciendo tazas limpias y de alta acidez. El **honey** es un punto intermedio: retiene parte del mucílago, aportando dulzura sin los sabores fermentados del natural.

[^1]: [cafecumbal.ar](https://cafecumbal.ar/tienda-online/)
[^2]: [johnandjoe.com.ar](https://johnandjoe.com.ar/productos1/)

---

## 3. ¿Cómo se prepara el café de especialidad?

El método de preparación define cómo el agua extrae los compuestos solubles del grano.

Las tres variables que siempre hay que tener en cuenta son:

- **Ratio** — cuántos gramos de café por mililitro de agua
- **Temperatura** — el agua no debe hervir; lo ideal es entre 90 y 96 °C
- **Molienda** — el grosor del molido depende del método.

Un error en cualquiera de estas variables arruina incluso el mejor grano.

### Prensa Francesa

La forma más simple de hacer un gran café en casa. El café y el agua conviven juntos durante 4 minutos, sin filtro de papel, lo que preserva todos los aceites naturales del grano y produce una taza de cuerpo pleno y textura sedosa.

- Molienda gruesa · 93–96 °C · 4 min · Ratio 1:15

### V60 / Pour Over

El método favorito de los baristas para mostrar la complejidad de un café. El agua pasa a través del grano por gravedad usando un filtro de papel, produciendo una taza limpia, brillante y llena de matices aromáticos. Ideal para cafés de origen africano.

- Molienda media-fina · 90–94 °C · 2:30–3:30 min · Ratio 1:16

### Aeropress

El método más versátil y tolerante a errores. Combina inmersión y presión manual, permitiendo preparar desde algo similar a un espresso hasta un filtrado suave. Muy recomendado para quienes se inician en el café de especialidad.

- Molienda media · 80–96 °C · 1–2 min · Ratio 1:10 a 1:16

### Espresso

Extracción rápida a alta presión. En 25–30 segundos, 9 bares de presión fuerzan el agua a través de un disco compacto de café muy fino, produciendo una bebida concentrada con crema. Es la base del cappuccino, el latte y el flat white. Requiere máquina específica.

- Molienda muy fina · 90–96 °C · 25–30 seg · Ratio 1:2

<br>

> [!TIP]
> **Regla clave de molienda:** a mayor tiempo de contacto agua-café, molienda más gruesa. Molienda incorrecta para el método es la causa más común de una mala taza, independientemente de la calidad del grano.
---

## 4. El problema de negocio identificado

SmartRoast vende café de excelente calidad. Pero cuando ese café llega a manos del consumidor, pasan dos cosas frecuentemente:

**1. No saben qué café elegir.** La variedad es abrumadora. Distintos orígenes, procesos, niveles de tueste y perfiles de sabor. Sin orientación, la gente elige al azar — y puede terminar con un café que no va con sus gustos.

**2. No saben cómo prepararlo.** Incluso eligiendo el café correcto, si se prepara con agua hirviendo, molienda equivocada o demasiado tiempo de extracción, la experiencia será mala. Y la culpa, injustamente, cae sobre la marca.

Esto genera insatisfacción, clientes que no vuelven y una reputación que se daña — no por la calidad del producto, sino por la falta de educación al consumidor.

---

## 5. Solución propuesta

Este repositorio contiene dos módulos que atacan el problema desde ángulos distintos pero complementarios:

### Recomendador de Café

Un programa interactivo que hace preguntas al usuario sobre sus preferencias y, mediante lógica condicional, determina cuál es exactamente el café que debería comprar y cómo prepararlo.

**Tecnología:** Python  

### Guía Interactiva de Extracción

Un sitio web educativo y visual para el consumidor hogareño. Explica paso a paso cómo preparar café con cada métodos (Prensa Francesa, V60, Aeropress, Espresso).

**Tecnología:** HTML5 · CSS3 · JavaScript  
