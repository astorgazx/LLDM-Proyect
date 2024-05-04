#Creacion de base de datos SQLite3 y Creacion de modelos de SQLalchemy

import os
from sqlalchemy import MetaData, create_engine 
from sqlalchemy import Column, Integer, String, ForeignKey ,Date 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import scoped_session
import db

Base = declarative_base()




# Creacion de modelos de SQLalchemy
class User(db.Base):
    #UserName
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    
    
    
    
class Miembro(db.Base):
    #Miembro
    __tablename__ = 'miembro'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    apellidoPaterno = Column(String(50), nullable=False)
    apellidoMaterno = Column(String(50), nullable=False)
    fechaNacimiento = Column(Date, nullable=False)
    lugarDeNacimiento = Column(String(50), nullable=True)
    sexo = Column(String(50), nullable=False)
    telefono = Column(String(50), nullable=True)
    correo = Column(String(50), nullable=True)
    direccion = Column(String(50), nullable=True)
    gradoEstudios = Column(String(50), nullable=True)
    ocupacion = Column(String(50), nullable=True)
    lugarTrabajo = Column(String(50), nullable=True)
    domicilioTrabajo = Column(String(50), nullable=True)
    estadoCivil = Column(String(50), nullable=True)
    horarioTrabajo = Column(String(50), nullable=True)
    especialidad = Column(String(50),nullable=True)
    oracion = Column(String(50),nullable=True)
    #Fotografia es un ligar donde se guardara la fotografia del miembro
    fotografia = Column(String(255), nullable=True)
    fechaDeBautismo = Column(Date, nullable=True)
    lugarDeBautismo = Column(String(50), nullable=True)
    fechaDeEspirituSanto = Column(Date, nullable=True)
    lugarDeEspirituSanto = Column(String(50), nullable=True)
    
    
    
    
    
class Matrimonio(db.Base):
    #Matrimonio
    __tablename__ = 'matrimonio'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fechaMatrimonio = Column(Date, nullable=False)
    lugarMatrimonio = Column(String(50), nullable=False)
    miembro1_id = Column(Integer, ForeignKey('miembro.id'))
    miembro2_id = Column(Integer, ForeignKey('miembro.id'))
    miembro1 = relationship('Miembro', foreign_keys=[miembro1_id])
    miembro2 = relationship('Miembro', foreign_keys=[miembro2_id])
    
class Hijo(db.Base):
    #Hijo
    __tablename__ = 'hijo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    fechaNacimiento = Column(Date, nullable=False)
    miembro_id = Column(Integer, ForeignKey('miembro.id'))
    miembro = relationship('Miembro', foreign_keys=[miembro_id])
    

