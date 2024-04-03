function affiche_questionnaire() {
    fetch("http://127.0.0.1:5000/todo/api/v1.0/questionnaire")
    .then(response => response.json())
    .then(data => {
        console.log(data);
        let html = "<ul>";
        data.questionnaires.forEach(questionnaire => {
            html += "<li>" + questionnaire.name + "</li>"; // Modification selon la structure de vos données
        });
        html += "</ul>";
        document.getElementById("questionnaire").innerHTML = html;
    });
}
function affiche_question_par_questionnaire(id) {
    fetch("http://127.0.0.1:5000/todo/api/v1.0/questionnaire/"+id)
    .then(response => response.json())
    .then(data => {
        console.log(data);
        let html = "<ul>";
        data.questions.forEach(question => {
            html += "<li>" + question.title + "</li>"; // Modification selon la structure de vos données
        });
        html += "</ul>";
        html+="<button id='questionButton'>voir question en entier</button>";
        html+="<input type='text' id='laQuestion' placeholder='nom question'>";
        document.getElementById("reponse").innerHTML = html;
    });
}
function affiche_reponse_par_question(id_questionnaire,id_question) {
    fetch("http:///127.0.0.1:5000/todo/api/v1.0/questionnaire/"+id_questionnaire+"/"+id_question)
    .then(response => response.json())
    .then(data => {
        console.log(data);
        let html = "<ul>";
        data.reponses.forEach(reponse => {
            html += "<li> la reponce est: " + reponse.answer + "</li>"; // Modification selon la structure de vos données
            html += "<li> choix1 est: " + reponse.choix1 + "</li>"; // Modification selon la structure de vos données
            html += "<li> choix2 est: " + reponse.choix2 + "</li>"; // Modification selon la structure de vos données
        });
        html += "</ul>";
        document.getElementById("reponse").innerHTML = html;
    });
}
    function ajout_question_simple(title, questions_type, questionnaire_id, answer,choix1, choix2) {
        let data = {
            title: title,
            QuestionType: questions_type,
            questionnaire_id: questionnaire_id,
            answer: answer,
            choix1: choix1,
            choix2: choix2
            
        };
    
        fetch("http://127.0.0.1:5000/todo/api/v1.0/questionnaire/ajout_question", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            // Gérer la réponse du serveur si nécessaire
        })
    }
    





    document.addEventListener("DOMContentLoaded", function() {
        affiche_questionnaire();
    
        document.getElementById("ajouter").addEventListener("click", function() {
            let id = document.getElementById("question").value;
            affiche_question_par_questionnaire(id);
        });
    
        document.getElementById("type_question").addEventListener("change", function() {
            var selectValue = this.value;
    
            if (selectValue === "simple") {
                let title = document.getElementById("texte").value;
                let questions_type = document.getElementById("type_question").value;
                let questionnaire_id = document.getElementById("id_questionnaire").value;
                let answer = document.getElementById("reponse").value;
                let choix1 = document.getElementById("choix1").value;
                let choix2 = document.getElementById("choix2").value;
                document.getElementById("inputSimple").style.display = "block";
                document.getElementById("inputMultiple").style.display = "none";
                ajout_question_simple(title, questions_type, questionnaire_id, answer,choix1, choix2);

            } else if (selectValue === "multiple") {
                document.getElementById("inputSimple").style.display = "none";
                document.getElementById("inputMultiple").style.display = "block";
            }
        });
    
        document.getElementById("ajouter_question").addEventListener("click", function() {
            let title = document.getElementById("texte").value;
            let questions_type = document.getElementById("type_question").value;
            let questionnaire_id = document.getElementById("id_questionnaire").value;
    

        });
    });
    
