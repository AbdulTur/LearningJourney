<template>
  <div class="home">
    Hello World
  </div>
  <p>My name is {{ name }} and my age is {{ age }}</p>
</template>

<script>


export default {
  name: 'HomeView',
  setup() {
    console.log('setup')
    let name = 'abdul'
    let age = 22
    return {name, age}
  }

}

</script>
