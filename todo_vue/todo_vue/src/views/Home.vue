
<template>
  <div class="home">
    <h1 class="title">Vuengo</h1>

    <hr>

    <div class="columns">
      <div class="column is-3 is-offset-3">
        <form @submit.prevent="addTask">
          <h2 class="subtitle">Add task</h2>

          <div class="field">
            <label class="label">Description</label>
            <div class="control">
              <input class="input" type="text" v-model="description">
            </div>
          </div>

          <div class="field">
            <label class="label">Status</label>
            <div class="control">
              <div class="select">
                <select v-model="status">
                  <option value="todo">To do</option>
                  <option value="done">Done</option>
                </select>
              </div>
            </div>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-link">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>

    <div class="columns">
      <div class="column is-6">
        <h2 class="subtitle">To do</h2>

        <div class="todo">
          <div class="card" v-for="todo in todos"  :key="todo.id" >
            <div class="card-content">{{ todo.description }}</div>

            <footer class="card-footer">
              <a class="card-footer-item" @click="setStatus(todo.id,'done')">Done</a>
            </footer>
          </div>
        </div>
      </div>
      <div class="column is-6">
        <h2 class="subtitle">Done</h2>

        <div class="done">
          <div class="card" v-for="done in dones" :key="done.id">
            <div class="card-content">{{ done.description }}</div>

            <footer class="card-footer">
              <a class="card-footer-item" @click="setStatus(done.id,'todo')">To do</a>
            </footer>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script >
// @ is an alias to /src
import axios from 'axios';
import {onMounted, ref, computed} from "vue";

export default {
  name: 'Home',
  setup() {
    const tasks = ref([])
    const description=ref("")
    const status=ref("todo")

    const load = async()=> {
      const response = await axios.get('tasks/')
      tasks.value = response.data
    }

    const setStatus = (id,status) => {
      const task = tasks.value.filter(task => task.id === id)[0]

      axios.put('tasks/'+id+'/', {
        status:status,
        description:task.description
      }).then(()=> {
        task.status = status
      })

    }

    const addTask = () => {
      if (description.value) {
        axios.post('tasks/', {
            description: description.value,
            status: status.value
          }).then( (response) => {
            // build new task
            const newTask = {
              'id':response.data.id,
              'description':response.data.description,
              'status':response.data.status
            }
            // push new task in tasks-array
            tasks.value.push(newTask)

            // set back and clean input fields
            description.value=""
            status.value="todo"
          }).catch((error) => {
            console.log(error)
          })
        }
      }


    onMounted(load)

    const todos = computed (()=> {
        return tasks.value.filter(task => task.status==='todo')
      })
    const dones = computed (()=> {
        return tasks.value.filter(task => task.status==='done')
      })

    return {
      tasks,
      load,
      addTask,
      setStatus,
      todos,
      dones,
      description,
      status
    }
  }
}
</script>
<style lang="scss">

</style>