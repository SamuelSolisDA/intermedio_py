sample_articles = [
    {
        "title": "Python logra nuevo éxito",
        "source": {"name": "TechNews"},
        "description": "Gran noticia",
        "category": "Tecnología",
    },
    {
        "title": "Mercado en crisis",
        "source": {"name": "Finance"},
        "description": "Análisis completo",
        "category": "Economía",
    },
    {
        "title": "Nueva tecnología",
        "source": {"name": "TechNews"},
        "description": "Innovación",
        "category": "Tecnología",
    },
    {
        "title": "Deportes hoy",
        "source": {"name": "Sports"},
        "description": "Resultados",
        "category": "Deportes",
    },
    {
        "title": "Política actual",
        "source": {"name": "News"},
        "description": "Actualidad",
        "category": "Política",
    },
    {
        "title": "Ciencia avanza",
        "source": {"name": "Science"},
        "description": "Descubrimientos",
        "category": "Ciencia",
    },
]


def extract_titles_traditional(articles):
    """Extrae solo los títulos usando un for."""
    titles = []
    for article in articles:
        titles.append(article["title"])  # iteración + acumulación
    return titles


def extract_titles(articles):
    """Extrae solo los títulos usando un comprehension."""
    return [article["title"] for article in articles]  # comprehension


def extract_titles_long(articles):
    return [a["title"] for a in articles if len(a["title"]) > 10]


# Filtra descripciones largas y construye un dict título -> descripción
long_desc_by_title = {
    a["title"]: a["description"]
    for a in sample_articles
    if len(a["description"]) > 20  # puede devolver vacío si ninguna cumple
}

# Ajusta el umbral si necesitas resultados visibles
by_title_min5 = {
    a["title"]: a["description"] for a in sample_articles if len(a["description"]) > 5
}


# Forma tradicional
def unique_sources_traditional(articles):
    sources = set()
    for a in articles:
        sources.add(a["source"])  # evita duplicados de manera natural
    return sources


# Con set comprehension
def unique_sources(articles):
    return {a["source"] for a in articles}

print(extract_titles(sample_articles))
print("====================================")
print(extract_titles_traditional(sample_articles))