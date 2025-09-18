import qrenderdoc as qrd
import renderdoc as rd
import os
from typing import Optional

import sys
# sys.path.append(r"C:/Users/lichanglong02/AppData/Roaming/qrenderdoc/extensions/LcL-RenderdocTextureExporter-main/lib")


class TestClass():
    def __init__(self, ctx: qrd.CaptureContext):
        super().__init__()
        self.ctx = ctx
        ctx.Replay().BlockInvoke(self._init_data)

    def _init_data(self):
        # print("This is a test method.")
        self.ctx.Extensions().MessageDialog(f"BlockInvoke 测试2")


    def test_example(self):
        print("This is a test method.")
        # self.ctx.Extensions().MessageDialog(f"测试3")
        
        plugin_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.ctx.Extensions().MessageDialog(f"{plugin_dir}", "plugin_dir")

        # try:
        #     # from PyQt5.QtWidgets import QApplication, QMessageBox
        #     app = QApplication.instance() or QApplication([])
        #     QMessageBox.information(None, "Qt5 测试", "PyQt5 已成功导入并可用！")
        # except Exception as e:
        #     ctx.Extensions().MessageDialog(f"PyQt5 测试失败: {e}", "Qt5 测试")