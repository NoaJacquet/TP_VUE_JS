from .models import db, Questionnaire, Question_simple, Question_multiple, Solution_simple, Solution_multiple
from sqlalchemy.orm import sessionmaker
from .app import app
@app.cli.command('initDB')
def initDB():
    db.drop_all()
    db.create_all()
    print('Base de données initialisée.')
    
    Session = sessionmaker(bind=db.engine, autoflush=False)
    session = Session()
    
    # Créer une session pour interagir avec la base de données
    questionnaires = [
        Questionnaire(name='Mathématiques'),
        Questionnaire(name='Sciences'),
        Questionnaire(name='Histoire')
    ]
    session.add_all(questionnaires)
    
    questions_simple = [
        Question_simple(title="Combien font 3 * 3", questionnaire_id=1),
        Question_simple(title="Combien font 2 + 2 ?", questionnaire_id=1)
    ]
    session.add_all(questions_simple)
    
    questions_multiple = [
        Question_multiple(title="Quels sont les éléments constitutifs de l'eau ?", questionnaire_id=2),
        Question_multiple(title="En quelle année a eu lieu la révolution française ?", questionnaire_id=3)
    ]
    session.add_all(questions_multiple)
    
    solutions_simple = [
        Solution_simple(question_id=1, answer="9", choix1="6", choix2="9"),
        Solution_simple(question_id=2, answer="4", choix1="2", choix2="4"),
        Solution_simple(question_id=4, answer="1789", choix1="1789", choix2="1987")
    ]
    session.add_all(solutions_simple)
    
    solutions_multiple = [
        Solution_multiple(question_id=3, answers1="Hydrogène", answers2="Oxygène", choix1="Hydrogène", choix2="Oxygène", choix3="Azote", choix4="Carbone")
        
    ]
    session.add_all(solutions_multiple)
    
    session.commit()

