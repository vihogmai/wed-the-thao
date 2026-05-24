from django.shortcuts import render
from .models import BaiViet, BangDiem

def trang_chu(request):
    # Lấy toàn bộ bài viết, xếp bài mới đăng lên đầu
    tin_moi = BaiViet.objects.all().order_by('-ngay_dang')
    
    # Lấy top 4 bài viết có lượt xem nhiều nhất cho cột phải
    tin_doc_nhieu = BaiViet.objects.all().order_by('-luot_xem')[:4]
    
    # Lấy danh sách bảng điểm sắp xếp từ điểm cao xuống thấp
    bang_diem = BangDiem.objects.all().order_by('-diem_so')
    
    return render(request, 'trang_chu.html', {
        'tin_moi': tin_moi,
        'tin_doc_nhieu': tin_doc_nhieu,
        'bang_diem': bang_diem
    })
