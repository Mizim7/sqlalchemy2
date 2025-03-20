from datetime import datetime
from database import SqlAlchemyBase, session
from data.users import User
from data.jobs import Jobs

SqlAlchemyBase.metadata.create_all(session.bind)

captain = User(
    surname="Scott",
    name="Ridley",
    age=21,
    position="captain",
    speciality="research engineer",
    address="module_1",
    email="scott_chief@mars.org",
    hashed_password="cap"
)
session.add(captain)

colonist1 = User(
    surname="Smith",
    name="John",
    age=35,
    position="engineer",
    speciality="mechanic",
    address="module_2",
    email="smith_john@mars.org",
    hashed_password="john123"
)
session.add(colonist1)

colonist2 = User(
    surname="Doe",
    name="Jane",
    age=28,
    position="scientist",
    speciality="biologist",
    address="module_3",
    email="doe_jane@mars.org",
    hashed_password="jane456"
)
session.add(colonist2)

colonist3 = User(
    surname="Brown",
    name="Alice",
    age=31,
    position="doctor",
    speciality="surgeon",
    address="module_4",
    email="brown_alice@mars.org",
    hashed_password="alice789"
)
session.add(colonist3)

session.commit()
job = Jobs(
    team_leader=1,
    job="deployment of residential modules 1 and 2",
    work_size=15,
    collaborators="2, 3",
    start_date=datetime.now(),
    is_finished=False
)
session.add(job)
session.commit()
