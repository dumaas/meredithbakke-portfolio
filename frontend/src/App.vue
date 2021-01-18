<template>
  <div id="app">
    <app-header />
    <router-view></router-view>
  </div>
</template>

<script>
  import Header from './components/header/Header.vue'
  export default {
    name: 'app',
    components: {
      'app-header': Header
    },
  }
</script>
