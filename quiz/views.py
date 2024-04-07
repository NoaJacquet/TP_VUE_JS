from flask import jsonify, request, abort, make_response, url_for,render_template
from .app import app
from .models import Questionnaire, Question, Solution_simple, Solution_multiple,Question_simple,Question_multiple,db


def make_public_solution_simple(solution):
    new_solution = {}
    for field in solution:
        if field == 'id':
            new_solution['value'] = solution[field]
        else:
            new_solution[field] = solution[field]
    return new_solution

def make_public_solution_multiple(solution):
    new_solution = {}
    for field in solution:
        if field == 'id':
            new_solution['value'] = solution[field]
        else:
            new_solution[field] = solution[field]
    return new_solution

def make_public_question(question):
    new_question = {}
    for field in question:
        if field == 'id':
            new_question['uri'] = url_for('get_question', questionnaire_id=question['questionnaire_id'],question_id=question['id'], _external=True)
        else:
            new_question[field] = question[field]
    return new_question

def make_public_questionnaire(questionnaire):
    new_questionnaire = {}
    for field in questionnaire:
        if field == 'id':
            new_questionnaire['uri'] = url_for('get_question_questionnaire', questionnaire_id=questionnaire['id'], _external=True)
        else:
            new_questionnaire[field] = questionnaire[field]
    return new_questionnaire


@app.route('/todo/api/v1.0/questionnaire', methods=['GET'])
def get_questionnaire():
    return jsonify({'questionnaires': [make_public_questionnaire(questionnaire.to_json()) for questionnaire in Questionnaire.query.all()]})

@app.route('/todo/api/v1.0/questionnaire/', methods=['POST'])
def create_questionnaire():
    if not request.json or not 'name' in request.json:
        abort(400)
    questionnaire = Questionnaire(name=request.json['name'])
    db.session.add(questionnaire)
    db.session.commit()
    return jsonify({'questionnaire': make_public_questionnaire(questionnaire.to_json())}), 201

@app.route('/todo/api/v1.0/questionnaire/<int:questionnaire_id>', methods=['DELETE'])
def delete_questionnaire(questionnaire_id):
    questionnaire = Questionnaire.query.get_or_404(questionnaire_id)
    db.session.delete(questionnaire)
    db.session.commit()
    return jsonify({'result': True})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.route('/todo/api/v1.0/questionnaire/<int:questionnaire_id>', methods=['GET'])
def get_question_questionnaire(questionnaire_id):
    questionnaire = Questionnaire.query.get_or_404(questionnaire_id)
    questions = questionnaire.questions.all()
    return jsonify({'questions': [make_public_question(question.to_json()) for question in questions]})

@app.route('/todo/api/v1.0/questionnaire/<int:questionnaire_id>/<int:question_id>', methods=['GET'])
def get_question(questionnaire_id, question_id):
    question = Question.query.get_or_404(question_id)
    solutions = None
    if question.QuestionType == 'simple':
        solutions = Solution_simple.query.filter_by(question_id=question_id).all()
    elif question.QuestionType == 'multiple':
        solutions = Solution_multiple.query.filter_by(question_id=question_id).all()
    else:
        abort(400)  # Handle invalid question type

    question_data = make_public_question(question.to_json())
    if question.QuestionType == 'simple':
        solutions_data = [make_public_solution_simple(solution.to_json()) for solution in solutions]
    else:
        solutions_data = [make_public_solution_multiple(solution.to_json()) for solution in solutions]
    
    return jsonify({'question': question_data, 'solutions': solutions_data})

@app.route('/todo/api/v1.0/questionnaire/ajout_question', methods=['POST'])
def create_question():
    if not request.json or not 'title' in request.json or not 'QuestionType' in request.json:
        abort(400)
    title = request.json['title']
    QuestionType = request.json['QuestionType']
    if QuestionType == 'simple':
        question = Question_simple(title=title, questionnaire_id=request.json['questionnaire_id'])
        db.session.add(question) # Add the question to the session
        db.session.commit() # Commit the session to generate the ID
        solution = Solution_simple(question_id=question.id, answer=request.json['answer'], choix1=request.json['choix1'], choix2=request.json['choix2'])
    elif QuestionType == 'multiple':
        question = Question_multiple(title=title, questionnaire_id=request.json['questionnaire_id'])
        db.session.add(question) # Add the question to the session
        db.session.commit() # Commit the session to generate the ID
        solution = Solution_multiple(question_id=question.id, answers1=request.json['answers1'], answers2=request.json['answers2'], choix1=request.json['choix1'], choix2=request.json['choix2'], choix3=request.json['choix3'], choix4=request.json['choix4'])
    else:
        abort(400)
    db.session.add(solution)
    db.session.commit()
    return jsonify({'question': make_public_question(question.to_json())}), 201

@app.route('/todo/api/v1.0/questionnaire/<int:questionnaire_id>/<int:question_id>', methods=['DELETE'])
def delete_question(questionnaire_id, question_id):
    question = db.session.query(Question).get(question_id)
    if question is None:
        abort(404)
    db.session.delete(question)
    db.session.commit()
    return jsonify({"result": True})

from flask import request, jsonify, abort
from .models import db, Question
from flask import request, jsonify, abort
from .models import db, Question

@app.route('/todo/api/v1.0/questionnaire/<int:questionnaire_id>/<int:question_id>', methods=['PUT'])
def update_question(questionnaire_id, question_id):
    question = db.session.query(Question).filter_by(id=question_id, questionnaire_id=questionnaire_id).first()
    if not question:
        abort(404)
    if not request.json:
        abort(400)

    # Mise à jour des champs de la question
    if 'title' in request.json:
        question.title = request.json['title']
    # Mise à jour des solutions associées à la question
    solutions = None
    if question.QuestionType == 'simple':
        solutions = Solution_simple.query.filter_by(question_id=question_id).all()
    elif question.QuestionType == 'multiple':
        solutions = Solution_multiple.query.filter_by(question_id=question_id).all()

    for solution in solutions:
        if 'answer' in request.json:
            solution.answer = request.json['answer']
        if 'choix1' in request.json:
            solution.choix1 = request.json['choix1']
        if 'choix2' in request.json:
            solution.choix2 = request.json['choix2']
        if 'choix3' in request.json:
            solution.choix3 = request.json['choix3']
        if 'choix4' in request.json:
            solution.choix4 = request.json['choix4']

    # Commit des modifications à la base de données
    db.session.commit()

    return jsonify(question.to_json()), 200





@app.route('/todo/api/v1.0/questionnaire/<int:questionnaire_id>', methods=['PUT'])
def update_questionnaire(questionnaire_id):
    questionnaire = db.session.query(Questionnaire).get(questionnaire_id)
    if questionnaire is None:
        abort(404)
    if not request.json:
        abort(400)
    if "name" in request.json and type(request.json["name"]) != str:
        abort(400)
    questionnaire.name = request.json.get("name", questionnaire.name)
    db.session.commit()
    return jsonify(questionnaire.to_json())