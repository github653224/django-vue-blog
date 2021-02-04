<template>
  <div class="container">
    <div class="columns">
      <div class="column two-thirds">
        <div class="cates" v-for="cate in categories" :key="cate.index" >
          <el-card shadow="hover" style="margin: 5px" :id="cate.name">
          <h3>{{cate.name}} :</h3>
          <br/>
          <div v-for="(item,index) in cate.blogs" :key="index" class="cateblog">
            <p style="text-align: left"><i class="el-icon-link" />{{index + 1 }}、{{ item.title }}</p>
          <p style="text-align: right"><i class="el-icon-alarm-clock" /><span>发布时间</span>{{item.publish_time}}</p>
            <el-divider/>
          </div>
          </el-card>
        </div>
      </div>
      <div class="column one-third">
        <el-card style="width: 20%;position: fixed;top:30%" >
          <div v-for="cad in categories" :key="cad.index" style="text-align: left;font-size: medium">
            <a  :href="'#'+cad.name" style="text-decoration: none">{{cad.name}}({{cad.blogs.length}})</a>
            <el-divider></el-divider>
          </div>
        </el-card>
      </div>
    </div>
    <el-backtop></el-backtop>
  </div>
</template>

<script>
export default {
  name: 'CategoryContent',
  data () {
    return {
      categories: []
    }
  },
  mounted () {
    this.axios.get('/api/categorydetails/')
      .then(response => {
        this.categories = response.data
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
.cateblog:hover{
  cursor:pointer;
  color: #409EFF;
}
</style>
