<template>
  <el-container>
    <el-header ><Header :activeIndex="'1'" :changeCompent="changeCompent"/></el-header>
    <el-main >
      <div class="musicbox">
        <p><i class="el-icon-sugar" /> 来点音乐吧</p>
        <VueAplayer  :music="songlist[0]" :float="true" :shuffle='true' :autoplay="true" :list="songlist" :listFolded="true"  :showLrc='true' />
      </div><component :is="CurrentCompent"/></el-main>
    <el-footer><Footer /></el-footer>
  </el-container>
</template>

<script>
import Header from '@/components/Header'
import IndexContent from '@/components/IndexContent'
import Footer from '@/components/Footer'
import CategoryContent from '@/components/CategoryContent'
import About from '@/components/About'
import FriendsLink from '@/components/FriendsLink'
import VueAplayer from 'vue-aplayer'
VueAplayer.disableVersionBadge = true
export default {
  name: 'index',
  components: { Header, IndexContent, Footer, CategoryContent, About, FriendsLink, VueAplayer },
  data () {
    return {
      CurrentCompent: IndexContent,
      musicSwitch: '',
      songlist: [
        {
          id: 44,
          artist: '周杰伦',
          title: '安静',
          src: 'http://www.oslozone.cn/music/mp3/安静.mp3',
          pic: 'http://www.oslozone.cn/music/pic/安静.jpg',
          lrc: 'http://www.oslozone.cn/music/lrc/安静.lrc'
        }
      ]
    }
  },
  methods: {
    changeCompent (key) {
      const actions = new Map([
        ['index', [IndexContent]],
        ['category', [CategoryContent]],
        ['about', [About]],
        ['friends', [FriendsLink]]
      ])
      this.CurrentCompent = actions.get(key)[0]
    }
  },
  beforeCreate () {
    this.axios.get('/api/music/')
      .then(response => {
        this.songlist = response.data
      })
  }
}
</script>
<style>
.el-main{
  width: 80%;
  margin: 0 auto;
  border: 0;
}
.el-header{
  width: 80%;
  margin: 0 auto;
  font-family: Dosis,Open Sans,pingfang SC,helvetica neue,arial,hiragino sans gb,microsoft yahei ui,microsoft yahei,simsun,sans-serif;
  font-size: .9375rem;
}
.el-footer{
  width: 80%;
  margin: 0 auto;
}
.musicbox{
  width: 75%;
  margin: 0 auto;
}
.musicbox > p{
  text-align: left;
  font-weight: normal;
  color: #333333;
  margin: 2px 2px;
}

</style>
