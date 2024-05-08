const app = Vue.createApp({
    data() {
        return {
            showBooks: true,
            title: "FInal Empire",
            author: "Brandon",
            age: 20
        }
    },
    methods: {
        handleEvent(e) {
            console.log(e, e.type)
        }
    },
})

app.mount('#app') 