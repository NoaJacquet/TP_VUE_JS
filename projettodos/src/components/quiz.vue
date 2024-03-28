<template>
  <div>
    <h2>Quiz Questions</h2>
    <ul>
      <li v-for="questionnaire in quizData" :key="questionnaire.nomQuestionnaire">
        <h3>{{ questionnaire.nomQuestionnaire }}</h3>
        <ul>
          <li v-for="question in questionnaire.questions" :key="question.question">
            <h4>{{ question.question }}</h4>
            <ul>
              <li v-for="choice in question.choices" :key="choice">{{ choice }}</li>
            </ul>
            <p>Answer: {{ question.answer }}</p>
          </li>
        </ul>
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
