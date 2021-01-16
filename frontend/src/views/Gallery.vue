<template>
  <div class="container mx-auto px-10 p-10">
    <h1 class="font-bold">Mere's Artwork</h1>
    <div id="gallery" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 mt-10">
      <div
        id="imageCards"
        class="rounded overflow-hidden shadow-lg text-center"
        v-for="post in postList"
        :key="post.id">
        <img :src="post.image" class="w-full" />
        <div class="px-6 py-4">
          <div class="font-bold text-purple-500 text-xl mb-2">{{ post.title }}</div>
          <ul>
            <li><strong>{{ post.medium }} on {{ post.substrate }}</strong></li>
            <li><strong>Year: {{ post.year }}</strong></li>
            <li><strong>Size: {{ post.size }}</strong></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    computed: {
      postList() {
        return this.$store.getters.postList
      },
    },
    created() {
      this.$store.dispatch('fetchPosts')
    },
  }
</script>

<style>
  h1, p {
    text-align: center;
  }

  p {
    color: red;
  }
</style>
