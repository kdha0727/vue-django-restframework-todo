<template>
  <v-app>
    <TodoHeader />
    <TodoContent
        v-bind:todoList="todoList"
        v-bind:api_url="api_url"
        v-on:saved="getTodoList"
        v-on:deleted="getTodoList"
        v-on:patched="getTodoList"
    />
    <TodoFooter />
  </v-app>
</template>

<script>
import axios from 'axios';
import TodoHeader from "./components/TodoHeader";
import TodoContent from "./components/TodoContent";
import TodoFooter from "./components/TodoFooter";

export default {
  name: "App",
  data: () => ({
    api_url: 'http://localhost:8000/api/todo/',
    todoList: [],
  }),
  components: {
    TodoHeader,
    TodoContent,
    TodoFooter
  },
  mounted() {
    this.getTodoList();
  },
  methods: {
    getTodoList: function() {
      axios({
        method: "GET",
        url: this.api_url
      })
        .then(response => {
          this.todoList = response.data;
          this.todoList.forEach(todo => {todo.is_hidden = false;})
        })
        .catch(response => {
          console.log("Failed to fetch", response)
        })
    },
    updateTodoList: function() {}
  }
}

</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap');
#app {
  font-family: 'Do Hyeon', sans-serif;
}
</style>
