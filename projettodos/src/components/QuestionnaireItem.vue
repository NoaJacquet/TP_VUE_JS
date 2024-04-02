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
            supprimerQuestionnaire : function(){
                this.$emit('remove', { id : this.questionnaire.title });
            }
        }
    }
</script>

<template>
    <button @click="afficherQuestions"> {{ questionnaire.title }} </button>
    <input type = "button"
            class = "btn btn-danger"
            value = "Supprimer"
            @click = "supprimerQuestionnaire"
            v-if="isQuestionnaireSelected">
</template>