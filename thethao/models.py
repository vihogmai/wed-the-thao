from django.db import models
from django.contrib.auth.models import User

class BaiViet(models.Model):
    # Bộ danh mục môn thể thao để phân loại bài viết
    CHOICES_THE_LOAI = [
        ('bong_da', 'Bóng Đá'),
        ('bong_ro', 'Bóng Rổ'),
        ('tennis', 'Tennis'),
        ('cau_long', 'Cầu Lông'),
        ('dua_xe', 'Đua Xe F1'),
        ('vo_thuat', 'Võ Thuật'),
        ('esports', 'Esports'),
    ]

    # Các trường dữ liệu cũ phục vụ bài viết (Đầy đủ không thiếu cái nào)
    tieu_de = models.CharField(max_length=200)
    tom_tat = models.TextField()
    noi_dung = models.TextField()
    anh_minh_hoa = models.ImageField(upload_to='anh_tin_tuc/', blank=True, null=True)
    ngay_dang = models.DateTimeField(auto_now_add=True)
    luot_xem = models.IntegerField(default=0)
    tac_gia = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Trường thể loại mới để lọc bài viết
    the_loai = models.CharField(max_length=20, choices=CHOICES_THE_LOAI, default='bong_da')

    def __str__(self):
        return self.tieu_de
