<template>
  <div >
    <el-menu :default-active="'2'"  mode="horizontal" @select="handleSelect" >
      <el-menu-item style="float: left"><img :src="logo" style="height: 95%" alt="logo"></el-menu-item>
      <el-menu-item index="1" style="float: right" @click="$router.push({name: 'index'})">点击返回首页</el-menu-item>
      <el-menu-item index="2" style="float: right">文章详情</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: 'detaiHeader',
  data () {
    return {
      logo: require('../static/IndexLogo.png')
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

<style scoped>

</style>
