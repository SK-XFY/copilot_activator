from activator.base_activator import BaseActivator
import os, platform


class VisualStudio(BaseActivator):

    def __init__(self):
        user_home_dir = os.path.expanduser('~')
        self.search_path = ''
        if platform.system() == 'Windows':
            self.search_path = os.path.join(user_home_dir, 'AppData', 'Local', 'Microsoft', 'VisualStudio', '*',
                                            'Extensions', '**', 'GitHub.Copilot.VisualStudio.dll')
        self.path_suffix = os.path.join('..', 'service', 'dist')
