import markdown2
from django.db import models
from mdeditor.fields import MDTextField


# Create your models here.
class BlogCatgory(models.Model):
    name = models.CharField(max_length=10, null=False, verbose_name='分类名')

    class Meta:
        # 指定表名
        db_table = 'catgory'
        managed = True

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100, null=False, verbose_name='博客标题')
    summary = models.CharField(max_length=400, null=False, verbose_name='博客摘要')
    category = models.IntegerField(verbose_name='博客分类')
    publish_time = models.DateField(auto_now_add=True, verbose_name='发布日期')
    contents = MDTextField(default='', verbose_name='内容')
    clicks = models.IntegerField(default=0, verbose_name='点击')

    class Meta:
        db_table = 'Blog'
        managed = True

    def __str__(self):
        return "{'id': %d, 'title': %s}" % (self.id, self.title)

    @property
    def category_name(self):
        return BlogCatgory.objects.get(id=self.category).name


class BlogComment(models.Model):
    blog_id = models.IntegerField(verbose_name='博客id', )
    create_time = models.DateTimeField(auto_created=True)
    emails = models.CharField(max_length=50, null=True, verbose_name='邮箱')
    ip = models.CharField(max_length=20, null=True, verbose_name='留言ip')
    content = models.CharField(max_length=200, null=True, verbose_name='留言内容')

    class Meta:
        db_table = 'Comment'
        managed = True

    def __str__(self):
        return "{'emails': %s, 'time': %s, 'content': %s}" % (self.emails, self.create_time, self.content)


class Messages(models.Model):
    # todo 保存时邮箱还需要调整
    emails = models.CharField(max_length=50, null=True, verbose_name='留言邮箱')
    content = MDTextField(default='', verbose_name='留言MD内容', null=True)
    create_time = models.DateTimeField(auto_created=True)

    class Meta:
        db_table = 'Messages'
        managed = True

    def __str__(self):
        return str(self.create_time) + self.emails


class FriendsLink(models.Model):
    url = models.CharField(max_length=50, null=False, verbose_name='友链链接')
    name = models.CharField(max_length=50, null=False, verbose_name='友链名称')
    is_use = models.IntegerField(null=True, blank=True, verbose_name='是否是使用')

    class Meta:
        db_table = 'FriendsLink'
        managed = True

    def __str__(self):
        return self.name


class Music(models.Model):
    title = models.CharField(max_length=50, null=False, verbose_name='歌曲名称')
    src = models.CharField(max_length=100, null=False, verbose_name='音频url')
    pic = models.CharField(max_length=100, null=False, verbose_name='封面url')
    lrc = models.CharField(max_length=100, null=False, verbose_name='歌词url')
    artist = models.CharField(max_length=100, null=False, verbose_name='作者')

    class Meta:
        db_table = 'Music'
        managed = True

    def __str__(self):
        return self.title
