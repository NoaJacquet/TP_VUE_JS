<script>
import questionnaire from "./components/questionnaire.vue";


export default {
  components: {
    questionnaire
  },
  data() {
    return {
      quizData: [
        {
          question: "Quelle est la capitale de la France?",
          choices: ["Paris", "Londres", "Madrid"],
          answer: "Paris",
        },
        {
          question: "Quel est le plus haut sommet du monde?",
          choices: ["Mont Everest", "K2", "Makalu"],
          answer: "Mont Everest",
        },
      ],
    };
  },
};
</script>

<template>
  <h1>Questionnaire IUT'O</h1>
  <h2>Choisissez un questionnaire :</h2>
  <button>Questionnaire 1</button>
  <button>Questionnaire 2</button>
  <!-- <div>
    <QuizVue :quizData="quizData" />
  </div> -->
  <questionnaire v-for="item in quizData":questionnaire=item></questionnaire>
</template>

<style scoped>
button{
  margin-left: 1vw;
}
</style>