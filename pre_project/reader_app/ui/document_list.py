"""
文档列表组件
"""


class DocumentList:
    """文档列表"""

    def __init__(self):
        self.documents = []

    def refresh(self):
        """刷新列表"""
        pass

    def add_item(self, doc_info: dict):
        """添加项目"""
        pass

    def remove_item(self, doc_id: str):
        """移除项目"""
        pass
