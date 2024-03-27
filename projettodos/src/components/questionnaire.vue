<script>
    export default {
        props : {
            questionnaire : Object
        } ,
        methods :{
        }
    }
</script>

<template>
    <div class="checkbox">
        <label>
        <input type="checkbox" v-model ="todo.checked">
            {{ todo.text }}
        </label>
        <input type = "button"
            class = "btn btn-danger"
            value = "Supprimer"
            @click = "suppr">
    </div>
</template>