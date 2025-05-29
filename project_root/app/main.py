from sqlalchemy import text
from app.database import SessionLocal
from app.nlp import interpretar_consulta
from fastapi import FastAPI, Request
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, database, nlp
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

# Crea la aplicación FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def serve_index():
    return FileResponse("static/index.html")

# Conexión a la base de datos
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Consultar todos los empleados
@app.get("/empleados/")
def obtener_empleados(db: Session = Depends(get_db)):
    return db.query(models.Empleado).all()

# Consultar proyectos de un empleado específico
@app.get("/empleado/{empleado_id}/proyectos/")
def obtener_proyectos(empleado_id: int, db: Session = Depends(get_db)):
    return db.query(models.Proyecto).join(models.AsignacionProyecto).filter(models.AsignacionProyecto.empleado_id == empleado_id).all()

# Consultar departamentos con sus empleados
@app.get("/departamentos/")
def obtener_departamentos(db: Session = Depends(get_db)):
    return db.query(models.Departamento).all()

# Consultar empleados en un departamento específico
@app.get("/departamento/{departamento_id}/empleados/")
def empleados_por_departamento(departamento_id: int, db: Session = Depends(get_db)):
    return db.query(models.Empleado).filter(models.Empleado.departamento_id == departamento_id).all()

# Consulta en lenguaje natural (sólo ejemplo de endpoint para este paso)
@app.post("/consulta/")
def consulta_sql(texto: str, db: Session = Depends(get_db)):
    # Aquí procesaríamos el texto con NLP y luego ejecutamos la consulta SQL generada
    sql_query = nlp.procesar_consulta(texto)
    return sql_query  # Por ejemplo, devolver el SQL generado
@app.post("/consulta")
async def consulta(request: Request):
    body = await request.json()
    texto = body.get("query")
    
    sql = interpretar_consulta(texto)
    
    if not sql:
        return {"error": "No se pudo interpretar la consulta."}
    
    db = SessionLocal()
    try:
        res = db.execute(text(sql))
        columnas = res.keys()
        result = res.fetchall()
        data = [dict(zip(columnas, row)) for row in result]
        return {"consulta": sql, "resultado": data}
    except Exception as e:
        return {"error": str(e)}
    finally:
        db.close()
