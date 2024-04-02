<script>
import axios from 'axios';
import question from "./components/QuestionItem.vue";
import questionnaire from "./components/QuestionnaireItem.vue";


// Définition de la fonction getQuestionnaire en dehors de l'objet Vue
async function getQuestionnaire() {
  try {
    const response = await axios.get('http://127.0.0.1:5000/todo/api/v1.0/questionnaire');
    const quizData = [];
    for (const questionnaire of response.data.questionnaires) {
      const questionnaireName = questionnaire['name'];
      const questionnaireUri = questionnaire['uri'];
      const lesQuestionsResponse = await axios.get(questionnaire['uri']);
      const questions = [];
      
      for (const question of lesQuestionsResponse.data.questions) {
        const questionTitle = question['title'];
        const questionUri = question['uri'];
        const detailQuestionResponse = await axios.get(question['uri']);
        const solutions = [];
        const choices = [];
        
        for (const detail of detailQuestionResponse.data.solutions) {
          // Ajouter toutes les valeurs des clés commençant par 'choix'
          Object.keys(detail).forEach(key => {
            if (key.startsWith('choi')) {
              choices.push(detail[key]);
            }
            if (key.startsWith('answer')){
              solutions.push(detail[key]);
            }
          });
        }
        
        const questionData = {
          uriQuestion: questionUri,
          question: questionTitle,
          choices: choices,
          answer: solutions
        };
        
        questions.push(questionData);
      }
      
      const questionnaireData = {
        uriQuestionnaire: questionnaireUri,
        nomQuestionnaire: questionnaireName,
        questions: questions
      };
      
      quizData.push(questionnaireData);
    }
    return quizData; // Retourner les données obtenues
  } catch (error) {
    console.error('Erreur lors de la récupération des questionnaires :', error);
    return []; // Retourner un tableau vide en cas d'erreur
  }
}

export default {
  components: {
    question,
    questionnaire
  },
  methods: {
        afficherQuestions(questionnaire) {
          this.selectedQuestionnaire = questionnaire;
        },
        async createQuestionnaire(){
          if (this.creationQuestionnaire && this.newQuestionnaireName!== undefined) {
            await axios.post("http://127.0.0.1:5000/todo/api/v1.0/questionnaire/" ,{
              name : this.newQuestionnaireName
            });
            window.location.reload();
          }
          this.creationQuestionnaire = !this.creationQuestionnaire;
        }, 
        async createQuestion(){
          if (this.creationQuestion) {
            await axios.post("http://127.0.0.1:5000/todo/api/v1.0/questionnaire/ajout_question" ,{
              questionnaire_id : this.selectedQuestionnaire.uriQuestionnaire.charAt(this.selectedQuestionnaire.uriQuestionnaire.length - 1),
              QuestionType : 'simple',
              title : this.newQuestionTitle,
              choix1 : this.newQuestionChoix1,
              choix2 : this.newQuestionChoix2,
              answer : this.newQuestionAnswer
            });
            window.location.reload();
          }
          this.creationQuestion = !this.creationQuestion;
        },
        async removeQuestionnaire(uriQuestionnaire) {
          await axios.delete(uriQuestionnaire);
          window.location.reload();
        },
        async removeQuestion(uriQuestion) {
          await axios.delete(uriQuestion);
          window.location.reload();
        },
        async modifierQuestionnaire() {
          if (this.modificationQuestionnaire) {
            await axios.put(this.selectedQuestionnaire.uriQuestionnaire, {
              name: this.newQuestionnaireName
            });
            window.location.reload();
          }
          this.modificationQuestionnaire = !this.modificationQuestionnaire;
        }
    },
  data() {
    return {
      modificationQuestionnaire: false,
      creationQuestionnaire: false,
      creationQuestion: false,
      selectedQuestionnaire: null,
      quizData: [] // Initialisé à un tableau vide
    };
  },
  async mounted() { // Utilisation de async pour rendre la fonction asynchrone
    this.quizData = await getQuestionnaire(); // Attendre le résultat de la fonction getQuestionnaire()
  }
};
</script>

<template>
  <h1>Questionnaire IUT'O</h1>
  <h2>Choisissez un questionnaire :</h2>
  <questionnaire v-for="(item) in quizData" :questionnaire="item" @afficher-questions="afficherQuestions" @removeQuestionnaire="removeQuestionnaire" @modifierQuestionnaire="modifierQuestionnaire"></questionnaire>
  <input v-if="modificationQuestionnaire" type="text"  v-model="newQuestionnaireName"></input>
  <input v-if="creationQuestionnaire" type="text"  v-model="newQuestionnaireName"></input>
  <button @click="createQuestionnaire">+</button>
  <div v-if="selectedQuestionnaire">
    <h2>{{ this.selectedQuestionnaire.nomQuestionnaire }}</h2> 
    <question v-for="(question, index) in selectedQuestionnaire.questions" :key="index" :question="question" @removeQuestion="removeQuestion"></question>
    <input v-if="creationQuestion" type="text" placeholder="Titre" v-model="newQuestionTitle"></input>
    <input v-if="creationQuestion" type="text" placeholder="Choix 1" v-model="newQuestionAnswer"></input>
    <input v-if="creationQuestion" type="text" placeholder="Choix 2" v-model="newQuestionChoix1"></input>
    <input v-if="creationQuestion" type="text" placeholder="Reponse" v-model="newQuestionChoix2"></input>
    <button @click="createQuestion">+</button>
  </div>
</template>


<style scoped>
button{
  margin-left: 1vw;
}
</style>