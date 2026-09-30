import streamlit as st
import random
import time

# Cấu hình giao diện trang web
st.set_page_config(page_title="Cuộc Đua Vịt Kịch Tính", page_icon="🦆", layout="centered")

st.title("🦆 Cuộc Đua Vịt Di Chuyển Trực Tuyến 🦆")
st.write("Nhập tên đấu thủ và xem các chú vịt 🦆 thi nhau chạy về đích!")

# Ô nhập tên các đấu thủ đua vịt
input_names = st.text_area("Danh sách đấu thủ (mỗi dòng một tên):", value="Vịt Vàng\nVịt Xanh\nVịt Đen\nVịt Hồng")

if st.button("Bắt Đầu Đua!", type="primary"):
    names = [name.strip() for name in input_names.split("\n") if name.strip()]
    
    if len(names) < 2:
        st.error("Bạn cần nhập ít nhất 2 chú vịt để bắt đầu cuộc đua!")
    else:
        st.write("### 🏁 ĐƯỜNG ĐUA KỊCH TÍNH... 🏁")
        
        # Đích đến là 30 bước di chuyển
        finish_line = 30
        positions = {name: 0 for name in names}
        
        # Tạo các ô trống động trên màn hình cho từng đấu thủ
        lanes = {name: st.empty() for name in names}
        winner_announce = st.empty()
        
        # Hiển thị vạch xuất phát ban đầu cho tất cả vịt
        for name in names:
            lanes[name].markdown(f"🏁 🦆 **{name}**")
            
        race_over = False
        winner = ""
        
        # Vòng lặp điều khiển chú vịt chạy bộ
        while not race_over:
            time.sleep(0.15) # Tốc độ nhảy bước của vịt (0.15 giây một lần)
            
            for name in names:
                # Mỗi lượt vịt tiến ngẫu nhiên từ 1 đến 3 bước
                positions[name] += random.randint(1, 3)
                
                # Giới hạn không cho vượt quá vạch đích
                if positions[name] > finish_line:
                    positions[name] = finish_line
                
                # Tạo chuỗi khoảng trắng để đẩy chú vịt dịch chuyển về bên phải
                # Càng nhiều bước, khoảng trắng càng dài, vịt chạy càng xa
                spaces = "&nbsp;" * (positions[name] * 4) 
                
                # Cập nhật hình ảnh chú vịt đang chạy trực quan lên màn hình
                lanes[name].markdown(f"🏁{spaces}🦆 **{name}**")
                
                # Kiểm tra xem chú vịt nào chạm đích trước
                if positions[name] >= finish_line and not race_over:
                    race_over = True
                    winner = name
        
        # Hiệu ứng bắn pháo hoa ăn mừng người chiến thắng
        st.snow() 
        winner_announce.success(f"🎉 Người chiến thắng: 🏆 **{winner}** 🏆 đã về đích đầu tiên!")

