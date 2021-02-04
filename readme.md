# 1 简介

一个简单的博客，使用Django+ Vue, 本人前端很菜，博客只适配了电脑页面，手机页面没适配。

需要Python + Vue环境，数据库采用MySQL,编辑器均采用MarkDown,后台存储markdown格式会自动转换为html
前端页面使用了highlight.js对代码块进行渲染

## 1.1 DEMO网站

可以去我的博客查看DEMO

[OsloZone](http://www.oslozone.cn)

# 2 配置

## 2.1克隆本项目至本地

```bash
git clone https://github.com/oslo254804746/django-vue-blog.git
```



## 2.2 安装依赖

### 2.2.1 安装python依赖

```bash
cd django-backends
pip install -r requirements.txt
```

### 2.2.2 安装vue依赖

```bash
cd blog_front
npm install
```

## 2.3修改配置

### 2.3.1 修改后台数据库

```bash
vim django-backends/blog/blogs/settings.py
```

修改以下配置至你的数据库，如果你使用的ORACLE等，数据库引擎也应该对应修改

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'HOST': '127.0.0.1',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'password',  # 数据库用户密码
        'NAME': 'blog'  # 数据库名字
    }
}
```
同时在同一个文件中修改SECRET_KEY的值，可以随便填或者使用一下方式

```python
import binascii, os
print(binascii.b2a_base64(os.urandom(50)))
```
### 2.3.2迁移数据库

需要提前创建数据库，如果你是使用MySQL

```bash
mysql -uroot -p 
 # 输入密码
mysql> create database blog charset='utf8'; #blog替换为你在上方配置中设置的名字

```



数据库创建好后则可迁移数据库，会自动创建对应数据库

```bash
python manage.py makemigrations
python manage.py migrate
```

迁移完成后，先创建一个superuser,博客的后台管理用的是django-admin自带的，后续对于留言博客等管理均在该页面进行，默认是在你启动django的ip:port/admin/这个Url

```bash
python manage.py createsuperuser  #根据后续提示输入账号密码邮箱等，创建用户
```

### 2.3.3 Tips

#### 1 邮箱回复功能

在django视图函数中，我添加了博客评论邮箱自动回复功能，同时博客留言界面也同样增加了该功能，如果不需要可以按照以下方式进行修改

```python
# 修改前: 具备回复功能
class CommentsView(ModelViewSet):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentsSerializer

    def create(self, request, *args, **kwargs):
        try:
            send_mail(request.data)
        except Exception as e:
            pass
        return super().create(request, *args, **kwargs)

# 修改后:
class CommentsView(ModelViewSet):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentsSerializer
      
```

如果你想使用，你需要增加以下配置
```python
# django-backends/blog/blogs/apps/apis/utils/Mail.py
mail_host = ""  # 设置服务器 邮件发送服务器
mail_user = ""  # 用户名 邮箱账号
mail_pass = ""  # 口令 邮箱密码
sender = '' # 发送人
```

#### 2 背景音乐

我给博客设置了音乐，music连接也是存在数据库中的，如果不需要，可以在前端页面的Index.vue中将该以下代码删除

```vue
# blog_front/src/views/index.vue


      <div class="musicbox">
        <p><i class="el-icon-sugar" /> 来点音乐吧</p>
        <VueAplayer  :music="songlist[0]" :float="true" :shuffle='true' :autoplay="true" :list="songlist" :listFolded="true"  :showLrc='true' />
      </div>

# 同时将下方的请求音乐信息函数删除
  

beforeCreate () {
    this.axios.get('/api/music/')
      .then(response => {
        this.songlist = response.data
      })
  }
```

如果需要使用音乐，你可以通过后台解析返回，或者提前下载好放在服务器，这里就不再赘述，在django-backends/blog/blogs/apps/apis/utils/MusicInfoExtra.py中有一个辅助工具，从mp3文件提取当前音乐封面



# 3 启动

```bash
cd blog_front
npm run serve


cd django_backends/blog/ 
python manage.py runserver
```

# 4 服务器部署

这里提供一个DEMO的 nginx.conf配置，其余部署步骤可以自行搜索一下百度

```nginx
    server {
        listen       80 default_server;
        listen       [::]:80 default_server;
        server_name  _;
        root         /usr/share/nginx/html;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

	location /static/ {
	    alias /root/blog/static/;
	    autoindex on;
	}
	location /music/ {
            alias /Music/;
            autoindex on;
        }
	location /media/ {
	    alias /uploads/;
	    autoindex on;
        }
        location /api/ {
	    uwsgi_pass 127.0.0.1:8000;
	    include uwsgi_params;
        }
	location /admin/ {
	    uwsgi_pass 127.0.0.1:8000;
	    include uwsgi_params;
        }
	location /mdeditor/ {
	    uwsgi_pass 127.0.0.1:8000;
	    include uwsgi_params;
        }
	location / {
	    index index.html;
	    root /www/dist/;
	}
}
```

# 5项目地址

[github](https://github.com/oslo254804746/django-vue-blog)

[gitee](https://gitee.com/oslo254804746/django-vue-blog)

