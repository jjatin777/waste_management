
from rest_framework.urlpatterns import format_suffix_patterns
from w import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.urls import path,include,re_path


urlpatterns = format_suffix_patterns([
	
	path('address/', views.address_list.as_view(), name='address-list'),
	path('address/<int:pk>/',views.address_detail.as_view(),name='address-detail'),
	path('user/',views.user_list.as_view(), name='user-list'),
	path('user/<slug:contact>/',views.user_detail.as_view(),name='user-detail'),
	path('product/',views.product_list.as_view(), name='product-list'),
	path('product/<int:pk>/',views.product_detail.as_view(),name='product-detail'),
	
])

urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
