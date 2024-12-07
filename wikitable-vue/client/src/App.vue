<template>
 <div class="div0" id="div1">
        <iframe id="frameLeft" src="https://en.wikipedia.org/wiki/France" title="页面1"></iframe>
    </div>
 

    <div class="div0" id="div2">
        <div class="VisContainer">
            <div class="topContainer"></div>
            <div class="botContainer"></div>
        </div>
    </div>

    <div class="div0" id="div3"> 
        <iframe id="frameRight" src="https://en.wikipedia.org/wiki/China" title="页面2"></iframe>
    </div>
</template>

<script>

import axios from 'axios';


export default {
  name: 'App',
  components: {
  },
  mounted() {
    this.getData()
  },
  methods: {
    getData() {
      let self = this
      api.get('data', { 'papername': 'rmap1' }, data => {
        Data = data
        store.state.loaddata = Math.random()
      })
      api.get('',{},(data)=>{
        console.log('@@@',data)
      })
      api.get('user',{'code':'9090'},(data)=>{
        console.log('!!!',data)
      })
    }
  }
}


</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100%;
  height: 100%;
  position: absolute;
}

body {
  display: flex;
  /* 使用 Flexbox 布局 */
  justify-content: space-around;
  /* 在主轴上均匀分配空间 */
  align-items: flex-start;
  /* 在交叉轴上靠上对齐 */
  height: 100vh;
  /* 设定页面高度为视口高度 */
  margin: 0;
  /* 去掉默认的 margin */
  width: 100%;
  height: 100%;
}

iframe {
  width: 100%;
  /* 每个 iframe 占据 30% 的宽度 */
  height: 100%;
  border: 1px solid #ccc;
  /* 给 iframe 添加边框 */
}

.div0 {
    position: absolute;
    height: 100vh;
}
#div1 {
    left: 0;
    width: 30%;
}
#div2 {
    width: 40%;
}
#div3 {
    width: 30%;
    right: 0;
}
</style>