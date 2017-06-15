#  Copyright 2017 Christoph Mende
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import imp
import os

plugin_folder = 'plugins'
main_module = '__init__'

def get_plugins():
    plugins = []
    plugin_candidates = os.listdir(plugin_folder)
    for i in plugin_candidates:
        location = os.path.join(plugin_folder, i)
        if not os.path.isdir(location) or main_module+'.py' not in os.listdir(location):
            continue
        info = imp.find_module(main_module, [location])
        plugins.append({'name': i, 'info': info})
    return plugins

def load_plugin(plugin):
    return imp.load_module(main_module, *plugin['info'])
