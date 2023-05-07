--We're going to start by defining a BaseModel class that sets the database connection:
class BaseModel(Model):
    class Meta:
        database = db
--A Meta class is a class that describes and configures another class. More on Meta classes here

--Now that we have our BaseModel, we can define our model and have it inherit from this BaseModel class:
class Question(BaseModel):
    question = CharField()
    answer = CharField()
--CharField() and DateField() are from PeeWee's field's.

--Once we have the model, we need to add the corresponding table to the database:
db.create_tables([Question])

artificial = Question(question='What is Artificial Intelligence?', answer='the theory and development of computer systems able to perform tasks that normally require human intelligence, such as visual perception, speech recognition, decision-making, and translation between languages.')
artificial.save()

app = Question(question='Is Machine Learning a form of Artificial Intelligence?', answer='yes')
app.save()

robotics = Question(question="How does robotics work?", answer='To function, a combination of computer programming and algorithms, a remotely controlled manipulator, actuators, control systems -- action, processing and perception -- real-time sensors and an element of automation helps to inform what a robot or robotic system does.')
robotics.save()

--commands: \c database_name then \dt to show all tables, \l lists all databses on the server, DROP DATABASES deletes and CREATE DATABSE creates

