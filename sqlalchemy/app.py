from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = "people"

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)


    def __init__(self, ssn, firts, last, gender, age):
        self.ssn = ssn 
        self.firstname = firts
        self.lastname = last
        self.gender =  gender
        self.age =  age

    def __repr__(self):
        return f"({self.ssn}) {self.firstname} {self.lastname} ({self.gender} {self.age})"
    

class Thing(Base):
    __tablename__="things"

    tid = Column("tid", Integer, primary_key=True)
    description = Column("description", String)
    owner = Column(Integer, ForeignKey("people.ssn"))

    def __init__(self, tid, desc, ownder):
        self.tid = tid
        self.description = desc
        self.owner = ownder

    def __repr__(self):
        return f"({self.tid}) {self.description} owned by {self.owner}"

engine = create_engine("sqlite:///mydb2.db", echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person(1, "Abdul", "Turonov", "m", 35)
session.add(person)
session.commit()

p2 = Person(2, "Anna", "Blue", "f", 40)
p3 = Person(3, "Bob", "Blue", "m", 35)
p4 = Person(4, "Angela", "cold", "f", 22)

session.add(p2)
session.add(p3)
session.add(p4)
session.commit()


results = session.query(Person).filter(Person.lastname=="Blue")
print(results)