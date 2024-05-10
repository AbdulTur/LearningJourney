<template>
  <h1>Reaction Timer</h1>
  <button @click="start" :disabled="isPlaying">play</button>
  <block v-if="isPlaying" :delay="delay"></block>
</template>

<script>
import block from './components/block.vue';

export default {
  name: 'App',
  components: { block },
  data() {
    return {
      isPlaying: false,
      delay: null,
    }
  },
  methods: {
    start() {
      this.delay=2000 + Math.random() * 5000
      this.isPlaying= true
      console.log(this.delay)
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
  color: #444;
  margin-top: 60px;
}
</style>
