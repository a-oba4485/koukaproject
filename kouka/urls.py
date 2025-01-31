from django.urls import path
from . import views

app_name = 'kouka'

urlpatterns = [
	path('',views.IndexView.as_view(), name='index'),
    path('post/', views.CreatePhotoView.as_view(), name='post'),
    path('post_done/',
    views.PostSuccessView.as_view(),
    name='post_done'),
    path('photos/<int:category>',
    views.CategoryView.as_view(),
    name = 'photos_cat'
    ),
    path('user-list/<int:user>',
    views.UserView.as_view(),
    name = 'user_list'
    ),

    path('mypage/', views.MypageView.as_view(), name = 'mypage'),
    path('photo/<int:pk>/delete/',
    views.PhotoDeleteView.as_view(),
    name = 'photo_delete'
    ),

    path('photo-detail/<int:pk>/', views.DynamicDetailView.as_view(), name='photo_detail'),

    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('keijiban/', views.KeijibanView.as_view(), name='keijiban'),
    path('add_comment/', views.AddCommentView.as_view(), name='add_comment'),
]


