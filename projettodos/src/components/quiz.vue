<template>
    <div>
      <ul>
        <li v-for="quiz in quizData" :key="quiz.question">
          <h3>{{ quiz.question }}</h3>
          <ul>
            <li v-for="choice in quiz.choices" :key="choice">{{ choice }}</li>
          </ul>
          <p>Answer: {{ quiz.answer }}</p>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      quizData: {
        type: Array,
        required: true,
      },
    },
  };
  </script>
  
  <style scoped>
  h2 {
    color: #42b883;
  }
  </style>