<template>
  <div>
    <a href="https://vitejs.dev" target="_blank">
      <img src="/vite.svg" class="logo" alt="Vite logo" />
    </a>
    <a href="https://vuejs.org/" target="_blank">
      <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
    </a>
    <QuizVue :quizData="quizData" />
  </div>
</template>

<script>
import axios from 'axios';
import QuizVue from "./components/quiz.vue";

// Définition de la fonction getQuestionnaire en dehors de l'objet Vue
async function getQuestionnaire() {
  try {
    const response = await axios.get('http://127.0.0.1:5000/todo/api/v1.0/questionnaire');
    const quizData = [];
    
    for (const questionnaire of response.data.questionnaires) {
      const questionnaireName = questionnaire['name'];
      const lesQuestionsResponse = await axios.get(questionnaire['uri']);
      
      for (const questions of lesQuestionsResponse.data.questions) {
        const questionTitle = questions['title'];
        const detailQuestionResponse = await axios.get(questions['uri']);
        const listeSolution = [];
        const listeChoix = [];
        for (const detail of detailQuestionResponse.data.solutions) {
          console.log(detail);
        }
        const questionData = {
          question: question['title'],
          choices: listeChoix,
          answer: listeSolution
        };
      }
    }
    
    return quizData; // Retourner les données obtenues
  } catch (error) {
    console.error('Erreur lors de la récupération des questionnaires :', error);
    return []; // Retourner un tableau vide en cas d'erreur
  }
}

export default {
  components: {
    QuizVue,
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


<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>