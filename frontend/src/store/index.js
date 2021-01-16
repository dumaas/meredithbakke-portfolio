import { createStore } from 'vuex'
import axios from '../axios-auth'

import router from '../router/index.js'

export default createStore({
  state: {
    access_token: null,
    refresh_token: null,
    posts: null
  },
  mutations: {
    authUser(state, postData) {
      state.access_token = postData.access_token
      state.refresh_token = postData.refresh_token
    },
    clearAuthData(state) {
      state.access_token = null
      state.refresh_token = null
    },
    storePost(state, posts) {
      state.posts = posts
    },
  },
  actions: {
    login({commit}, authData) {
      axios.post('dj-rest-auth/login/', {
        username: authData.username,
        email: authData.email,
        password: authData.password,
      })
        .then(res => {
          console.log(res)
          commit('authUser', {
            access_token: res.data.access_token,
            refresh_token: res.data.refresh_token
          })
          localStorage.setItem('access_token', res.data.access_token)
          localStorage.setItem('refresh_token', res.data.refresh_token)
          router.replace('/')
        })
        .catch(err => console.log(err))
    },
    logout({commit}) {
      commit('clearAuthData')
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      router.replace('/')
    },
    fetchPosts({commit}) {
      axios.get('')
        .then(res => {
          console.log(res)
          const data = res.data
          const posts = []
          for (let key in data) {
            const post = data[key]
            post.id = key
            posts.push(post)
          }
          console.log(posts)
          commit('storePost', posts)
        })
        .catch(err => console.log(err))
    }
  },
  modules: {
  },
  getters: {
    postList(state) {
      return state.posts
    },
    isAuthenticated(state) {
      return state.access_token !== null
    },
  }
})
