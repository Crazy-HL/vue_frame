import { createApp } from 'vue'
import App from './App.vue'

import $ from 'jquery'
window.$ = $

import api from './api/index.js'
window.api = api
window.Data = {}

import * as d3 from 'd3'
window.d3 = d3

import store from './store.js';
window.store = store


const app = createApp(App)
app.use(store)
app.mount('#app')
