"""
文档解析器模块
"""
from pathlib import Path


class DocumentParser:
    """文档解析器"""

    @staticmethod
    def parse_txt(file_path: Path) -> str:
        """解析 TXT 文件"""
        pass

    @staticmethod
    def parse_md(file_path: Path) -> str:
        """解析 Markdown 文件"""
        pass

    @staticmethod
    def parse_pdf(file_path: Path) -> str:
        """解析 PDF 文件"""
        pass

    @staticmethod
    def parse_docx(file_path: Path) -> str:
        """解析 Word 文档"""
        pass
