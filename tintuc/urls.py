from django.contrib import admin
from django.urls import path
from thethao import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.trang_chu, name='trang_chu'),
    path('dang-tin/', views.dang_tin_tu_che, name='dang_tin'),
    path('dang-ky/', views.dang_ky_tai_khoan, name='dang_ky'),
    path('dang-nhap/', views.dang_nhap_tai_khoan, name='dang_nhap'),
    path('dang-xuat/', views.dang_xuat_tai_khoan, name='dang_xuat'),
]

# Chỉ thêm phần này để chạy ảnh khi đang trong chế độ DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)