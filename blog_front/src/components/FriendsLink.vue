<template>
  <div class="container">
    <div class="columns">
      <el-card style="width: 45%;margin-right: 5%;display: inline-block">
        <div>
          <div v-for="link in links" :key="link.index" class="friendsLink">
          <p style="text-align: left;"><i class="el-icon-right" /><a :href="link.url" style="text-decoration: none;color: #2c3e50">{{ link.name }}</a></p>
            <el-divider/>
          </div>
        </div>
      </el-card>
      <el-card style="width: 43%;margin-left: 5%;float: right;">
        <p>你也可以在About留言</p>
        <p>收到互增友链请求后</p>
        <p>我会给您加上</p>
      </el-card>
    </div>
    <el-backtop></el-backtop>
  </div>
</template>

<script>
export default {
  name: 'FriendsLink',
  data () {
    return {
      links: []
    }
  },
  mounted () {
    this.axios.get('/api/friendslink/')
      .then(response => {
        this.links = response.data
      })
  }
}
</script>

<style scoped>
.columns{
  margin-left: 10%;
  margin-right: 10%;
}
.column{padding-right:5px;padding-left:5px;margin-top: 20px}
.one-third{width:31%; float: right}
.two-thirds{width:62%; float: left;text-align: left}
.container:before{display:table;content:""}
.container:after{display:table;clear:both;content:""}
.friendsLink>p:hover{
  cursor:pointer;
  color: #409EFF;
}
</style>
