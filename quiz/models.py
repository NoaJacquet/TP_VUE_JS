# models.py
from flask_sqlalchemy import SQLAlchemy
from .app import db

Base = db.Model
metadata = Base.metadata

class Questionnaire(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<Questionnaire (%d) %r>' % (self.id, self.name)
    
    def __init__(self, name):
        self.name = name
        
    def to_json(self):
        json={
            'id': self.id,
            'name': self.name,
        }
        return json

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120))  # Changed from 'question' to 'title'
    QuestionType = db.Column(db.String(120))
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'))
    questionnaire = db.relationship('Questionnaire',
        backref=db.backref('questions', lazy='dynamic'))
    
    def __repr__(self):
        return '<Question (%d) %r>' % (self.id, self.title)  # Changed from 'question' to 'title'
    
    def __init__(self, title, QuestionType, questionnaire_id):
        self.title = title
        self.QuestionType = QuestionType
        self.questionnaire_id = questionnaire_id
        
    def to_json(self):
        json={
            'id': self.id,
            'title': self.title,  # Changed from 'question' to 'title'
            'questionnaire_id': self.questionnaire_id,
        }
        return json
    

class Question_simple (Question):
    id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)
    __mapper_args__ = {
        'polymorphic_identity':'simple'
    }
    def __init__(self, title, questionnaire_id):
        super().__init__(title, 'simple', questionnaire_id)
    
        
        
        
    def to_json(self):
        json = super().to_json()
        return json
    
class Question_multiple (Question):
    id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)
    __mapper_args__ = {
        'polymorphic_identity':'multiple'
    }    
    
    def __init__(self, title, questionnaire_id ):
        super().__init__(title, 'multiple', questionnaire_id)
       
        
    def to_json(self):
        json = super().to_json()
        return json
    def add_answer(self, answer):
        self.answers.append(answer)

class Solution_simple(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question_simple.id'))
    answer = db.Column(db.String(120))
    choix1 = db.Column(db.String(120))
    choix2 = db.Column(db.String(120))
    
    def __init__(self, question_id, answer, choix1, choix2):
        self.question_id = question_id
        self.answer = answer
        self.choix1 = choix1
        self.choix2 = choix2
        
    def to_json(self):
        json = {
            'id': self.id,
            'question_id': self.question_id,
            'answer': self.answer,
            'choix1': self.choix1,
            'choix2': self.choix2,
        }
        return json
    def reponce_possible(self):
        if self.choix1== self.answer or self.choix2== self.answer:
            return True
        else:
            return False
class Solution_multiple(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question_multiple.id'))
    answers1 = db.Column(db.String(120))
    answers2 = db.Column(db.String(120))
    choix1 = db.Column(db.String(120))
    choix2 = db.Column(db.String(120))
    choix3 = db.Column(db.String(120))
    choix4 = db.Column(db.String(120))
    
    def __init__(self, question_id, answers1, answers2, choix1, choix2, choix3, choix4):
        self.question_id = question_id
        self.answers1 = answers1
        self.answers2 = answers2
        self.choix1 = choix1
        self.choix2 = choix2
        self.choix3 = choix3
        self.choix4 = choix4
        
    def to_json(self):
        json = {
            'id': self.id,
            'question_id': self.question_id,
            'answers1': self.answers1,
            'answers2': self.answers2,
            'choix1': self.choix1,
            'choix2': self.choix2,
            'choix3': self.choix3,
            'choix4': self.choix4,
        }
        return json
    def reponce_possible(self):
        if self.choix1== self.answers1 or self.choix2== self.answers1 or self.choix3== self.answers1 or self.choix4== self.answers1:
            return True
        else:
            return False
