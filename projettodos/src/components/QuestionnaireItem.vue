<script>
    export default {
        props: {
            questionnaire: Object
        },computed: {
            isQuestionnaireSelected() {
                return this.$parent.selectedQuestionnaire === this.questionnaire;
            },
            isQuestionnaireModif() {
                return this.$parent.modificationQuestionnaire;
            }
        },
        data() {
            return {
                isModified : false
            }
        },
        methods: {
            afficherQuestions() {
                this.$emit('afficher-questions', this.questionnaire);
            },
            supprimerQuestionnaire(){
                this.$emit('removeQuestionnaire', this.questionnaire.uriQuestionnaire);
            },
            modifierQuestionnaire(){
                this.$emit('modifierQuestionnaire');
            }
        },
        emits: ['afficher-questions', 'removeQuestionnaire', 'modifierQuestionnaire']
    }
</script>

<template>
    <button @click="afficherQuestions"> {{ questionnaire.nomQuestionnaire }} </button>
    <input type = "button"
        class = "btn btn-danger"
        value = "Modifier"
        @click = "modifierQuestionnaire"
        v-if="isQuestionnaireSelected">
    <input type = "button"
            class = "btn btn-danger"
            value = "Supprimer"
            @click = "supprimerQuestionnaire"
            v-if="isQuestionnaireSelected">
</template>