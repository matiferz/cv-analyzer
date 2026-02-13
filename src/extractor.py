import re

SKILLS = [
    "python", "java", "sql", "excel",
    "git", "docker", "linux"
]


def extraer_email(texto):
    texto = texto.replace(" ", "").replace("\n", "")
    patron = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    resultado = re.search(patron, texto)
    return resultado.group() if resultado else None

def extraer_habilidades(texto):
    texto = texto.lower()
    encontradas = []

    for skill in SKILLS:
        if skill in texto:
            encontradas.append(skill)

    return encontradas

def extraer_requisitos(texto, requisitos):
    texto = texto.lower()
    encontrados = {}

    for categoria, items in requisitos.items():
        encontrados[categoria] = []
        for item in items:
            if item in texto:
                encontrados[categoria].append(item)

    return encontrados