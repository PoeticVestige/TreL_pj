"""
配置管理模块
"""
import json
from pathlib import Path

# 默认配置
DEFAULT_CONFIG = {
    "app": {
        "version": "1.0.0",
        "data_dir": "./storage/data"
    },
    "reader": {
        "opacity": 0.8,
        "width": 800,
        "height": 600,
        "font_family": "Microsoft YaHei",
        "font_size": 14,
        "text_color": "#FFFFFF",
        "bg_color": "#000000",
        "always_on_top": True
    },
    "hotkeys": {
        "move_up": "ctrl+up",
        "move_down": "ctrl+down",
        "move_left": "ctrl+left",
        "move_right": "ctrl+right",
        "opacity_up": "ctrl+shift+1",
        "opacity_down": "ctrl+shift+2",
        "width_increase": "ctrl+shift+3",
        "width_decrease": "ctrl+shift+4",
        "height_increase": "ctrl+shift+5",
        "height_decrease": "ctrl+shift+6",
        "page_up": "pageup",
        "page_down": "pagedown",
        "page_up_alt": "ctrl+shift+up",
        "page_down_alt": "ctrl+shift+down",
        "exit": "ctrl+q",
        "toggle_visibility": "ctrl+b"
    }
}


class ConfigManager:
    """配置管理器"""

    def __init__(self):
        self.config_dir = Path(__file__).parent
        self.config_file = self.config_dir / "app_config.json"
        self._config = None

    def load(self):
        """加载配置"""
        pass

    def save(self):
        """保存配置"""
        pass

    def get(self, key, default=None):
        """获取配置项"""
        pass
