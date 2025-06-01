import spacy
from textblob import TextBlob
import nltk
import re

nlp = spacy.load('es_core_news_md')

def corregir_ortografia(texto: str) -> str:
    blob = TextBlob(texto)
    return str(blob.correct())

def extraer_palabras_clave(texto: str):
    doc = nlp(texto)
    keywords = [token.text for token in doc if not token.is_stop and not token.is_punct]
    return keywords

def procesar_consulta(texto: str):
    texto_corregido = corregir_ortografia(texto)
    palabras_clave = extraer_palabras_clave(texto_corregido)
    
    
   
    if 'empleado' in palabras_clave and 'sueldo' in palabras_clave:
        return "SELECT nombre, apellido, salario_base FROM empleados JOIN cargos ON empleados.cargo_id = cargos.id;"
    
    return "Consulta no reconocida"
from .nlp_patterns import patterns

def interpretar_consulta(texto):
    texto = texto.lower()
    
    for clave, info in patterns.items():
        if all(kw in texto for kw in info["keywords"]):
            if "sql" in info:
                return info["sql"]
            elif "sql_template" in info:
                if clave == "proyectos_por_departamento":
                    depto = texto.split("de")[-1].strip()
                    return info["sql_template"].format(departamento=depto)
                elif clave == "empleados_despues_fecha":
                    
                    import re
                    match = re.search(r'\d{4}-\d{2}-\d{2}', texto)
                    if match:
                        fecha = match.group(0)
                        return info["sql_template"].format(fecha=fecha)
    return None

def interpretar_consulta(texto):
    texto = texto.lower()

    for key, info in patterns.items():
        if all(kw in texto for kw in info["keywords"]):
            if "sql" in info:
                return info["sql"]
            elif "sql_template" in info:
                if key == "empleados_entre_fechas":
                    fechas = re.findall(r"\d{4}-\d{2}-\d{2}", texto)
                    if len(fechas) == 2:
                        return info["sql_template"].format(
                            fecha_inicio=fechas[0],
                            fecha_fin=fechas[1]
                        )
                elif key == "empleados_despues_fecha":
                    fecha = re.search(r"\d{4}-\d{2}-\d{2}", texto)
                    if fecha:
                        return info["sql_template"].format(fecha=fecha.group())
                elif key == "proyectos_por_departamento":
                    depto = re.search(r"departamento de (\w+)", texto)
                    if depto:
                        return info["sql_template"].format(departamento=depto.group(1))

                elif "variables" in info:
                    values = {}
                    for var in info["variables"]:
                        match = re.search(fr"{var} de (\w+)", texto)
                        if match:
                            values[var] = match.group(1)

                    if len(values) == len(info["variables"]):
                        return info["sql_template"].format(**values)

    return None
