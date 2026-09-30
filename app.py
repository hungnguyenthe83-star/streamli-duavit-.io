import streamlit as st

# Cấu hình giao diện trang web
st.set_page_config(page_title="Cuộc Đua Vịt Hoạt Họa 3D", page_icon="🦆", layout="centered")

st.title("🏖️ Cuộc Đua Vịt dàng cho mấy đứa chơi casino🐧 🎈")
st.write("Nhập tên đấu thủ và xem các chú vịt 🦆!")

# Ô nhập tên các đấu thủ đua vịt
input_names = st.text_area("Danh sách đấu thủ (mỗi dòng một tên):", value="Vịt Vàng\nVịt Xanh\nVịt Đỏ\nVịt Hồng")

if st.button("Bắt Đầu Đua!", type="primary"):
    names = [name.strip() for name in input_names.split("\n") if name.strip()]
    
    if len(names) < 2:
        st.error("Bạn cần nhập ít nhất 2 chú vịt để bắt đầu cuộc đua!")
    else:
        js_names = str(names)
        
        # Nhúng toàn bộ mã HTML/CSS/JS tạo mô hình hoạt họa vịt chạy
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
                    perspective: 600px;
                }}
                /* Đường đua bãi biển góc nghiêng 3D */
                .track-container {{
                    background: linear-gradient(to bottom, #4fc3f7 0%, #4fc3f7 65%, #ffe082 65%, #ffe082 100%);
                    border: 4px solid #0288d1;
                    border-radius: 12px;
                    padding: 30px 10px;
                    position: relative;
                    transform: rotateX(15deg);
                    box-shadow: 0 15px 30px rgba(0,0,0,0.2), inset 0 0 20px rgba(0,0,0,0.1);
                }}
                .lane {{
                    position: relative;
                    height: 70px;
                    margin-bottom: 15px;
                    border-bottom: 2px dashed rgba(255,255,255,0.4);
                    display: flex;
                    align-items: center;
                }}
                .duck-3d-box {{
                    position: absolute;
                    left: 0px;
                    width: 50px;
                    height: 50px;
                    transition: left 0.1s linear;
                    z-index: 2;
                    transform-style: preserve-3d;
                }}
                /* Hiệu ứng HOẠT HỌA CHẠY BỘ (Animation) */
                .duck-body {{
                    font-size: 38px;
                    position: relative;
                    text-shadow: 3px 3px 0px #f57f17, 6px 6px 5px rgba(0,0,0,0.3);
                    /* Gọi hiệu ứng running: chạy liên tục trong 0.25 giây, đổi chiều liên tục */
                    animation: running 0.25s infinite alternate ease-in-out;
                    transform-origin: bottom center;
                }}
                /* Hoạt họa bóng đổ co giãn theo nhịp chạy của vịt */
                .duck-shadow {{
                    position: absolute;
                    bottom: -2px;
                    left: 5px;
                    width: 32px;
                    height: 8px;
                    background: rgba(0, 0, 0, 0.25);
                    border-radius: 50%;
                    filter: blur(2px);
                    z-index: 1;
                    animation: shadow-change 0.25s infinite alternate ease-in-out;
                }}
                /* Định nghĩa hành động chạy bộ kịch tính */
                @keyframes running {{
                    0% {{ 
                        transform: scaleY(0.9) scaleX(1.05) rotate(-8deg) translateY(0); 
                    }}
                    50% {{
                        transform: scaleY(1.05) scaleX(0.95) rotate(0deg) translateY(-8px); /* Vịt bật nhảy lên cao */
                    }}
                    100% {{ 
                        transform: scaleY(0.9) scaleX(1.05) rotate(8deg) translateY(0); /* Vịt giậm chân đổi bên */
                    }}
                }}
                /* Định nghĩa bóng nhỏ lại khi vịt nhảy lên cao */
                @keyframes shadow-change {{
                    0% {{ transform: scale(1); opacity: 1; }}
                    50% {{ transform: scale(0.7); opacity: 0.5; }}
                    100% {{ transform: scale(1); opacity: 1; }}
                }}
                .duck-name {{
                    position: absolute;
                    top: -12px;
                    left: 50px;
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
                }}
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
                const maxRight = track.clientWidth - 110; 

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
        
        st.components.v1.html(html_code, height=600)



