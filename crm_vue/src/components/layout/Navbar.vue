<template>
    <nav class="navbar is-dark">
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item">
                <strong>CRM</strong>
            </router-link>
        </div>

        <div class="navbar-menu">
            <div class="navbar-end">
                <router-link to="/dashboard/leads" class="navbar-item">Leads</router-link>
                <div class="navbar-item">
                    <div class="buttons">
                        <template v-if="!$store.state.isAuthenticated">
                            <router-link to="/sign-up" class="button is-success"><strong>Sign up</strong></router-link>
                            <router-link to="/log-in" class="button is-secondary">Log in</router-link>
                        </template>
                        <template v-else>  
                            <router-link to="/dashboard/my-account" class="button is-success">My Account</router-link>                      
                            <button @click="logout" class="button is-secondary">Log out</button>
                        </template>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
import axios from 'axios'
export default{
        name: 'Navbar',
        methods: {
            async logout(){
                await axios
                    .post('/api/v1/token/logout')
                    .then(response => {
                        console.log('Logged out')
                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))
                    })
                axios.defaults.headers.common['Authorization'] = ''
                localStorage.removeItem('token')
                this.$store.commit('removeToken')
                this.$router.push('/')
            }
        }
    }
</script>
