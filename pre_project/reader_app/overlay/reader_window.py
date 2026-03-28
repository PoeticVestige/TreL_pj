"""
阅读器覆盖层窗口
"""


class ReaderWindow:
    """阅读器窗口（硬件覆盖层）"""

    def __init__(self):
        self.hwnd = None
        self.opacity = 0.8
        self.width = 800
        self.height = 600
        self.content = ""
        self.current_page = 0

    def create(self):
        """创建窗口"""
        pass

    def show(self):
        """显示窗口"""
        pass

    def hide(self):
        """隐藏窗口"""
        pass

    def set_content(self, text: str):
        """设置显示内容"""
        pass

    def set_opacity(self, opacity: float):
        """设置透明度"""
        pass

    def move(self, dx: int, dy: int):
        """移动窗口位置"""
        pass

    def resize(self, width: int, height: int):
        """调整窗口大小"""
        pass

    def next_page(self):
        """下一页"""
        pass

    def prev_page(self):
        """上一页"""
        pass
