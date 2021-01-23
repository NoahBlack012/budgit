<template>
    <div id="RecentItems">
        <h3>Recent Items</h3>
        <div class="items" v-bind:key='item.id' v-for="item in items">
            <p>
                {{item.title}}
                ${{item.value}}
            </p>
        </div>
    </div>
</template>

<script>
import { mapGetters } from "vuex";
import axios from "axios";
export default {
    name: "RecentItems", 
    data(){
        return{
            all_items: null,
            items: null, 
        }
    }, 
    computed: mapGetters(['userid']),
    async created(){
        if (! this.userid){
            this.$router.push("/login")
        }
        const res = await axios.post(`${process.env.VUE_APP_BASE}/get_items`, {
            "userid": this.userid,
            "api_key": process.env.VUE_APP_API_KEY
        })
        this.all_items = res.data.items;
        this.items = this.all_items.slice(this.all_items.length - 3, this.all_items.length);
    }
}
</script>

<style scoped>

</style>