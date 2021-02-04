from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from blogs.apps.apis.models import Blog, BlogCatgory, BlogComment, Messages, FriendsLink, Music
from .serializer import IndexBlogSerializer, CategoryDetailSerializer, BlogDetailSerializer, BlogCommentsSerializer, \
    MessageSerializer, FriendsLinkSerializer, MusicSerializer
from blogs.apps.apis.utils.Mail import send_mail, reply_message_mail
from django.utils.decorators import method_decorator
from blogs.apps.apis.utils.utils import change_clicks


class IndexBlogPaginator(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = 'page'


class IndexBlogView(ModelViewSet):
    queryset = Blog.objects.order_by('-publish_time')
    pagination_class = IndexBlogPaginator
    serializer_class = IndexBlogSerializer


class CategoryDetailView(ModelViewSet):
    queryset = BlogCatgory.objects.all()
    serializer_class = CategoryDetailSerializer


@method_decorator(change_clicks, name='retrieve')
class BlogDetailView(ModelViewSet):
    queryset = Blog.objects.order_by('-publish_time')
    serializer_class = BlogDetailSerializer


class CommentsView(ModelViewSet):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentsSerializer

    def create(self, request, *args, **kwargs):
        try:
            send_mail(request.data)
        except Exception as e:
            pass
        return super().create(request, *args, **kwargs)


class HotBlogPaginator(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    page_query_param = 'page'


class HotBlogsView(ModelViewSet):
    queryset = Blog.objects.order_by('-clicks')
    serializer_class = IndexBlogSerializer
    pagination_class = HotBlogPaginator


class SearchBlog(APIView):
    def get(self, request):
        param = request.GET.get("param")
        if not param:
            return JsonResponse({'error': 'Not Found'}, safe=False)
        query_set = Blog.objects.filter(
            Q(title__contains=param) | Q(contents__contains=param) | Q(summary__contains=param))
        if query_set:
            serializer = IndexBlogSerializer(query_set, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({'error': 'Not Found'}, safe=False)


class MessagePaginator(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'


class MessageView(ModelViewSet):
    queryset = Messages.objects.all().order_by('-create_time')
    pagination_class = MessagePaginator
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        try:
            reply_message_mail(request.data)
        except Exception as e:
            pass
        return super().create(request, *args, **kwargs)


class FriendsLinkView(ModelViewSet):
    queryset = FriendsLink.objects.all().order_by('id')
    serializer_class = FriendsLinkSerializer


class MusicLinks(ModelViewSet):
    queryset = Music.objects.all().order_by('id')
    serializer_class = MusicSerializer
