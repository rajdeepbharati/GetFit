<template>
  <div id="app">
    <template>
      <b-navbar>
        <template slot="brand">
          <b-navbar-item tag="router-link" :to="{ path: '/' }">
            <!-- <img
              src="https://raw.githubusercontent.com/buefy/buefy/dev/static/img/buefy-logo.png"
              alt="Lightweight UI components for Vue.js based on Bulma"
            /> -->
            <h1>VigorIt</h1>
          </b-navbar-item>
        </template>
        <template slot="start">
          <b-navbar-item href="#">
            Home
          </b-navbar-item>
          <b-navbar-dropdown label="Info">
            <b-navbar-item href="#">
              About
            </b-navbar-item>
            <b-navbar-item href="#">
              Contact
            </b-navbar-item>
          </b-navbar-dropdown>
        </template>

        <template slot="end">
          <b-navbar-item tag="div">
            <div class="buttons">
              <a class="button is-primary">
                <strong>Sign up</strong>
              </a>
              <a class="button is-light">
                Log in
              </a>
            </div>
          </b-navbar-item>
        </template>
      </b-navbar>
    </template>
    <h1>VigorIt</h1>
    <!-- <router-view /> -->
    <carousel
      :per-page="1"
      :navigate-to="someLocalProperty"
      :mouse-drag="false"
    >
      <slide @slideclick="handleSlideClick">
        <img src="@/assets/logo-vue.png" alt="" />
      </slide>
      <slide>
        Slide 2 Content
      </slide>
    </carousel>
  </div>
</template>

<script>
import { Carousel, Slide } from 'vue-carousel'

export default {
  components: {
    Carousel,
    Slide
  },
  methods: {
    handleSlideClick () {}
  }
}
</script>
<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
