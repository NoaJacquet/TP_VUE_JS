<script>
import question from "./components/QuestionItem.vue";
import questionnaire from "./components/QuestionnaireItem.vue";


export default {
  components: {
    question,
    questionnaire
  },
  data() {
    return {
      quizData: [
        {
          title: "Questionnaire 1",
          questions: [
            {
              title: "Quelle est la capitale de la France?",
              choices: ["Paris", "Londres", "Madrid"],
              answer: "Paris"
            },
            {
              title: "Quel est le plus haut sommet du monde?",
              choices: ["Mont Everest", "K2", "Makalu"],
              answer: "Mont Everest"
            }
          ]
        },{
          title: "Questionnaire 2",
          questions: [
            {
              title: "Quelle est la capitale de la Espagne?",
              choices: ["Paris", "Londres", "Madrid"],
              answer: "Madrid"
            },
            {
              title: "Quel est le plus haut sommet du monde?",
              choices: ["Mont Everest", "K2", "Makalu"],
              answer: "Mont Everest"
            }
          ]
        },
        // Ajoutez d'autres questionnaires si nécessaire
      ],
      selectedQuestionnaire: null
    };
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