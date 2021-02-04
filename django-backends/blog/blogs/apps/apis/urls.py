from django.urls import path
from .views import IndexBlogView, CategoryDetailView, BlogDetailView, CommentsView,\
    HotBlogsView, SearchBlog, MessageView,FriendsLinkView, MusicLinks

urlpatterns = [
    path('listBlogs/', IndexBlogView.as_view({'get': 'list'})),
    path('categorydetails/', CategoryDetailView.as_view({'get': 'list'})),
    path('blogDetails/<int:pk>/', BlogDetailView.as_view({'get': 'retrieve'})),
    path('addComments/', CommentsView.as_view({'post': 'create'})),
    path("hotBlogs/",HotBlogsView.as_view({'get': 'list'})),
    path("searchBlogs/", SearchBlog.as_view()),
    path("messages/", MessageView.as_view({'get': 'list', 'post': 'create'})),
    path("friendslink/", FriendsLinkView.as_view({'get': 'list'})),
    path("music/", MusicLinks.as_view({'get': 'list'}))
]
