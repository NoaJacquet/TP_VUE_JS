<script>
    export default {
        props : {
            question : Object
        } ,
        methods :{
        }
    }
</script>

<template>
    <h3>{{ question.title }}</h3>
    <ul>
        <li v-for="choice in question.choices" :key="choice">{{ choice }}</li>
    </ul>
    <p>Réponse : {{ question.answer }}</p>
</template>
<style>
li{
    list-style-type: none;
  }
</style>