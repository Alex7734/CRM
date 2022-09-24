<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <div class="container">
      <br />
      <p v-if="this.$store.state.isAuthenticated">The user token is: {{info}}</p>
      <p v-else>User not auth.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Home',
  data() {
    return {
      info: null
    }
  },
  mounted(){
    this.info = axios.defaults.headers.common['Authorization'] 
  }
}
</script>
