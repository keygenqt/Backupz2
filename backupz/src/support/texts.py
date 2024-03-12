"""
Copyright 2021-2024 Vitaliy Zarubin

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from enum import Enum


# Application texts
class AppTexts(Enum):
    @staticmethod
    def error_dependency_git():
        return '<red>Application</red> "git" <red>not found, install it.</red>'

    @staticmethod
    def error_dependency_pigz():
        return '<red>Application</red> "pigz" <red>not found, install it.</red>'

    @staticmethod
    def confirm_init():
        return 'Add default backupz configuration file?'

    @staticmethod
    def success_init(path: str):
        return '<green>Configuration file added successfully:</green> {}'.format(path)

    @staticmethod
    def error_load_key(key: str):
        return '<red>Error reading configuration file. Check the</red> "{}" <red>parameter.</red>'.format(key)