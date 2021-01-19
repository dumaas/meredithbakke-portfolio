<template>
  <div id="addPost">
    <div class="addPost-form">
      <form @submit.prevent="onSubmit">

        <div class="input">
          <label for="title">Title</label>
          <input
            type="text"
            id="title"
            v-model="title">
        </div>
        <div class="input">
          <label for="year">Year</label>
          <select id="year" v-model="year">
            <option value="2019">2019</option>
            <option value="2020">2020</option>
            <option value="2021">2021</option>
          </select>
        </div>
        <div class="input">
          <label for="medium">Medium</label>
          <select id="medium" v-model="medium">
            <option value="Oil">Oil</option>
            <option value="Acrylic">Acrylic</option>
            <option value="Watercolor">Watercolor</option>
            <option value="Pastel">Pastel</option>
            <option value="Colored Pencil">Colored Pencil</option>
            <option value="Graphite">Graphite</option>
          </select>
        </div>
        <div class="input">
          <label for="substrate">Substrate</label>
          <select id="substrate" v-model="substrate">
            <option value="Panel">Panel</option>
            <option value="Canvas">Canvas</option>
            <option value="Linen">Linen</option>
            <option value="Paper">Paper</option>
          </select>
        </div>
        <div class="input">
          <label for="size">Size</label>
          <input
            type="text"
            id="size"
            v-model="size">
        </div>
        <div class="input">
          <label for="image">Image</label>
          <input
            type="file"
            id="image">
        </div>
        <div class="submit object-center">
          <button type="submit">Submit</button>
        </div>

      </form>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        title: '',
        year: null,
        medium: '',
        substrate: '',
        size: '',
        image: null,
      }
    },
  }
</script>

<style scoped>
  .addPost-form {
    width: 400px;
    margin: 30px auto;
    border: 1px solid #eee;
    padding: 20px;
    box-shadow: 0 2px 3px #ccc;
  }

  .input {
    margin: 10px auto;
  }

  .input label {
    display: block;
    color: #4e4e4e;
    margin-bottom: 6px;
  }

  .input.inline label {
    display: inline;
  }

  .input input {
    font: inherit;
    width: 100%;
    padding: 6px 12px;
    box-sizing: border-box;
    border: 1px solid #ccc;
  }

  .input.inline input {
    width: auto;
  }

  .input input:focus {
    outline: none;
    border: 1px solid #521751;
    background-color: #eee;
  }

  .input select {
    border: 1px solid #ccc;
    font: inherit;
  }

  .hobbies button {
    border: 1px solid #521751;
    background: #521751;
    color: white;
    padding: 6px;
    font: inherit;
    cursor: pointer;
  }

  .hobbies button:hover,
  .hobbies button:active {
    background-color: #8d4288;
  }

  .hobbies input {
    width: 90%;
  }

  .submit button {
    border: 1px solid #521751;
    color: #521751;
    padding: 10px 20px;
    font: inherit;
    cursor: pointer;
  }

  .submit button:hover,
  .submit button:active {
    background-color: #521751;
    color: white;
  }

  .submit button[disabled],
  .submit button[disabled]:hover,
  .submit button[disabled]:active {
    border: 1px solid #ccc;
    background-color: transparent;
    color: #ccc;
    cursor: not-allowed;
  }
</style>
