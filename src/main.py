import sys

from reader import leer_pdf
from analyzer import analizar_cv_completo
from matcher import match_habilidades


REQUISITOS_PUESTO = {
    "lenguajes": ["python", "java", "sql"],
    "herramientas": ["git", "docker"],
    "sistemas": ["linux"]
}


def main():
    if len(sys.argv) < 2:
        print("Uso correcto: python src/main.py <ruta_al_cv.pdf>")
        return

    ruta_cv = sys.argv[1]

    texto_cv = leer_pdf(ruta_cv)
    resultado = analizar_cv_completo(texto_cv, REQUISITOS_PUESTO)

    habilidades_puesto = ["python", "sql", "docker"]

    score, coincidencias = match_habilidades(
        resultado["habilidades"],
        habilidades_puesto
    )

    print("=== RESULTADO DEL ANALISIS ===")
    print(f"Email detectado: {resultado['email']}")
    print(f"Habilidades detectadas: {resultado['habilidades']}")
    print(f"Match con el puesto: {score:.2f}%")
    print(f"Coincidencias: {coincidencias}")

    print("\n--- REQUISITOS DETECTADOS ---")
    for categoria, items in resultado["requisitos_detectados"].items():
        print(f"{categoria.capitalize()}: {items}")


if __name__ == "__main__":
    main()