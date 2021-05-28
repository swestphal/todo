
<template>
  <div class="home">
    <h1 class="title">Vuengo</h1>

    <hr>

    <div class="columns">
      <div class="column is-3 is-offset-3">
        <form >
          <h2 class="subtitle">Add task</h2>

          <div class="field">
            <label class="label">Description</label>
            <div class="control">
              <input class="input" type="text">
            </div>
          </div>

          <div class="field">
            <label class="label">Status</label>
            <div class="control">
              <div class="select">
                <select>
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
          <div class="card" v-for >
            <div class="card-content">description</div>

            <footer class="card-footer">
              <a class="card-footer-item" >Done</a>
            </footer>
          </div>
        </div>
      </div>
      <div class="column is-6">
        <h2 class="subtitle">Done</h2>

        <div class="done">
          <div class="card" >
            <div class="card-content">description</div>

            <footer class="card-footer">
              <a class="card-footer-item" >To do</a>
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
import {onMounted, ref} from "vue";

export default {
  name: 'Home',
  setup() {
    const tasks = ref([])

    const load = async()=> {

      const response = await axios.get('tasks')
      tasks.value = response.data

    }

    onMounted(load)
    return {
      tasks,
      load
    }
  }
}
</script>
<style lang="scss">

</style>