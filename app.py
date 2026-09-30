import streamlit as st

# Cấu hình giao diện trang web
st.set_page_config(page_title="Cuộc Đua Vịt Bãi Biển", page_icon="🦆", layout="centered")

st.title("🏖️ Cuộc Đua Vịt Bãi Biển Siêu Mượt 🎈")
st.write("Nhập tên đấu thủ và xem các chú vịt bứt tốc 60 FPS về đích!")

# Ô nhập tên các đấu thủ đua vịt
input_names = st.text_area("Danh sách đấu thủ (mỗi dòng một tên):", value="Vịt Vàng\nVịt Xanh\nVịt Đen\nVịt Hồng")

if st.button("Bắt Đầu Đua!", type="primary"):
    names = [name.strip() for name in input_names.split("\n") if name.strip()]
    
    if len(names) < 2:
        st.error("Bạn cần nhập ít nhất 2 chú vịt để bắt đầu cuộc đua!")
    else:
        js_names = str(names)
        
        # Nhúng toàn bộ mã HTML/CSS/JS bãi biển và bóng bay mượt mà vào Streamlit
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
                }}
                /* Thiết kế đường đua màu cát biển xanh */
                .track-container {{
                    background: linear-gradient(to bottom, #4fc3f7 0%, #4fc3f7 70%, #ffe082 70%, #ffe082 100%);
                    border: 4px solid #0288d1;
                    border-radius: 12px;
                    padding: 20px 10px;
                    position: relative;
                    box-shadow: inset 0 0 20px rgba(0,0,0,0.1);
                }}
                .lane {{
                    position: relative;
                    height: 50px;
                    margin-bottom: 15px;
                    border-bottom: 2px dashed rgba(255,255,255,0.5);
                    display: flex;
                    align-items: center;
                }}
                .duck {{
                    position: absolute;
                    left: 0px;
                    font-size: 32px;
                    transition: left 0.1s linear;
                    z-index: 2;
                }}
                .duck-name {{
                    background: rgba(255,255,255,0.9);
                    padding: 2px 6px;
                    border-radius: 8px;
                    font-size: 12px;
                    font-weight: bold;
                    margin-left: 35px;
                    white-space: nowrap;
                    border: 1px solid #ffb300;
                    display: inline-block;
                }}
                .finish-line {{
                    position: absolute;
                    right: 40px;
                    top: 0;
                    bottom: 0;
                    width: 15px;
                    background: repeating-linear-gradient(45deg, #fff, #fff 5px, #000 5px, #000 10px);
                }}
                .winner-text {{
                    text-align: center;
                    font-size: 26px;
                    font-weight: bold;
                    color: #d81b60;
                    margin-top: 20px;
                    display: none;
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
                const maxRight = track.clientWidth - 90; 

                // Tạo các làn đua vịt bãi biển
                names.forEach((name, index) => {{
                    const lane = document.createElement('div');
                    lane.className = 'lane';
                    
                    const duck = document.createElement('div');
                    duck.className = 'duck';
                    duck.innerHTML = '🦆<span class="duck-name">' + name + '</span>';
                    
                    lane.appendChild(duck);
                    track.appendChild(lane);
                    
                    duckData.push({{ element: duck, name: name, pos: 0 }});
                }});

                // Hàm tạo bùng nổ bóng bay 🎈 ngay lập tức
                function spawnBalloons() {{
                    for(let i = 0; i < 40; i++) {{
                        setTimeout(() => {{
                            const balloon = document.createElement('div');
                            balloon.className = 'balloon';
                            balloon.innerText = '🎈';
                            balloon.style.left = Math.random() * 95 + '%';
                            // Tạo tốc độ bay ngẫu nhiên cho tự nhiên
                            balloon.style.animationDuration = (Math.random() * 2 + 2) + 's'; 
                            document.body.appendChild(balloon);
                        }}, i * 80); // Cứ mỗi 80 mili giây lại có bóng mới bay lên
                    }}
                }}

                // Vòng lặp cuộc đua 60fps siêu mượt
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
                            
                            // Hiện người thắng và thả bóng bay lập tức!
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
        
        # Nhúng HTML vào Streamlit [Streamlit Components API Reference]
        st.components.v1.html(html_code, height=550)


