import unittest
import os
import sys
from unittest.mock import patch, MagicMock
import customtkinter as ctk

# Add the src directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import app

class TestPDFMerger(unittest.TestCase):
    
    def setUp(self):
        self.app = app.App()

    def tearDown(self):
        self.app.destroy()

    def test_app_initialization(self):
        self.assertIsNotNone(self.app)
        self.assertEqual(self.app.title(), "PDF Merger")

    def test_change_appearance_mode(self):
        self.app.change_appearance_mode("Light")
        self.assertEqual(ctk.get_appearance_mode(), "Light")

    def test_change_scaling(self):
        self.app.change_scaling("1440p")
        self.assertEqual(self.app.geometry().split("+")[0], "2560x1440")

        self.app.change_scaling("Manual")
        self.assertEqual(self.app.ui_button_minus.cget("state"), "enabled")
        self.assertEqual(self.app.ui_button_plus.cget("state"), "enabled")

    def test_clear_scfr(self):
        self.app.content = ["dummy_path_1", "dummy_path_2"]
        self.app.clear_scfr()
        self.assertEqual(self.app.content, [])
        self.assertEqual(self.app.scrollframe.grid_size(), (1, 0))

    def test_build_scrollframe(self):
        self.app.content = ["dummy_path_1", "dummy_path_2"]
        self.app.build_scrollframe()
        self.assertEqual(len(self.app.scrollframe.winfo_children()), 2)

    @patch('tkinter.filedialog.askopenfilename')
    def test_select_file(self, mock_askopenfilename):
        mock_askopenfilename.return_value = "dummy_path"
        self.app.select_file()
        self.assertIn("dummy_path", self.app.content)

    @patch('tkinter.filedialog.askdirectory')
    def test_select_destination_folder(self, mock_askdirectory):
        mock_askdirectory.return_value = "dummy_folder"
        self.app.select_destination_folder()
        self.assertEqual(self.app.footer_destination.cget("text"), "dummy_folder")

    @patch('pypdf.PdfMerger')
    def test_merge(self, mock_PdfMerger):
        self.app.content = ["dummy_path_1", "dummy_path_2"]
        self.app.footer_destination.configure(text="dummy_folder")
        self.app.footer_name.insert(0, "merged_file.pdf")

        mock_merger_instance = MagicMock()
        mock_PdfMerger.return_value = mock_merger_instance

        self.app.merge()

        mock_merger_instance.append.assert_any_call("dummy_path_1")
        mock_merger_instance.append.assert_any_call("dummy_path_2")
        mock_merger_instance.write.assert_called_with("dummy_folder/merged_file.pdf")
        mock_merger_instance.close.assert_called_once()

    def test_merge_with_errors(self):
        self.app.content = []
        self.app.footer_destination.configure(text="Destination folder")
        self.app.footer_name.delete(0, 'end')

        self.app.merge()

        self.assertEqual(self.app.scrollframe.cget("fg_color"), "red")
        self.assertEqual(self.app.footer_destination.cget("fg_color"), "red")
        self.assertEqual(self.app.footer_name.cget("fg_color"), "red")

if __name__ == '__main__':
    unittest.main()
