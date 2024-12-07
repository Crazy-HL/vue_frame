// src/store.js
import { createStore } from 'vuex';

const store = createStore({
  // 定义状态
  state() {
    return {
      loaddata: null
    };
  },
  // // 定义变更状态的方法
  // mutations: {
  //   increment(state) {
  //     state.count++;
  //   },
  //   decrement(state) {
  //     state.count--;
  //   },
  // },
  // // 定义动作，可以包含异步操作
  // actions: {
  //   increment({ commit }) {
  //     commit('increment');
  //   },
  //   decrement({ commit }) {
  //     commit('decrement');
  //   },
  //   incrementAsync({ commit }, payload) {
  //     setTimeout(() => {
  //       commit('increment');
  //     }, payload.delay);
  //   },
  // },
  // // 定义获取状态的方法
  // getters: {
  //   getCount(state) {
  //     return state.count;
  //   },
  // },
});

// 导出 store
export default store;
