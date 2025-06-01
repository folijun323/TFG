from fastapi.responses import PlainTextResponse
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


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/empleados/")
def obtener_empleados(db: Session = Depends(get_db)):
    return db.query(models.Empleado).all()


@app.get("/empleado/{empleado_id}/proyectos/")
def obtener_proyectos(empleado_id: int, db: Session = Depends(get_db)):
    return db.query(models.Proyecto).join(models.AsignacionProyecto).filter(models.AsignacionProyecto.empleado_id == empleado_id).all()


@app.get("/departamentos/")
def obtener_departamentos(db: Session = Depends(get_db)):
    return db.query(models.Departamento).all()


@app.get("/departamento/{departamento_id}/empleados/")
def empleados_por_departamento(departamento_id: int, db: Session = Depends(get_db)):
    return db.query(models.Empleado).filter(models.Empleado.departamento_id == departamento_id).all()


@app.post("/consulta/")
def consulta_sql(texto: str, db: Session = Depends(get_db)):
    
    sql_query = nlp.procesar_consulta(texto)
    return sql_query
@app.post("/consulta", response_class=PlainTextResponse)
async def consulta(request: Request):
    body = await request.json()
    texto = body.get("query")

    sql = interpretar_consulta(texto)

    if not sql:
        return "No se pudo interpretar la consulta."

    db = SessionLocal()
    try:
        res = db.execute(text(sql))
        columnas = res.keys()
        result = res.fetchall()

        # Formatear como texto plano
        consulta_str = f"Consulta:\n{sql.strip()}\n\n"
        header = "\t".join(columnas) + "\n"
        rows = ""
        for row in result:
            rows += "\t".join(str(col) for col in row) + "\n"

        return consulta_str + "Resultado:\n" + header + rows

    except Exception as e:
        return f"Error en la consulta: {str(e)}"
    finally:
        db.close()

