<script>

import axios from 'axios';

export default {
  props: {
    question: Object,
    isModified: Boolean // Propriété pour stocker la valeur de isModified de la classe parent
  },
  data() {
    return {
      modificationQuestion: false,
    };
  },
  methods: {
            supprimerQuestion(){
              this.$emit('removeQuestion', this.question.uriQuestion);
            },
            async modifierQuestion(){
              if (this.modificationQuestion) {
                await axios.put(this.question.uriQuestion, {
                  title : this.newQuestionTitle,
                  choix1 : this.newQuestionChoix1,
                  choix2 : this.newQuestionChoix2,
                  answer : this.newQuestionAnswer
                });
                window.location.reload();
              }
              this.modificationQuestion = !this.modificationQuestion;
            }
        },
        emits: ['removeQuestion']
};
</script>

<template>
  <h3>{{ question.question }}</h3>
  <ul>
    <li v-for="choice in question.choices" :key="choice">{{ choice }}</li>
  </ul>
  <p>Réponse : {{ question.answer }}</p>
  <input v-if="modificationQuestion" type="text" placeholder="Titre" v-model="newQuestionTitle"></input>
  <input v-if="modificationQuestion" type="text" placeholder="Choix 1" v-model="newQuestionChoix1"></input>
  <input v-if="modificationQuestion" type="text" placeholder="Choix 2" v-model="newQuestionChoix2"></input>
  <input v-if="modificationQuestion" type="text" placeholder="Reponse" v-model="newQuestionAnswer"></input>
  
  <input type = "button"
      class = "btn btn-danger"
      value = "Modifier"
      @click = "modifierQuestion">
  <input type = "button"
        class = "btn btn-danger"
        value = "Supprimer"
        @click = "supprimerQuestion">
</template>

<style>
li {
  list-style-type: none;
}
</style>
