from activator.base_activator import BaseActivator
import os, platform


class JetBrains(BaseActivator):

    def __init__(self):
        user_home_dir = os.path.expanduser('~')
        self.search_path = ''
        if platform.system() == 'Darwin':
            self.search_path = os.path.join(user_home_dir, 'Library', 'Application Support', 'JetBrains', '**',
                                            'github-copilot-intellij')
        else:
            if platform.system() == 'Windows':
                self.search_path = os.path.join(user_home_dir, 'AppData', 'Roaming', 'JetBrains', '**',
                                                'github-copilot-intellij')
            else:
                if platform.system() == 'Linux':
                    self.search_path = os.path.join(user_home_dir, '.local', 'share', 'JetBrains', '**',
                                                    'github-copilot-intellij')
        self.path_suffix = os.path.join('copilot-agent', 'bin')
