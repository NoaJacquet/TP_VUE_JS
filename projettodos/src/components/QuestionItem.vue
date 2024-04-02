<script>
export default {
  props: {
    question: Object,
    isModified: Boolean // Propriété pour stocker la valeur de isModified de la classe parent
  },
  methods: {
            supprimerQuestion(){
                this.$emit('removeQuestion', this.question.uriQuestion);
            }
        },
        emits: ['removeQuestion']
};
</script>

<template>
  <h3>{{ question.question }}</h3>
  <input type = "button"
        class = "btn btn-danger"
        value = "Supprimer"
        @click = "supprimerQuestion">
  <ul>
    <li v-for="choice in question.choices" :key="choice">{{ choice }}</li>
  </ul>
  <p>Réponse : {{ question.answer[0] }}</p>
</template>

<style>
li {
  list-style-type: none;
}
</style>
