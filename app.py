import streamlit as st
import random
import time

# Cấu hình tiêu đề trang web
st.set_page_config(page_title="Cuộc sòng bài Đua Vịt", page_icon="🦆", layout="centered")

st.title("🦆 Cuộc Đua Vịt Trực Tuyến 🦆")

# Khung nhập tên người chơi
input_names = st.text_area("Nhập tên các đấu thủ (mỗi dòng một tên):", value="Vịt Vàng\nVịt Xanh\nVịt Đen")

if st.button("Bắt Đầu Đua!", type="primary"):
    # Tách tên người chơi thành danh sách
    names = [name.strip() for name in input_names.split("\n") if name.strip()]
    
    if len(names) < 2:
        st.error("Bạn cần nhập ít nhất 2 chú vịt để bắt đầu cuộc đua!")
    else:
        st.write("---")
        # Khởi tạo vị trí ban đầu của các chú vịt (0 bước)
        positions = {name: 0 for name in names}
        
        # Tạo các khung hiển thị động cho từng chú vịt
        placeholders = {name: st.empty() for name in names}
        winner_announce = st.empty()
        
        race_over = False
        winner = ""
        
        # Vòng lặp cuộc đua
        while not race_over:
            time.sleep(0.1) # Tốc độ cập nhật khung hình
            
            for name in names:
                # Mỗi lượt vịt tiến ngẫu nhiên từ 1 đến 5 bước
                positions[name] += random.randint(1, 5)
                
                # Tạo hiệu ứng khoảng trống di chuyển bằng dấu gạch ngang hoặc khoảng trắng
                spaces = "   " * positions[name]
                placeholders[name].markdown(f"| {spaces} 🦆 **{name}**")
                
                # Kiểm tra nếu có vịt chạm đích (đạt 20 bước)
                if positions[name] >= 20:
                    race_over = True
                    winner = name
                    break
                    
        # Hiển thị người chiến thắng
        winner_announce.success(f"🎉 Người chiến thắng: 🏆 **{winner}** 🏆")
