import json
from typing import Dict, Any, List, Optional

# 预定义的场景模板
SCENE_TEMPLATES = {
    "cozy": """
    <svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
        <rect width="800" height="600" fill="#f5f0e6"/>
        <rect x="50" y="50" width="700" height="500" rx="10" fill="#ffffff" stroke="#e0d6c8" stroke-width="2"/>
        <rect x="100" y="150" width="300" height="350" rx="5" fill="#f9f6f2" stroke="#e0d6c8" stroke-width="1"/>
        <circle cx="650" cy="200" r="80" fill="#ffead7"/>
        <rect x="550" y="350" width="150" height="100" rx="5" fill="#f0e6d8"/>
        <text x="400" y="100" font-family="Arial" font-size="24" text-anchor="middle" fill="#6d5c4d">温馨阅读</text>
        
        <!-- 猫咪元素 -->
        <g id="cat" transform="translate(180, 400) scale(0.8)">
            <circle cx="0" cy="0" r="25" fill="#F9B572"/>
            <circle cx="-8" cy="-10" r="5" fill="#FFFFFF"/>
            <circle cx="8" cy="-10" r="5" fill="#FFFFFF"/>
            <circle cx="-8" cy="-10" r="2" fill="#333333"/>
            <circle cx="8" cy="-10" r="2" fill="#333333"/>
            <path d="M-10,5 Q0,12 10,5" stroke="#333333" stroke-width="1.5" fill="none"/>
            <path id="tail" d="M-5,-20 Q-30,-40 -40,-20" stroke="#F9B572" stroke-width="10" fill="none"/>
            <path d="M-18,-28 L-25,-35 M18,-28 L25,-35" stroke="#F9B572" stroke-width="4" fill="none"/>
        </g>
        
        <!-- 交互脚本 -->
        <script type="text/ecmascript">
            // 添加滚动事件监听
            document.addEventListener('scroll', function() {
                const scrollPercent = window.scrollY / (document.body.scrollHeight - window.innerHeight);
                const tail = document.getElementById("tail");
                
                // 根据滚动位置改变猫咪尾巴形状
                if(scrollPercent > 0.7) {
                    tail.setAttribute("d", "M-5,-20 Q-10,-45 -30,-35");
                } else if(scrollPercent > 0.4) {
                    tail.setAttribute("d", "M-5,-20 Q-20,-30 -35,-15");
                } else {
                    tail.setAttribute("d", "M-5,-20 Q-30,-40 -40,-20");
                }
            });
            
            // 添加鼠标移动交互
            document.addEventListener('mousemove', function(e) {
                const cat = document.getElementById("cat");
                const svgRect = cat.viewportElement.getBoundingClientRect();
                const mouseX = e.clientX - svgRect.left;
                const mouseY = e.clientY - svgRect.top;
                
                // 猫咪眼睛跟随鼠标
                const leftEye = document.getElementById("cat").children[3];
                const rightEye = document.getElementById("cat").children[4];
                
                // 计算眼睛移动方向
                const catX = 180;
                const catY = 400;
                const eyeMovementX = (mouseX - catX) / 100;
                const eyeMovementY = (mouseY - catY) / 100;
                
                // 限制眼球移动范围
                const maxMove = 2;
                const moveX = Math.max(-maxMove, Math.min(maxMove, eyeMovementX));
                const moveY = Math.max(-maxMove, Math.min(maxMove, eyeMovementY));
                
                leftEye.setAttribute("cx", -8 + moveX);
                leftEye.setAttribute("cy", -10 + moveY);
                rightEye.setAttribute("cx", 8 + moveX);
                rightEye.setAttribute("cy", -10 + moveY);
            });
        </script>
    </svg>
    """,
    "outdoor": """
    <svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
        <rect width="800" height="600" fill="#e8f4fc"/>
        <rect x="0" y="400" width="800" height="200" fill="#7cba92"/>
        <circle cx="700" cy="100" r="60" fill="#ffeb5b"/>
        <path d="M100,400 L200,300 L300,400 Z" fill="#527a58"/>
        <path d="M300,400 L400,250 L500,400 Z" fill="#3d5e43"/>
        <rect x="550" y="350" width="150" height="50" rx="5" fill="#e6c28f"/>
        <text x="400" y="100" font-family="Arial" font-size="24" text-anchor="middle" fill="#3a6582">户外阅读</text>
        
        <!-- 猫咪元素 -->
        <g id="cat" transform="translate(600, 360) scale(0.7)">
            <circle cx="0" cy="0" r="25" fill="#F9B572"/>
            <circle cx="-8" cy="-10" r="5" fill="#FFFFFF"/>
            <circle cx="8" cy="-10" r="5" fill="#FFFFFF"/>
            <circle cx="-8" cy="-10" r="2" fill="#333333"/>
            <circle cx="8" cy="-10" r="2" fill="#333333"/>
            <path d="M-10,5 Q0,12 10,5" stroke="#333333" stroke-width="1.5" fill="none"/>
            <path id="tail" d="M-5,-20 Q-30,-40 -40,-20" stroke="#F9B572" stroke-width="10" fill="none"/>
            <path d="M-18,-28 L-25,-35 M18,-28 L25,-35" stroke="#F9B572" stroke-width="4" fill="none"/>
        </g>
        
        <!-- 交互脚本 -->
        <script type="text/ecmascript">
            // 添加太阳动画
            const sun = document.querySelector('circle');
            let angle = 0;
            
            function animateSun() {
                angle += 0.005;
                const yOffset = Math.sin(angle) * 10;
                sun.setAttribute('cy', 100 + yOffset);
                requestAnimationFrame(animateSun);
            }
            
            animateSun();
            
            // 添加滚动事件监听
            document.addEventListener('scroll', function() {
                const scrollPercent = window.scrollY / (document.body.scrollHeight - window.innerHeight);
                const tail = document.getElementById("tail");
                
                // 根据滚动位置改变猫咪尾巴形状
                if(scrollPercent > 0.7) {
                    tail.setAttribute("d", "M-5,-20 Q-10,-45 -30,-35");
                } else if(scrollPercent > 0.4) {
                    tail.setAttribute("d", "M-5,-20 Q-20,-30 -35,-15");
                } else {
                    tail.setAttribute("d", "M-5,-20 Q-30,-40 -40,-20");
                }
            });
        </script>
    </svg>
    """,
    "fantasy": """
    <svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
        <rect width="800" height="600" fill="#2a1a4a"/>
        <circle cx="400" cy="150" r="80" fill="#f5b8ff" opacity="0.7"/>
        <circle cx="200" cy="250" r="40" fill="#b0f0ff" opacity="0.5"/>
        <circle cx="600" cy="350" r="60" fill="#ffd0a8" opacity="0.6"/>
        <path d="M100,500 C200,450 300,550 400,500 C500,450 600,550 700,500" stroke="#c299ff" stroke-width="3" fill="none"/>
        <text x="400" y="100" font-family="Arial" font-size="24" text-anchor="middle" fill="#f0c7ff">奇幻阅读</text>
        
        <!-- 星星 -->
        <g id="stars">
            <circle cx="150" cy="120" r="2" fill="#ffffff"/>
            <circle cx="250" cy="80" r="1" fill="#ffffff"/>
            <circle cx="350" cy="200" r="1.5" fill="#ffffff"/>
            <circle cx="450" cy="150" r="1" fill="#ffffff"/>
            <circle cx="550" cy="100" r="2" fill="#ffffff"/>
        </g>
        
        <!-- 魔法猫咪 -->
        <g id="magic_cat" transform="translate(400, 300) scale(0.9)">
            <circle cx="0" cy="0" r="25" fill="#9f7bea"/>
            <circle cx="-8" cy="-10" r="5" fill="#FFFFFF"/>
            <circle cx="8" cy="-10" r="5" fill="#FFFFFF"/>
            <circle cx="-8" cy="-10" r="2" fill="#4e2a84"/>
            <circle cx="8" cy="-10" r="2" fill="#4e2a84"/>
            <path d="M-10,5 Q0,12 10,5" stroke="#4e2a84" stroke-width="1.5" fill="none"/>
            <path id="tail" d="M-5,-20 Q-30,-40 -40,-20" stroke="#9f7bea" stroke-width="10" fill="none"/>
            <path d="M-18,-28 L-25,-35 M18,-28 L25,-35" stroke="#9f7bea" stroke-width="4" fill="none"/>
            <path id="magic_aura" d="M-40,-40 A60,60 0 1,0 40,40" stroke="#f5b8ff" stroke-width="2" fill="none" opacity="0.6"/>
        </g>
        
        <!-- 交互脚本 -->
        <script type="text/ecmascript">
            // 星星闪烁动画
            const stars = document.querySelectorAll('#stars circle');
            
            stars.forEach((star, index) => {
                const randomDelay = Math.random() * 5;
                const randomDuration = 1 + Math.random() * 3;
                
                const animation = star.animate([
                    { opacity: 0.2 },
                    { opacity: 1 },
                    { opacity: 0.2 }
                ], {
                    duration: randomDuration * 1000,
                    delay: randomDelay * 1000,
                    iterations: Infinity
                });
            });
            
            // 魔法光环旋转
            const aura = document.getElementById('magic_aura');
            let angle = 0;
            
            function rotateMagicAura() {
                angle += 1;
                aura.setAttribute('transform', `rotate(${angle}, 0, 0)`);
                requestAnimationFrame(rotateMagicAura);
            }
            
            rotateMagicAura();
            
            // 添加滚动事件监听
            document.addEventListener('scroll', function() {
                const scrollPercent = window.scrollY / (document.body.scrollHeight - window.innerHeight);
                const tail = document.getElementById("tail");
                
                // 根据滚动位置改变猫咪尾巴形状
                if(scrollPercent > 0.7) {
                    tail.setAttribute("d", "M-5,-20 Q-10,-45 -30,-35");
                } else if(scrollPercent > 0.4) {
                    tail.setAttribute("d", "M-5,-20 Q-20,-30 -35,-15");
                } else {
                    tail.setAttribute("d", "M-5,-20 Q-30,-40 -40,-20");
                }
            });
        </script>
    </svg>
    """,
    "modern": """
    <svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
        <rect width="800" height="600" fill="#ffffff"/>
        <rect x="50" y="50" width="700" height="500" fill="#f7f7f7" stroke="#e0e0e0" stroke-width="1"/>
        <line x1="50" y1="150" x2="750" y2="150" stroke="#e0e0e0" stroke-width="1"/>
        <rect x="100" y="200" width="250" height="300" fill="#f0f0f0"/>
        <rect x="450" y="200" width="250" height="150" fill="#f0f0f0"/>
        <rect x="450" y="380" width="250" height="120" fill="#f0f0f0"/>
        <text x="400" y="100" font-family="Arial" font-size="24" text-anchor="middle" fill="#333333">现代阅读</text>
        
        <!-- 科技感猫咪 -->
        <g id="tech_cat" transform="translate(650, 280) scale(0.6)">
            <rect x="-30" y="-30" width="60" height="60" rx="15" fill="#e0e0e0"/>
            <circle cx="0" cy="0" r="25" fill="#a0a0a0"/>
            <circle cx="-8" cy="-10" r="5" fill="#FFFFFF"/>
            <circle cx="8" cy="-10" r="5" fill="#FFFFFF"/>
            <circle cx="-8" cy="-10" r="2" fill="#333333"/>
            <circle cx="8" cy="-10" r="2" fill="#333333"/>
            <path d="M-10,5 Q0,12 10,5" stroke="#333333" stroke-width="1.5" fill="none"/>
            <path id="tech_tail" d="M-5,-20 Q-30,-40 -40,-20" stroke="#a0a0a0" stroke-width="10" fill="none"/>
            <line x1="-20" y1="-25" x2="-10" y2="-35" stroke="#a0a0a0" stroke-width="3"/>
            <line x1="20" y1="-25" x2="10" y2="-35" stroke="#a0a0a0" stroke-width="3"/>
            <rect id="progress" x="-28" y="25" width="0" height="5" fill="#4e8df5"/>
        </g>
        
        <!-- 交互脚本 -->
        <script type="text/ecmascript">
            // 添加滚动事件监听
            document.addEventListener('scroll', function() {
                const scrollPercent = window.scrollY / (document.body.scrollHeight - window.innerHeight);
                const tail = document.getElementById("tech_tail");
                const progress = document.getElementById("progress");
                
                // 更新进度条
                progress.setAttribute('width', Math.min(56, scrollPercent * 56));
                
                // 根据滚动位置改变猫咪尾巴形状
                if(scrollPercent > 0.7) {
                    tail.setAttribute("d", "M-5,-20 Q-10,-45 -30,-35");
                } else if(scrollPercent > 0.4) {
                    tail.setAttribute("d", "M-5,-20 Q-20,-30 -35,-15");
                } else {
                    tail.setAttribute("d", "M-5,-20 Q-30,-40 -40,-20");
                }
            });
            
            // 添加视觉效果
            const techRects = document.querySelectorAll('rect[id!="progress"]');
            
            techRects.forEach((rect, index) => {
                const randomDelay = Math.random() * 2;
                const randomDuration = 0.5 + Math.random() * 1;
                
                const animation = rect.animate([
                    { opacity: 0.9 },
                    { opacity: 1 },
                    { opacity: 0.9 }
                ], {
                    duration: randomDuration * 1000,
                    delay: randomDelay * 1000,
                    iterations: Infinity
                });
            });
        </script>
    </svg>
    """
}

