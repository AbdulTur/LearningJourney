<template>
    <div class="post-list">
      <div v-for="post in posts" :key="post.id">
        <!-- <h3>{{ post.title }}</h3> -->
        <SinglePost :post="post" />
      </div>
    </div>
  </template>
  
  <script>
  // component imports
  import { onMounted } from 'vue';
  import SinglePost from './SinglePost.vue'
  
  export default {
    props: ['posts'],
    components: { SinglePost },
    setup(props) {
      onMounted(() => {console.log('component mounted')})
    }
  }
  </script>
  
  <style>
  
  </style>