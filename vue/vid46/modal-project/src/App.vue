<template>
  <h1>{{title}}</h1>
  <div v-if="showModal">
    <Modal theme="sale" @close="toggleModal">
      <template v-slot:links>
        <a href="#">Sign up</a>
        <a href="#">More info</a>
      </template>
      <h1>ninja giveaway</h1>
      <p>Giveaway</p>
    </Modal>
  </div>
  <button @click.alt="toggleModal">open modal (alt) </button>
</template>

<script>
import Modal from './components/Modal.vue';

export default {
  name: 'App',
  components: {Modal},
  data() {
    return {
      title: 'My First Vue app',
      header: 'Sign up',
      text: 'giveaway',
      showModal: false,
    }
  },
  methods: {
    toggleModal(){
      this.showModal =!this.showModal
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
