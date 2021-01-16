<template>
  <div class="rounded overflow-hidden shadow-lg">
    <img :src="image" class="w-full" />
    <div class="px-6 py-4">
      <div class="font-bold text-purple-500 text-x1 mb-2">Title: {{ image.title }}</div>
    </div>
  </div>
</template>

<script>
  export default {
    props: ['image'],
    setup(props) {
      const image
    }
  }
</script>
