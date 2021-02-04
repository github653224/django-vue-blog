from blogs.apps.apis.models import Blog, Music
import re
import markdown2
import os


def change_clicks(func):
    def wrapeer(request, *args, **kwargs):
        full_path = request.get_full_path()
        id = full_path.split('/')[-2]
        try:
            id = int(id)
        except Exception as e:
            return
        query_blog = Blog.objects.get(id=id)
        query_blog.clicks += 1
        query_blog.save()
        return func(request, *args, **kwargs)

    return wrapeer


def gen_music_src():
    root = '/Users/wangbaofeng/Desktop/Music'
    src_root = '/music/'
    music_list = os.listdir(root + '/mp3')
    lrc_list = os.listdir(root + '/lrc')
    pic_list = os.listdir(root + '/pic')
    for i in music_list:
        if i.split('.')[0] in str(lrc_list) and i.split('.')[0] in str(pic_list):
            j = Music()
            j.lrc = 'http://www.oslozone.cn/music/lrc/%s.lrc' % i.split('.')[0]
            j.src = 'http://www.oslozone.cn/music/mp3/%s' % i
            j.pic = 'http://www.oslozone.cn/music/pic/%s.jpg' % i.split('.')[0]
            j.title = i.split('.')[0]
            j.save()