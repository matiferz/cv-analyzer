from extractor import extraer_email, extraer_habilidades, extraer_requisitos

def analizar_cv_completo(texto, requisitos):
    return {
        "email": extraer_email(texto),
        "habilidades": extraer_habilidades(texto),
        "requisitos_detectados": extraer_requisitos(texto, requisitos)
    }