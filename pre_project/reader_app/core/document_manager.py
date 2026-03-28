"""
文档管理模块
"""
from pathlib import Path


class DocumentManager:
    """文档管理器"""

    def __init__(self, data_dir: Path):
        self.data_dir = data_dir

    def upload(self, file_path: Path):
        """上传文档"""
        pass

    def delete(self, doc_id: str):
        """删除文档"""
        pass

    def rename(self, doc_id: str, new_name: str):
        """重命名文档"""
        pass

    def list_documents(self):
        """获取文档列表"""
        pass
