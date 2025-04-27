from typing import Dict, Any, List, Optional

# 预定义的交互反应
INTERACTION_RESPONSES = {
    "click": {
        "default": {
            "response_action": "highlight",
            "update_data": {
                "highlight_color": "#ffcc00",
                "duration": "0.5s"
            }
        },
        "text_element": {
            "response_action": "zoom",
            "update_data": {
                "scale": 1.1,
                "duration": "0.3s"
            }
        },
        "background": {
            "response_action": "theme_change",
            "update_data": {
                "transition": "fade",
                "duration": "1s"
            }
        },
        "cat": {
            "response_action": "meow",
            "update_data": {
                "sound": "soft_meow",
                "animation": "gentle_bounce",
                "duration": "0.5s"
            }
        }
    },
    "hover": {
        "default": {
            "response_action": "tooltip",
            "update_data": {
                "show": True,
                "position": "above"
            }
        },
        "interactive_element": {
            "response_action": "glow",
            "update_data": {
                "color": "#8aedff",
                "intensity": 0.6
            }
        },
        "cat": {
            "response_action": "wiggle_tail",
            "update_data": {
                "amplitude": 10,
                "frequency": 2,
                "duration": "1s"
            }
        }
    },
    "drag": {
        "default": {
            "response_action": "move",
            "update_data": {
                "constrain_to_parent": True
            }
        },
        "resizable_element": {
            "response_action": "resize",
            "update_data": {
                "preserve_aspect_ratio": True,
                "min_size": {"width": 50, "height": 50}
            }
        },
        "cat": {
            "response_action": "follow",
            "update_data": {
                "speed": 0.5,
                "min_distance": 20,
                "animation": "smooth"
            }
        }
    }
}

def get_element_type(element_id: str) -> str:
    """
    根据元素ID确定元素类型
    """
    if element_id.startswith("text"):
        return "text_element"
    elif element_id.startswith("bg") or element_id == "background":
        return "background"
    elif element_id in ["cat", "magic_cat", "tech_cat"] or element_id.startswith("cat_"):
        return "cat"
    elif element_id.startswith("int_"):
        return "interactive_element"
    elif element_id.startswith("resize_"):
        return "resizable_element"
    return "default"

def get_theme_from_interaction(x_position: float, screen_width: float = 800) -> str:
    """
    根据用户点击位置推荐主题
    """
    relative_position = x_position / screen_width
    
    if relative_position < 0.25:
        return "cozy"
    elif relative_position < 0.5:
        return "outdoor"
    elif relative_position < 0.75:
        return "fantasy"
    else:
        return "modern"

def handle_interaction(request: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    处理用户与阅读场景的交互
    
    Args:
        request: 包含交互信息的请求
        context: 插件上下文
    
    Returns:
        包含响应动作和更新数据的响应
    """
    interaction_type = request.get("interaction_type", "click")
    element_id = request.get("element_id", "")
    position = request.get("position", {"x": 0, "y": 0})
    
    # 确保交互类型有效
    if interaction_type not in INTERACTION_RESPONSES:
        interaction_type = "click"  # 默认交互类型
    
    # 获取元素类型
    element_type = get_element_type(element_id)
    
    # 获取交互响应
    response_config = INTERACTION_RESPONSES[interaction_type].get(
        element_type, 
        INTERACTION_RESPONSES[interaction_type]["default"]
    )
    
    # 创建响应
    response = {
        "response_action": response_config["response_action"],
        "update_data": {
            **response_config["update_data"],
            "element_id": element_id,
            "position": position
        }
    }
    
    # 特殊交互处理逻辑
    if interaction_type == "click" and element_type == "background":
        # 背景点击可能触发场景主题变化
        suggested_theme = get_theme_from_interaction(position["x"])
        response["update_data"]["theme_suggestion"] = suggested_theme
    
    # 猫咪特殊交互
    if element_type == "cat":
        if interaction_type == "click":
            # 点击猫咪时增加一些随机反应
            import random
            cat_reactions = ["purr", "mew", "stretch", "blink", "tilt_head"]
            response["update_data"]["reaction"] = random.choice(cat_reactions)
            
        elif interaction_type == "drag":
            # 拖动猫咪时记录初始和目标位置
            response["update_data"]["start_position"] = position
            response["update_data"]["target_position"] = {
                "x": position["x"] + 50,  # 示例目标位置
                "y": position["y"] + 30
            }
    
    return response 