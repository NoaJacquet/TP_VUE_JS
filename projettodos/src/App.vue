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
      const lesQuestionsResponse = await axios.get(questionnaire['uri']);
      const questions = [];
      
      for (const question of lesQuestionsResponse.data.questions) {
        const questionTitle = question['title'];
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
          question: questionTitle,
          choices: choices,
          answer: solutions
        };
        
        questions.push(questionData);
      }
      
      const questionnaireData = {
        nomQuestionnaire: questionnaireName,
        questions: questions
      };
      
      quizData.push(questionnaireData);
    }
    console.log(quizData)
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
        remove(questionnaire) {
          console.log("test");
            this.quizData = this.quizData.filter(item => item.title !== questionnaire.title);
            if (this.selectedQuestionnaire && this.selectedQuestionnaire.title === questionnaire.title) {
                this.selectedQuestionnaire = null;
            }
        }
    },
  data() {
    return {
      quizData: [] // Initialisé à un tableau vide
    };
  },
  async mounted() { // Utilisation de async pour rendre la fonction asynchrone
    this.quizData = await getQuestionnaire(); // Attendre le résultat de la fonction getQuestionnaire()
    console.log(this.quizData)
  }
};
</script>

<template>
  <h1>Questionnaire IUT'O</h1>
  <h2>Choisissez un questionnaire :</h2>
  <questionnaire v-for="item in quizData" :key="item.title" :questionnaire="item" @afficher-questions="afficherQuestions"
  ></questionnaire>
  <button>+</button>
  <div v-if="selectedQuestionnaire">
    <h3>{{ selectedQuestionnaire.title }}</h3> 
    <question v-for="(question, index) in selectedQuestionnaire.questions" :key="index" :question="question"></question>
  </div>
</template>

<style scoped>
button{
  margin-left: 1vw;
}
</style>