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
import QuizVue from "./components/quiz.vue";

export default {
  components: {
    QuizVue,
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