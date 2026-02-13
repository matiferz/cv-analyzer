def match_habilidades(habilidades_cv, habilidades_puesto):
    coincidencias = set(habilidades_cv) & set(habilidades_puesto)
    score = (len(coincidencias) / len(habilidades_puesto)) * 100
    return score, list(coincidencias)