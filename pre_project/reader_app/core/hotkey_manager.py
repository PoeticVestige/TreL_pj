"""
快捷键管理模块
"""


class HotkeyManager:
    """快捷键管理器"""

    def __init__(self):
        self.handlers = {}

    def register(self, hotkey: str, callback):
        """注册快捷键"""
        pass

    def unregister(self, hotkey: str):
        """注销快捷键"""
        pass

    def start_listening(self):
        """开始监听"""
        pass

    def stop_listening(self):
        """停止监听"""
        pass
