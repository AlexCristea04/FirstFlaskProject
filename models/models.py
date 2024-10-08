from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Project (db.Model):
    __tablename__ = 'projects'
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column (db.String (100), nullable=False)
    description= db.Column (db.String (200), nullable=True)

    tasks = db.relationship ('Task', backref='project', lazy=True)


    def repr_(self):
        return f'<Project {self.name}>'

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column (db.String(100), nullable=False)
    description= db.Column (db.String (200), nullable=True)
    project_id = db.Column (db.Integer, db.ForeignKey('projects.id'), nullable=False)
    completed = db.Column (db.Boolean, default=False)
    def repr_(self):
        return f'<Task {self.title}>'