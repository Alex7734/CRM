<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">
                    {{lead.title}}
                </h1>
                <router-link to="/" class="button is-light">Edit</router-link>
            </div>
            <div class="column is-6">
                <div class="box">
                    <h2>Details</h2>

                </div>
            </div>

            <div class="column is-6">
                <div class="box">
                    <h2>Contact Information</h2>
                    
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default ({   
    name:"Lead",
    data() {
        return{
            lead: []
        }
    }
})
</script>
