<template>
  <div class="header">
    <el-menu :default-active="activeIndex"  mode="horizontal" >
      <el-menu-item style="float: left"><img :src="logo" style="height: 95%" alt="logo"></el-menu-item>
      <el-menu-item index="4" style="float: right" @click="changeCompent('friends')">友链</el-menu-item>
      <el-menu-item index="3" style="float: right" @click="changeCompent('about')">关于</el-menu-item>
      <el-menu-item index="2" style="float: right" @click="changeCompent('category')">分类</el-menu-item>
      <el-menu-item index="1" style="float: right" @click="changeCompent('index')">首页</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: 'Header',
  data () {
    return {
      input: '请输入搜索内容',
      logo: require('../static/IndexLogo.png')
    }
  },
  methods: {
  },
  props: ['activeIndex', 'changeCompent']
}
</script>

<style scoped>
.header{
  color: #ffffff;
}
.el-input{
  border-radius: 30px
}
</style>