# 动画效果定义
ANIMATION_EFFECTS = {
    "cozy": {
        "light_flicker": {
            "element": "circle",
            "attributes": {
                "opacity": [0.8, 1],
                "duration": "3s",
                "repeatCount": "indefinite"
            }
        },
        "cat_tail_swing": {
            "element": "#tail",
            "attributes": {
                "path": [
                    "M-5,-20 Q-30,-40 -40,-20",
                    "M-5,-20 Q-20,-30 -35,-15",
                    "M-5,-20 Q-10,-45 -30,-35"
                ],
                "duration": "5s",
                "repeatCount": "indefinite"
            }
        }
    },
    "outdoor": {
        "sun_pulse": {
            "element": "circle:first-of-type",
            "attributes": {
                "r": [55, 65],
                "duration": "5s",
                "repeatCount": "indefinite"
            }
        },
        "cat_tail_swing": {
            "element": "#tail",
            "attributes": {
                "path": [
                    "M-5,-20 Q-30,-40 -40,-20",
                    "M-5,-20 Q-20,-30 -35,-15",
                    "M-5,-20 Q-10,-45 -30,-35"
                ],
                "duration": "5s",
                "repeatCount": "indefinite"
            }
        }
    },
    "fantasy": {
        "magic_glow": {
            "elements": ["circle"],
            "attributes": {
                "opacity": [0.4, 0.8],
                "duration": "3s",
                "repeatCount": "indefinite"
            }
        },
        "star_twinkle": {
            "elements": ["#stars circle"],
            "attributes": {
                "opacity": [0.2, 1, 0.2],
                "duration": "random(1-4)s",
                "delay": "random(0-5)s",
                "repeatCount": "indefinite"
            }
        },
        "magic_aura_rotate": {
            "element": "#magic_aura",
            "attributes": {
                "transform": "rotate(angle, 0, 0)",
                "angle_increment": 1,
                "duration": "continuous"
            }
        }
    },
    "modern": {
        "subtle_shift": {
            "elements": ["rect"],
            "attributes": {
                "opacity": [0.9, 1, 0.9],
                "duration": "random(0.5-1.5)s",
                "delay": "random(0-2)s",
                "repeatCount": "indefinite"
            }
        },
        "progress_update": {
            "element": "#progress",
            "attributes": {
                "width": "scroll_percent * 56",
                "max_width": 56,
                "update_on": "scroll"
            }
        }
    }
}

