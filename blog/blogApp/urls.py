from django.urls import path
from blogApp.views import CategoryListView, CategoryDetailView, BlogListView, BlogDetailView

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category-detail'),
    path('blog/', BlogListView.as_view(), name='blog-list'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
]

# urlpatterns = [
#     path('category/', CategoryList.as_view(), name='category-list'),
#     path('category/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
#     path('blogs/', BlogList.as_view(), name='blog-list'),
#     path('blogs/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
# ]