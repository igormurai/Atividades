const app = Vue.createApp({
    data() {
        return {
            product: 'Socks',
            description: 'These are comfortable socks for everyday wear.'
        }
    }
});

const mountedApp = app.mount('#app');