def extract_keywords(content: str) -> List[str]:
    """
    从内容中提取关键词以增强场景渲染效果
    """
    # 这里可以使用更复杂的NLP处理来提取关键词
    # 简化版本：提取一些常见的描述性词汇
    keywords = []
    common_descriptors = [
        "明亮", "温暖", "黑暗", "寒冷", "温馨", "神秘",
        "欢快", "忧伤", "繁忙", "安静", "古老", "现代",
        "自然", "科技", "魔法", "现实"
    ]
    
    for word in common_descriptors:
        if word in content:
            keywords.append(word)
    
    return keywords

def enhance_svg_with_content(svg: str, content: str) -> str:
    """
    根据内容增强SVG
    """
    keywords = extract_keywords(content)
    
    # 基于关键词调整SVG
    for keyword in keywords:
        if keyword in ["明亮", "温暖"]:
            # 使背景色更暖
            svg = svg.replace('fill="#f5f0e6"', 'fill="#f7e8d0"')
        elif keyword in ["黑暗", "寒冷"]:
            # 使背景色更冷
            svg = svg.replace('fill="#f5f0e6"', 'fill="#e0e8f0"')
        elif keyword in ["神秘", "魔法"]:
            # 添加星星或闪光元素
            if "<circle cx=" in svg and "id=\"stars\"" not in svg:
                star_elements = '''
                <g id="stars">
                    <circle cx="150" cy="120" r="2" fill="#ffffff"/>
                    <circle cx="250" cy="80" r="1" fill="#ffffff"/>
                    <circle cx="350" cy="200" r="1.5" fill="#ffffff"/>
                    <circle cx="450" cy="150" r="1" fill="#ffffff"/>
                    <circle cx="550" cy="100" r="2" fill="#ffffff"/>
                </g>
                '''
                svg = svg.replace('</svg>', f'{star_elements}</svg>')
    
    return svg

def generate_animation_data(theme: str) -> Dict[str, Any]:
    """
    生成动画数据
    """
    if theme in ANIMATION_EFFECTS:
        return ANIMATION_EFFECTS[theme]
    return {}

def render_scene(request: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    根据内容和主题渲染阅读场景
    
    Args:
        request: 包含内容和主题的请求
        context: 插件上下文
    
    Returns:
        包含SVG内容和动画数据的响应
    """
    content = request.get("content", "")
    theme = request.get("theme", "cozy")
    
    # 确保主题有效
    if theme not in SCENE_TEMPLATES:
        theme = "cozy"  # 默认主题
    
    # 获取基础SVG模板
    svg_content = SCENE_TEMPLATES[theme]
    
    # 根据内容增强SVG
    enhanced_svg = enhance_svg_with_content(svg_content, content)
    
    # 生成动画数据
    animation_data = generate_animation_data(theme)
    
    return {
        "svg_content": enhanced_svg,
        "animation_data": animation_data
    } 