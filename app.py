import streamlit as st
import random
import time

# Cấu hình giao diện trang web
st.set_page_config(page_title="Cuộc Đua Vịt Kịch Tính", page_icon="🦆", layout="centered")

st.title("🦆 Cuộc Đua Vịt Trực Tuyến 🦆")
st.write("Nhập tên và bấm nút để xem các chú vịt bứt tốc về đích!")

# Ô nhập tên các đấu thủ
input_names = st.text_area("Danh sách đấu thủ đua vịt (mỗi dòng một tên):", value="Vịt Vàng\nVịt Xanh\nVịt Đen\nVịt Hồng")

if st.button("Bắt Đầu Đua!", type="primary"):
    names = [name.strip() for name in input_names.split("\n") if name.strip()]
    
    if len(names) < 2:
        st.error("Bạn cần nhập ít nhất 2 chú vịt để bắt đầu cuộc đua!")
    else:
        st.write("### 🏁 ĐƯỜNG ĐUA ĐANG DIỄN RA... 🏁")
        
        # Khởi tạo vị trí ban đầu của các chú vịt (0%)
        positions = {name: 0 for name in names}
        
        # Tạo danh sách các ô hiển thị động cố định trên màn hình
        lanes = {}
        for name in names:
            st.write(f"**{name}**")
            lanes[name] = st.progress(0) # Dùng thanh tiến trình làm đường đua
            
        race_over = False
        winner = ""
        
        # Vòng lặp chạy cuộc đua trực quan
        while not race_over:
            time.sleep(0.2) # Tạo khoảng dừng 0.2 giây giữa mỗi bước để mắt người nhìn kịp
            
            for name in names:
                # Mỗi lượt tiến ngẫu nhiên từ 5 đến 15 bước
                positions[name] += random.randint(5, 15)
                
                # Giới hạn tối đa là 100% đường đua
                if positions[name] > 100:
                    positions[name] = 100
                    
                # Cập nhật thanh tiến trình chạy ngay trên màn hình mà không bị đứng im
                lanes[name].progress(positions[name])
                
                # Kiểm tra nếu chú vịt này chạm đích (100%)
                if positions[name] >= 100 and not race_over:
                    race_over = True
                    winner = name
                    
        # Báo cáo kết quả rực rỡ khi cuộc đua kết thúc
        st.balloons() # Hiệu ứng bóng bay ăn mừng người chiến thắng
        st.success(f"🎉 Chúc mừng chiến thắng: 🏆 **{winner}** 🏆 đã về đích đầu tiên!")
