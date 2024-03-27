<script>

    export default {
        props : {
            questionnaire : Object
        } ,
        methods :{
            afficherQuestions() {
                this.$emit('afficher-questions', this.questionnaire);
            }
        }
    }
</script>

<template>
    <button @click="afficherQuestions"> {{ questionnaire.title }} </button>
</template>