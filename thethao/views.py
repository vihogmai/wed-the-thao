from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import BaiViet

def trang_chu(request):
    # Lọc bài viết theo môn nếu có tham số ?mon=...
    mon = request.GET.get('mon')
    if mon:
        tin_moi = BaiViet.objects.filter(the_loai=mon).order_by('-ngay_dang')
    else:
        tin_moi = BaiViet.objects.all().order_by('-ngay_dang')
    
    # Chỉ truyền những biến mà giao diện thực sự cần
    return render(request, 'trang_chu.html', {
        'tin_moi': tin_moi,
        'tin_doc_nhieu': BaiViet.objects.all().order_by('-luot_xem')[:4],
    })
@login_required(login_url='/dang-nhap/')
@login_required(login_url='/dang-nhap/')
def dang_tin_tu_che(request):
    if request.method == "POST":
        tieu_de = request.POST.get('tieu_de')
        tom_tat = request.POST.get('tom_tat')
        noi_dung = request.POST.get('noi_dung')
        anh_minh_hoa = request.FILES.get('anh_minh_hoa')
        luot_xem = request.POST.get('luot_xem', 0)
        # THÊM DÒNG NÀY:
        the_loai = request.POST.get('the_loai') 

        # Lưu vào Database
        BaiViet.objects.create(
            tieu_de=tieu_de,
            tom_tat=tom_tat,
            noi_dung=noi_dung,
            anh_minh_hoa=anh_minh_hoa,
            luot_xem=luot_xem,
            the_loai=the_loai, # THÊM DÒNG NÀY ĐỂ LƯU VÀO CSDL
            tac_gia=request.user
        )
        return redirect('/')

    return render(request, 'dang_tin.html') # Thẳng hàng với chữ "if" ở trên

# 3. Xử lý Đăng ký thành viên mới
def dang_ky_tai_khoan(request):
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        re_p = request.POST.get('re_password')
        
        if p != re_p:
            return render(request, 'dang_ky.html', {'error': 'Mật khẩu nhập lại không trùng khớp!'})
        if User.objects.filter(username=u).exists():
            return render(request, 'dang_ky.html', {'error': 'Tên tài khoản này đã có người sử dụng!'})
            
        # Tạo tài khoản thành công
        user = User.objects.create_user(username=u, password=p)
        login(request, user) # Đăng ký xong tự động đăng nhập luôn
        return redirect('/')
        
    return render(request, 'dang_ky.html')

# 4. Xử lý Đăng nhập
def dang_nhap_tai_khoan(request):
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('/') # Đăng nhập đúng về trang chủ
        else:
            return render(request, 'dang_nhap.html', {'error': 'Sai tài khoản hoặc mật khẩu rồi bạn ơi!'})
    return render(request, 'dang_nhap.html')

# 5. Xử lý Đăng xuất
def dang_xuat_tai_khoan(request):
    logout(request)
    return redirect('/')