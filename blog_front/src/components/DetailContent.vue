<template>
  <div class="container">
    <div class="columns">
      <div class="column two-thirds">
        <article v-html="blog.contents" v-highlight style="width: 100%"></article>
        <el-divider></el-divider>
        <h3>分享本页</h3>
        <V-share
          :share-url="url"
          :share-description="blog.summary"
          :share-wechat-qrcode-title="blog.title"
        ></V-share>
        <h3>评论区(支持MD语法):</h3>
        <mavon-editor
          v-model="content"
          ref="md"
          :toolbars="toolbars"
          style="min-height: 300px"
        />
        <el-button class="editor-btn" type="primary" style="float: right;margin-top: 10px" round @click="dialogFormVisible=true"
        >提交</el-button
        >
        <el-dialog title="请输入邮箱" :visible.sync="dialogFormVisible" width="20%">
          <p style="text-align: center">请放心填写,仅做非机器人校验以及回复需要</p>
          <el-form :model="ruleform" status-icon :rules="rules" ref="ruleForm">
            <el-form-item label="" label-width="'30px'" prop="email">
              <el-input v-model="ruleform.email" autocomplete="off"></el-input>
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="dialogFormVisible = false">取 消</el-button>
            <el-button type="primary" @click="submitForm('ruleForm')">确 定</el-button>
          </div>
        </el-dialog>
      </div>
      <div class="column one-third">
        <br/>
        <br/>
        <el-card>
          <div class="authorInfo">
          <el-avatar :src="avatar" :size="'large'"></el-avatar>
          <h4><i class="el-icon-user-solid" /><span>作者:</span>Oslo Wang</h4>
          <h4><i class="el-icon-location-information" /><span>位置:</span>Hangzhou China</h4>
          <br />
          </div>
          <el-divider></el-divider>
          <div class="blogInfo">
          <h4><i class="el-icon-notebook-1"/><span>标题:</span><span>{{ blog.title }}</span> </h4>
          <h4><i class="el-icon-alarm-clock" /><span>发布时间:</span><span>{{ blog.publish_time }}</span> </h4>
          <h4><i class="el-icon-collection-tag" /><span>分类:</span><span>{{ blog.category_name }}</span> </h4>
          </div>
        </el-card>
      <br />
        <br />
        <el-card>
          <div class="comments-title">
          <h4>评论展示区:</h4>
          <h5>Tips: 发表评论在文章末尾哦!</h5>
          </div>
          <el-divider></el-divider>
          <div class="comments" v-for="item in comments" :key="item.index" >
            <div>
              <h5>
              <span style="float: left">来自{{ item.email }}的网友</span>
              <span style="float: right">{{ item.create_time }}</span></h5>
              <br/><br />
              <div class="comments-content" style="text-align: left;color: black" v-html="item.content" v-highlight>
              </div>
              <el-divider />
            </div>
          </div>
        </el-card>
      </div>
    </div>
    <el-backtop></el-backtop>
  </div>
</template>

<script>
export default {
  name: 'DetailContent',
  data () {
    const checkEmail = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('邮箱不能为空'))
      }
      setTimeout(() => {
        const re = new RegExp('[\\w!#$%&\'*+/=?^_`{|}~-]+(?:\\.[\\w!#$%&\'*+/=?^_`{|}~-]+)*@(?:[\\w](?:[\\w-]*[\\w])?\\.)+[\\w](?:[\\w-]*[\\w])?')
        if (!re.test(value)) {
          callback(new Error('请输入合法的邮箱'))
        } else {
          callback()
        }
      }, 1000)
    }
    return {
      blogId: this.$route.query.id,
      blog: [],
      comments: [],
      searchValue: '',
      content: '',
      avatar: require('../static/avata.jpeg'),
      ruleform: {
        email: ''
      },
      url: '',
      rules: {
        email: [
          {
            validator: checkEmail,
            trigger: 'blur'
          }
        ]
      },
      dialogFormVisible: false,
      toolbars: {
        bold: true, // 粗体
        italic: true, // 斜体
        header: true, // 标题
        underline: true, // 下划线
        strikethrough: true, // 中划线
        mark: true, // 标记
        superscript: true, // 上角标
        subscript: true, // 下角标
        quote: true, // 引用
        ol: true, // 有序列表
        ul: true, // 无序列表
        link: true, // 链接
        imagelink: false, // 图片链接
        code: true, // code
        table: true, // 表格
        fullscreen: false, // 全屏编辑
        readmodel: true, // 沉浸式阅读
        htmlcode: true, // 展示html源码
        help: true, // 帮助
        undo: true, // 上一步
        redo: true, // 下一步
        trash: true, // 清空
        save: true, // 保存（触发events中的save事件）
        navigation: true, // 导航目录
        alignleft: true, // 左对齐
        aligncenter: true, // 居中
        alignright: true, // 右对齐
        subfield: true, // 单双栏模式
        preview: true // 预览
      }
    }
  },
  mounted () {
    this.axios.get('/api/blogDetails/' + this.blogId + '/')
      .then(response => {
        this.blog = response.data
        if (this.blog.comments !== []) {
          this.comments = this.blog.comments
        }
      })
    this.url = window.location.href
  },
  methods: {
    getTime () {
      var date1 = new Date()
      var year = date1.getFullYear()
      var month = date1.getMonth() + 1
      var day = date1.getDate()
      var hours = date1.getHours()
      var minutes = date1.getMinutes()
      var seconds = date1.getSeconds()
      return year + '-' + month + '-' + day + ' ' + hours + ':' + minutes + ':' + seconds
    },
    getDay () {
      var date1 = new Date()
      var year = date1.getFullYear()
      var month = date1.getMonth() + 1
      var day = date1.getDate()
      return year + '-' + month + '-' + day
    },
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          const comments = {
            id: 0,
            create_time: this.getTime(),
            emails: this.ruleform.email,
            ip: 'dsdsf',
            content: this.content,
            blog_id: this.blogId
          }
          this.axios.post('/api/addComments/', JSON.stringify(comments))
            .then(response => {
              if (response.status === 201) {
                this.$message({
                  message: '提交评论成功',
                  type: 'success'
                })
                this.dialogFormVisible = false
                this.comments.push(response.data)
                this.ruleform.email = ''
                this.content = ''
              } else {
                this.$message({
                  message: '提交失败',
                  type: 'warning'
                })
              }
            })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    }
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
p>img{
  height: 100%;
  width: auto;
}
</style>
<style lang="scss">
.markdown-container {
  .editor-btn {
    margin-top: 20px;
  }
  .title {
    padding-bottom: 30px;
    text-align: center;
    font-size: 20px;
    letter-spacing: 1px;
    color: #333;
    font-weight: 600;
  }
}
.blogInfo{
  margin-left: 10%;
  margin-right: 10%;
  text-align: left;
  font-style: normal;
}
.authorInfo{
  margin-left: 10%;
  margin-right: 10%;
  text-align: left;
  font-style: normal;
}
.comments-title{
  text-align: left;
}
.comments{
  font-size: xx-small;
  font-weight: lighter;
  text-decoration: none;
}
img{
  width: 85%;
}
</style>
