<template>
  <div id="dashboard" class="container mx-auto px-10 p-10">
    <h1 class="font-bold text-center">Welcome to the dashboard!</h1>
    <CreatePost />
  </div>
</template>

<script>
  import CreatePost from '../components/admin/CreatePost.vue'

  export default {
    components: {
      CreatePost,
    }
  }
</script>
