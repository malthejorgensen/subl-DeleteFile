import os

import sublime
import sublime_plugin


class DeleteFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        full_path = self.view.file_name()

        os.unlink(full_path)

        self.view.close()
