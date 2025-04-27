#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from scene_renderer import render_scene
from interaction_handler import handle_interaction

class TestReadingScenePlugin(unittest.TestCase):
    """测试阅读场景插件的基本功能"""
    
    def test_render_scene(self):
        """测试场景渲染功能"""
        # 测试默认温馨主题
        result = render_scene({"content": "这是一个测试"}, None)
        self.assertIn("svg_content", result)
        self.assertIn("animation_data", result)
        self.assertIn("<svg", result["svg_content"])
        self.assertIn("cat", result["svg_content"])
        
        # 测试不同主题
        themes = ["cozy", "outdoor", "fantasy", "modern"]
        for theme in themes:
            result = render_scene({"content": "测试内容", "theme": theme}, None)
            self.assertIn(theme, str(result["animation_data"]))
    
    def test_content_enhancement(self):
        """测试内容增强功能"""
        # 测试关键词增强
        warm_result = render_scene({"content": "温暖的阳光照耀着小猫", "theme": "cozy"}, None)
        cold_result = render_scene({"content": "寒冷的冬天让小猫蜷缩在角落", "theme": "cozy"}, None)
        
        # 验证内容影响了渲染结果
        self.assertNotEqual(warm_result["svg_content"], cold_result["svg_content"])
        
    def test_handle_interaction(self):
        """测试交互处理功能"""
        # 测试点击猫咪
        cat_click = handle_interaction({
            "interaction_type": "click",
            "element_id": "cat",
            "position": {"x": 180, "y": 400}
        }, None)
        
        self.assertEqual(cat_click["response_action"], "meow")
        self.assertIn("reaction", cat_click["update_data"])
        
        # 测试背景点击
        bg_click = handle_interaction({
            "interaction_type": "click",
            "element_id": "background",
            "position": {"x": 700, "y": 300}
        }, None)
        
        self.assertEqual(bg_click["response_action"], "theme_change")
        self.assertIn("theme_suggestion", bg_click["update_data"])
        self.assertEqual(bg_click["update_data"]["theme_suggestion"], "modern")

if __name__ == "__main__":
    unittest.main() 