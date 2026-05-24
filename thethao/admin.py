from django.contrib import admin
from .models import BaiViet

@admin.register(BaiViet)
class BaiVietAdmin(admin.ModelAdmin):
    list_display = ('tieu_de', 'the_loai', 'ngay_dang', 'tac_gia') # Hiển thị các thông tin này
    list_filter = ('the_loai',) # Tạo bộ lọc theo chủ đề ở cột phải
    search_fields = ('tieu_de',) # Thanh tìm kiếm bài viết