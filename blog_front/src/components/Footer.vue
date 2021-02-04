<template>
<div>
  <p>©2020 OsloZone.cn 版权所有</p>
  <p @click="toGov">蜀ICP备2020035099号</p>
</div>
</template>

<script>
export default {
  name: 'Footer',
  methods: {
    toGov () {
      window.location.href = 'https://beian.miit.gov.cn/'
    }
  }
}
</script>

<style scoped>
div{
  background: transparent;
  font-style: initial;
  margin-left: 10%;
  margin-right: 10%;
  width: 80%;
  margin-top: 20px;
  text-align: left;
}
p{
  font-size: 14px;
  text-decoration: none;
}

</style>
