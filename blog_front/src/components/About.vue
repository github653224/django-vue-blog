<template>
  <div class="container">
    <div class="columns">
      <el-card shadow="always" style="width: 100%">
      <el-avatar :src="avatar" style="margin: 0 auto;"></el-avatar>
        <p>你好，你可以叫我Oslo, 感谢你的访问</p>
        <p>如果你有任何疑问或者需要互增友链，可以在下方留言</p>
        <p>本站资源均为测试/学习使用，请于下载后24h删除</p>
        <p>感谢</p>
        <el-divider/>
        <p>技能</p>
        <div class="tags">
          <el-tag type="success" size="medium">Python</el-tag>
          <el-tag type="info" size="medium">Java</el-tag>
          <el-tag type="warning" size="medium">JavaScript</el-tag>
          <el-tag type="danger" size="medium">Linux</el-tag>
        </div>
        <el-divider></el-divider>
        <div class="tags">
          <p>关注我</p>
          <font-awesome-icon :icon="['fab', 'github']" size="3x" @click="jump('github')" />
          <span style="margin:3px"></span>
          <font-awesome-icon :icon="['fab', 'weibo']" size="3x" @click="jump('weibo')"/>
          <span style="margin:3px"></span>
          <font-awesome-icon :icon="['fab', 'weixin']" size="3x" @mouseover="qrcode = true" @mouseleave="qrcode = false"/>
        </div>
        <img :src="publicQrcode" style="height: 200px;width: 200px;" v-show="qrcode" ref="qrcode" alt="qrcode">
        <el-dialog title="请输入邮箱" :visible.sync="MessageEmailVisible" width="20%">
          <p style="text-align: center">请放心填写,仅做非机器人校验以及回复需要</p>
          <el-form :model="ruleform" status-icon :rules="rules" ref="ruleForm">
            <el-form-item label="" label-width="'30px'" prop="email">
              <el-input v-model="ruleform.email" autocomplete="off"></el-input>
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="MessageEmailVisible = false">取 消</el-button>
            <el-button type="primary" @click="submitForm('ruleForm')">确 定</el-button>
          </div>
        </el-dialog>
        <br/>
        <br/>
        <el-divider></el-divider>
        <h3 style="text-align: left">你可以在这里给我留言(支持MD语法):</h3>
        <div class="message">
          <mavon-editor
            v-model="content"
            ref="md"
            :toolbars="toolbars"
            style="min-height: 300px"
          />
        </div>
        <el-button type="success" style="float: right;margin: 10px" round @click="MessageEmailVisible = true">发送</el-button>
        <div class="show-messages">
          <br/>
          <br/>
          <div v-for="message in messages" :key="message.index">
            <p style="text-align: left">
              <span class="repo-list-description">
                #{{ message.email }}
              </span>
              <span></span>
            </p>
              <div v-html="message.content" v-highlight style="text-align: left">
          </div>
            <p style="text-align: right;">
          <span class="meta-info">
            <i class="el-icon-alarm-clock" />
            {{ message.create_time }}
          </span></p>
            <el-divider/>
          </div>
          <el-pagination
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page="currentPage"
            :page-sizes="[10, 20, 30, 40]"
            :page-size="pageSize"
            layout="total, sizes, prev, pager, next, jumper"
            :total="maxCount">
          </el-pagination>
        </div>
      </el-card>
    </div>
    <el-backtop></el-backtop>
  </div>
</template>

<script>
export default {
  name: 'About',
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
      qrcode: false,
      publicQrcode: require('../static/qrcode.jpeg'),
      maxCount: 1,
      currentPage: 1,
      pageSize: 10,
      messages: [],
      avatar: require('../static/avata.jpeg'),
      rules: {
        email: [
          {
            validator: checkEmail,
            trigger: 'blur'
          }
        ]
      },
      content: '',
      MessageEmailVisible: false,
      ruleform: {
        email: ''
      },
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
        table: false, // 表格
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
  methods: {
    handleSizeChange (val) {
      this.pageSize = val
      this.getMessage()
    },
    handleCurrentChange (val) {
      this.currentPage = val
      this.getMessage()
    },
    jump (index) {
      const actions = new Map([
        ['weibo', ['https://weibo.com/u/5339625147/']],
        ['github', ['http://github.com/oslo254804746/']]
      ])
      window.open(actions.get(index)[0], '_blank')
    },
    getMessage () {
      this.axios.get('/api/messages/?page=' + this.currentPage + '&page_size=' + this.pageSize + '/')
        .then(response => {
          this.maxCount = response.data.count
          if (response.data.results.length > 0) {
            this.messages = response.data.results
          } else {
            this.messages = '暂无留言'
          }
        })
    },
    getDay () {
      var date1 = new Date()
      var year = date1.getFullYear()
      var month = date1.getMonth() + 1
      var day = date1.getDate()
      return year + '-' + month + '-' + day
    },
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
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          const messages = {
            id: 0,
            create_time: this.getTime(),
            emails: this.ruleform.email,
            content: this.content
          }
          this.axios.post('/api/messages/', JSON.stringify(messages))
            .then(response => {
              if (response.status === 201) {
                this.$message({
                  message: '提交留言成功',
                  type: 'success'
                })
                this.MessageEmailVisible = false
                this.messages.push(response.data)
              } else {
                this.$message({
                  message: '提交失败',
                  type: 'warning'
                })
              }
            }
            )
        } else {
          this.$message({
            message: '提交失败',
            type: '错误的邮箱'
          })
        }
      })
    }
  },
  mounted () {
    this.getMessage()
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
.qr_code{
  width: 200px;
  height: 200px;
}
</style>
