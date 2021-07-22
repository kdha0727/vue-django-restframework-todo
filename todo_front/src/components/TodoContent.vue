<template>
  <div>
    <v-container fluid>
      <v-layout column>

        <v-flex xs12>
          <h3 class="subject">what is your plan?</h3>
        </v-flex>

        <v-flex column>

          <v-row>
            <v-col cols="4" md="3">
              <v-text-field v-model="data.title" :counter="32" label="Title" required></v-text-field>
            </v-col>
            <v-col cols="4" md="3">
              <v-text-field v-model="data.author" :counter="64" label="Author" required></v-text-field>
            </v-col>
            <v-col cols="4" md="6">
              <v-text-field v-model="data.description" :counter="255" label="Content" required></v-text-field>
            </v-col>
          </v-row>

          <div data-app>
            <v-menu
              v-model="showPicker"
              :close-on-content-click="false"
              transition="scale-transition"
              offset-y
              max-width="300px"
              min-width="300px"
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  v-model="data.due_date"
                  label="Due Date"
                  hint="YYYY-MM-DD"
                  persistent-hint
                  readonly
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                width="300px"
                v-model="data.due_date"
                @input="showPicker = false"
              ></v-date-picker>
            </v-menu>
          </div>

          <v-btn @click="sendForm" color="#4CAF50">create</v-btn>
          <v-btn @click="clearForm" color="#F44336">clear</v-btn>

        </v-flex>

        <v-flex class="todoList" column>
          <v-card fluid>
            <v-list-item v-for="(todo, index) in todoList" v-bind:key="index">

              <v-row v-show="!todo.is_hidden">
                <v-col cols="12" md="8">
                  <v-list-item-content>
                    <v-list-item-title>Title: {{ todo.title }}</v-list-item-title>
                    <v-list-item-title>Author: {{ todo.author }}</v-list-item-title>
                    <v-list-item-title>Due Date: {{ todo.due_date }}</v-list-item-title>
                    <v-list-item-subtitle>Content: {{ todo.description }}</v-list-item-subtitle>
                    <v-list-item-title v-show="todo.completed">
                      <font-awesome-icon class="fa-2x" icon="calendar-check" />
                    </v-list-item-title>
                    <v-list-item-title v-show="!todo.completed">
                      <font-awesome-icon class="fa-2x" icon="calendar" />
                    </v-list-item-title>
                  </v-list-item-content>
                </v-col>
                <v-col cols="12" md="4">
                  <v-container>
                    <v-btn class="ma-2" @click="onlyTodoListCard(index)" color="#F9A825">Update</v-btn>
                    <v-btn class="ma-2" @click="deleteTodo(todo)" color="#F44336">Delete</v-btn>
                  </v-container>
                </v-col>
              </v-row>

              <v-form v-show="todo.is_hidden">
                <v-container>
                  <v-row>
                    <v-col cols="12" md="6">
                      <v-text-field v-model="todo.title" :counter="64" label="Title" required />
                    </v-col>
                    <v-col cols="12" md="3">
                      <v-text-field v-model="todo.author" :counter="32" label="Title" required />
                    </v-col>
                    <v-col cols="12" md="3">
                      <v-text-field v-model="todo.due_date" label="Title" required />
                    </v-col>
                    <v-col cols="12" md="10">
                      <v-text-field v-model="todo.description" :counter="500" label="Description" required />
                    </v-col>
                    <v-col cols="12" md="2">
                      <v-checkbox v-model="todo.completed" color="#2962FF" label="Completed" required />
                    </v-col>

                    <v-col cols="12" md="4">
                      <v-btn class="ma-2" @click="updateTodo(todo); todo.is_hidden = false;" color="#4CAF50">Save</v-btn>
                      <v-btn class="ma-2" @click="deleteTodo(todo)" color="#F44336">Delete</v-btn>
                    </v-col>

                  </v-row>
                </v-container>
              </v-form>

            </v-list-item>
          </v-card>
        </v-flex>

      </v-layout>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "TodoContent",
  props: ["todoList", "api_url"],
  data: () => ({
    showPicker: false,
    data: {
      title: "",
      author: "",
      description: "",
      due_date: new Date().toISOString().substr(0, 10)
    },
  }),
  methods: {
    clearForm: function() {
      this.data.title = "";
      this.data.description = "";
      this.data.author = "";
      this.data.due_date = "";
    },
    sendForm: function() {
      axios({
        method: "POST",
        url: this.api_url,
        data: this.data
      })
        .then(() => {
          this.$emit("saved");
        })
        .catch(e => {
          console.log("Failed to fetch", e.response);
        })
    },
    updateTodo: function(data) {
      axios({
        method: "PATCH",
        url: this.api_url + data.id + "/",
        data: data
      })
        .then(() => {
          this.$emit("patched");
        })
        .catch(e => {
          console.log("Failed to fetch", e);
        })
    },
    deleteTodo: function(data) {
      axios({
        method: "DELETE",
        url: this.api_url + data.id + "/"
      })
        .then(() => {
          this.$emit("deleted");
        })
        .catch(e => {
          console.log("Failed to fetch", e);
        })
    },
    onlyTodoListCard: function(index) {
      this.todoList.forEach((todo, idx) => (todo.is_hidden = (idx === index)))
      this.$forceUpdate();
    }
  }
}
</script>

<style scoped>
.subject {
  color: blue;
  font-style: oblique;
  padding: 30px;
  text-align: center;
}
.todoList {
    margin: 30px 0 30px 0;
}
</style>