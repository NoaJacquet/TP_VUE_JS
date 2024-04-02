<script>
    export default {
        props: {
            questionnaire: Object
        },computed: {
            isQuestionnaireSelected() {
                return this.$parent.selectedQuestionnaire === this.questionnaire;
            }
        },
        methods: {
            afficherQuestions() {
                this.$emit('afficher-questions', this.questionnaire);
            },
            supprimerQuestionnaire : function(index){
                this.$emit('remove', {id:index});
            }
        },
        emits: ['afficher-questions', 'remove']
    }
</script>

<template>
    <button @click="afficherQuestions"> {{ questionnaire.nomQuestionnaire }} </button>
    <input type = "button"
            class = "btn btn-danger"
            value = "Supprimer"
            @click = "supprimerQuestionnaire(index)"
            v-if="isQuestionnaireSelected">
</template>