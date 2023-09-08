from activator.base_activator import BaseActivator
import os, shutil
from frozen_dir import app_path

APP_PATH = app_path()


class VSCode(BaseActivator):

    def __init__(self):
        user_home_dir = os.path.expanduser('~')
        self.search_path = os.path.join(user_home_dir, '.vscode', 'extensions', 'github.copilot-*')
        self.path_suffix = os.path.join('dist')

    def modify_extension(self, paths, key):
        if not paths:
            paths = super().get_path()
        for path in paths:
            file_path = os.path.join(path, 'extension.js')
            extension_js_path = ''
            if 'copilot-labs' in file_path:
                extension_js_path = os.path.join(APP_PATH, 'js', 'extension-labs.js')
            else:
                if 'copilot-chat' in file_path:
                    extension_js_path = os.path.join(APP_PATH, 'js', 'extension-chat.js')
                else:
                    extension_js_path = os.path.join(APP_PATH, 'js', 'extension-copilot.js')
            if os.path.isfile(file_path):
                self._copy_and_add_key(extension_js_path, file_path, key)
                self._addActivator_js(os.path.dirname(file_path))

    def _addActivator_js(self, file_path):
        activator_js_path = os.path.join(APP_PATH, 'js', 'activator.js')
        activator_js_dest_path = os.path.join(file_path, 'activator.js')
        if os.path.exists(activator_js_dest_path):
            os.remove(activator_js_dest_path)
        shutil.copy(activator_js_path, activator_js_dest_path)

    def _copy_and_add_key(self, file_path_src, file_path_dest, key):
        with open(file_path_src, 'r', encoding='utf-8') as (file):
            file_content = file.read()
        file_content = 'const aukey="%s";' % key + file_content
        with open(file_path_dest, 'w', encoding='utf-8') as (file):
            file.write(file_content)
