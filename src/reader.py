from PyPDF2 import PdfReader

def leer_pdf(ruta_archivo):
    reader = PdfReader(ruta_archivo)
    texto = ""

    for pagina in reader.pages:
        texto += pagina.extract_text()


    return texto