# Импортируем из библиотеки SqlAlchemy нужные функции и классы
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, CheckConstraint
from sqlalchemy import Integer, String, Boolean, DateTime, Numeric, SmallInteger

import datetime as dt

# Импортируем из подмодуля ORM функции и классы, предназначенные для
# высокоуровневой работы с базой данных посредством построения объектной модели ORM
# (ORM ~ object-relational model)
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker

# Общий родиетльский класс для дочерних таблиц
class Basis(DeclarativeBase):
    pass


class Jobs(Basis):
    __tablename__ = "jobs"
    job_id = Column(String(10), primary_key=True)
    job_title = Column(String(100), nullable=False)
    min_salary = Column(Integer(), nullable=True)
    max_salary = Column(Integer(), nullable=True)

    # Обратные связи
    employees = relationship("Employee", back_populates="job")
    job_history = relationship("JobHistory", back_populates="job")

    def __str__(self):
        return f"<{self.job_id}> {self.job_title} salary from {self.min_salary} to {self.max_salary}"


class JobHistory(Basis):
    __tablename__ = "job_history"
    employee_id = Column(Integer(), nullable=False)
    start_date = Column(String(20), nullable=False)
    end_date = Column(String(20), nullable=False)
    job_id = Column(String(10), ForeignKey("jobs.job_id"), nullable=False)
    department_id = Column(Integer(), nullable=True)

    job_id = relationship("Jobs", back_populates="job_history")
    employee = relationship("Employee", back_populates="job_history")

    def __str__(self):
        return f"<{self.employee_id}> on {self.job_id} from {self.start_date} to {self.end_date}"


class JobGrades(Basis):
    __tablename__ = "job_grades"
    grade_level = Column(String(10), primary_key=True)
    lowest_sal = Column(Integer(), nullable=True)
    highest_sal = Column(Integer(), nullable=True)

    def __str__(self):
        return f"{self.grade_level} {self.lowest_sal} {self.highest_sal}"


class Region(Basis):
    __tablename__ = "regions"
    region_id = Column(Integer(), primary_key=True)
    region_name = Column(String(100), unique=True, nullable=False)

    # Обратная связь
    countries = relationship("Country", back_populates="region")

    def __str__(self):
        return f"<{self.region_id}> {self.region_name}"


class Country(Basis):
    __tablename__ = "countries"
    country_id = Column(String(2), primary_key=True)
    country_name = Column(String(100), nullable=False, unique=True)
    region_id = Column(Integer(), ForeignKey("regions.region_id"))

    # Исправлена связь
    region = relationship("Region", back_populates="countries")
    locations = relationship("Location", back_populates="country")

    def __str__(self):
        return f"<{self.country_id}> {self.country_name}"


class Location(Basis):
    __tablename__ = "locations"
    location_id = Column(Integer(), primary_key=True)
    street_address = Column(String(100), nullable=True)
    postal_code = Column(String(20), nullable=True)
    city = Column(String(100), nullable=False)
    state_province = Column(String(100), nullable=True)
    country_id = Column(String(2), ForeignKey("countries.country_id"))

    # Обратные связи
    country = relationship("Country", back_populates="locations")
    departments = relationship("Department", back_populates="location")

    def __str__(self):
        return f"<{self.location_id}> {self.state_province}, {self.city}"


class Employee(Basis):
    __tablename__ = "employees"
    employee_id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(20), nullable=True)
    hire_date = Column(String(20), nullable=False)
    job_id = Column(String(10), ForeignKey("jobs.job_id"), nullable=False)
    salary = Column(Numeric(10, 2), nullable=True)
    commission_pct = Column(Numeric(3, 2), nullable=True)
    manager_id = Column(Integer(), ForeignKey("employees.employee_id"), nullable=True)
    department_id = Column(Integer(), nullable=True)

    # Исправлены связи
    job = relationship("Job", back_populates="employees")
    manager = relationship("Employee", remote_side=[employee_id], backref="subordinates")
    job_history = relationship("JobHistory", back_populates="employee")
    managed_departments = relationship("Department", back_populates="manager")

    def __str__(self):
        return f"<{self.employee_id}> {self.first_name} {self.last_name}"


class Department(Basis):
    __tablename__ = "departments"
    department_id = Column(Integer(), primary_key=True)
    department_name = Column(String(100), nullable=False)
    manager_id = Column(Integer(), ForeignKey("employees.employee_id"), nullable=True)
    location_id = Column(Integer(), ForeignKey("locations.location_id"), nullable=True)

    # Исправлены связи
    manager = relationship("Employee", back_populates="managed_departments")
    location = relationship("Location", back_populates="departments")

    def __str__(self):
        return f"<{self.department_id}> {self.department_name}"

engine = create_engine("sqlite:///My_Database/Staff.db?echo=True")

Basis.metadata.create_all(engine)

factory = sessionmaker(bind=engine)