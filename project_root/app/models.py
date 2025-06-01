from sqlalchemy import Column, Integer, String, Date, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from datetime import date
from .database import Base

class Departamento(Base):
    __tablename__ = 'departamentos'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)

    empleados = relationship('Empleado', back_populates='departamento', cascade='all, delete')
    proyectos = relationship('Proyecto', back_populates='departamento', cascade='all, delete')

class Cargo(Base):
    __tablename__ = 'cargos'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    salario_base = Column(DECIMAL(10, 2))

    empleados = relationship('Empleado', back_populates='cargo', cascade='all, delete')

class Empleado(Base):
    __tablename__ = 'empleados'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    fecha_contratacion = Column(Date)
    departamento_id = Column(Integer, ForeignKey('departamentos.id', ondelete='CASCADE', onupdate='CASCADE'))
    cargo_id = Column(Integer, ForeignKey('cargos.id', ondelete='CASCADE', onupdate='CASCADE'))

    departamento = relationship('Departamento', back_populates='empleados')
    cargo = relationship('Cargo', back_populates='empleados')
    asignaciones = relationship('AsignacionProyecto', back_populates='empleado', cascade='all, delete')

class Proyecto(Base):
    __tablename__ = 'proyectos'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    descripcion = Column(String)
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date, nullable=True)
    departamento_id = Column(Integer, ForeignKey('departamentos.id', ondelete='CASCADE', onupdate='CASCADE'))

    departamento = relationship('Departamento', back_populates='proyectos')
    asignaciones = relationship('AsignacionProyecto', back_populates='proyecto', cascade='all, delete')

class AsignacionProyecto(Base):
    __tablename__ = 'asignaciones_proyectos'

    id = Column(Integer, primary_key=True, index=True)
    empleado_id = Column(Integer, ForeignKey('empleados.id', ondelete='CASCADE', onupdate='CASCADE'))
    proyecto_id = Column(Integer, ForeignKey('proyectos.id', ondelete='CASCADE', onupdate='CASCADE'))
    fecha_asignacion = Column(Date, default=date.today)

    empleado = relationship('Empleado', back_populates='asignaciones')
    proyecto = relationship('Proyecto', back_populates='asignaciones')
