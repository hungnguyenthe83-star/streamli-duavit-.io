import streamlit as st

# Cấu hình giao diện trang web
st.set_page_config(page_title="Cuộc Đua Vịt 3D Bãi Biển", page_icon="🦆", layout="centered")

st.title("🏖️ Cuộc Đua Vịt 3D Bãi Biển Siêu Nhẹ 🎈")
st.write("Nhập tên đấu thủ và xem các chú vịt 3D bứt tốc về đích!")

# Ô nhập tên các đấu thủ đua vịt
input_names = st.text_area("Danh sách đấu thủ (mỗi dòng một tên):", value="Vịt Vàng\nVịt Xanh\nVịt Đỏ\nVịt Hồng")

if st.button("Bắt Đầu Đua!", type="primary"):
    names = [name.strip() for name in input_names.split("\n") if name.strip()]
    
    if len(names) < 2:
        st.error("Bạn cần nhập ít nhất 2 chú vịt để bắt đầu cuộc đua!")
    else:
        js_names = str(names)
        
        # Nhúng toàn bộ mã HTML/CSS/JS tạo mô hình vịt 3D hiệu ứng chiều sâu bằng mã thuần
        html_code = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: sans-serif;
                    background: #f0f8ff;
                    margin: 0;
                    padding: 10px;
                    overflow: hidden;
                    perspective: 600px; /* Tạo không gian 3D sâu cho trình duyệt */
                }}
                /* Thiết kế đường đua bãi biển góc nghiêng 3D */
                .track-container {{
                    background: linear-gradient(to bottom, #4fc3f7 0%, #4fc3f7 65%, #ffe082 65%, #ffe082 100%);
                    border: 4px solid #0288d1;
                    border-radius: 12px;
                    padding: 30px 10px;
                    position: relative;
                    transform: rotateX(15deg); /* Nghiêng đường đua tạo cảm giác 3D */
                    box-shadow: 0 15px 30px rgba(0,0,0,0.2), inset 0 0 20px rgba(0,0,0,0.1);
                }}
                .lane {{
                    position: relative;
                    height: 65px;
                    margin-bottom: 15px;
                    border-bottom: 2px dashed rgba(255,255,255,0.4);
                    display: flex;
                    align-items: center;
                }}
                /* Tạo mô hình Vịt 3D nhẹ máy từ CSS */
                .duck-3d-box {{
                    position: absolute;
                    left: 0px;
                    width: 40px;
                    height: 40px;
                    transition: left 0.1s linear;
                    z-index: 2;
                    transform-style: preserve-3d;
                }}
                /* Hình khối thân vịt 3D có đổ bóng khối */
                .duck-body {{
                    font-size: 36px;
                    position: relative;
                    text-shadow: 3px 3px 0px #f57f17, 6px 6px 5px rgba(0,0,0,0.3); /* Tạo khối 3D giả lập cho Emoji */
                    animation: waddle 0.2s infinite alternate ease-in-out; /* Hiệu ứng vịt lắc lư đi bộ */
                }}
                /* Hiệu ứng bóng đổ dưới chân vịt trên cát */
                .duck-shadow {{
                    position: absolute;
                    bottom: -5px;
                    left: 5px;
                    width: 30px;
                    height: 8px;
                    background: rgba(0, 0, 0, 0.2);
                    border-radius: 50%;
                    filter: blur(2px);
                    z-index: 1;
                }}
                .duck-name {{
                    position: absolute;
                    top: -15px;
                    left: 45px;
                    background: rgba(255,255,255,0.95);
                    padding: 2px 8px;
                    border-radius: 8px;
                    font-size: 11px;
                    font-weight: bold;
                    white-space: nowrap;
                    border: 1px solid #ffb300;
                    box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
                }}
                .finish-line {{
                    position: absolute;
                    right: 50px;
                    top: 0;
                    bottom: 0;
                    width: 15px;
                    background: repeating-linear-gradient(45deg, #fff, #fff 5px, #000 5px, #000 10px);
                    box-shadow: 2px 0 5px rgba(0,0,0,0.2);
                }}
                .winner-text {{
                    text-align: center;
                    font-size: 26px;
                    font-weight: bold;
                    color: #d81b60;
                    margin-top: 20px;
                    display: none;
                    text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
                }}
                /* Định nghĩa bước đi lắc lư của vịt */
                @keyframes waddle {{
                    0% {{ transform: rotate(-6deg) translateY(0); }}
                    100% {{ transform: rotate(6deg) translateY(-4px); }}
                }}
                /* Cấu hình bóng bay 🎈 */
                .balloon {{
                    position: fixed;
                    bottom: -100px;
                    font-size: 50px;
                    animation: floatUp 3s linear forwards;
                    z-index: 9999;
                    pointer-events: none;
                }}
                @keyframes floatUp {{
                    0% {{ bottom: -100px; transform: translateX(0) rotate(0deg); opacity: 1; }}
                    50% {{ transform: translateX(50px) rotate(15deg); }}
                    100% {{ bottom: 105vh; transform: translateX(-50px) rotate(-15deg); opacity: 0; }}
                }}
            </style>
        </head>
        <body>

            <div class="track-container" id="track">
                <div class="finish-line"></div>
            </div>
            <div class="winner-text" id="winnerAnnounce"></div>

            <script>
                const names = {js_names};
                const track = document.getElementById('track');
                const winnerAnnounce = document.getElementById('winnerAnnounce');
                
                const duckData = [];
                const maxRight = track.clientWidth - 100; 

                // Tạo các làn đua vịt 3D
                names.forEach((name, index) => {{
                    const lane = document.createElement('div');
                    lane.className = 'lane';
                    
                    const box = document.createElement('div');
                    box.className = 'duck-3d-box';
                    
                    box.innerHTML = `
                        <div class="duck-shadow"></div>
                        <div class="duck-body">🦆</div>
                        <span class="duck-name">${{name}}</span>
                    `;
                    
                    lane.appendChild(box);
                    track.appendChild(lane);
                    
                    duckData.push({{ element: box, name: name, pos: 0 }});
                }});

                // Hàm tạo bùng nổ bóng bay 🎈 ngay lập tức
                function spawnBalloons() {{
                    for(let i = 0; i < 40; i++) {{
                        setTimeout(() => {{
                            const balloon = document.createElement('div');
                            balloon.className = 'balloon';
                            balloon.innerText = '🎈';
                            balloon.style.left = Math.random() * 95 + '%';
                            balloon.style.animationDuration = (Math.random() * 2 + 2) + 's'; 
                            document.body.appendChild(balloon);
                        }}, i * 80);
                    }}
                }}

                // Vòng lặp cuộc đua siêu mượt
                let raceOver = false;
                const interval = setInterval(() => {{
                    if (raceOver) return;

                    duckData.forEach(duck => {{
                        const step = Math.random() * 4 + 1; 
                        duck.pos += step;
                        duck.element.style.left = duck.pos + 'px';

                        if (duck.pos >= maxRight && !raceOver) {{
                            raceOver = true;
                            clearInterval(interval);
                            
                            winnerAnnounce.innerHTML = "🎉 Người chiến thắng: 🏆 <strong>" + duck.name + "</strong> 🏆";
                            winnerAnnounce.style.display = "block";
                            spawnBalloons();
                        }}
                    }});
                }}, 30); 
            </script>
        </body>
        </html>
        """
        
        # Nhúng HTML vào Streamlit
        st.components.v1.html(html_code, height=580)


