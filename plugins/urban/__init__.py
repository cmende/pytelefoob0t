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

import requests

API = 'https://api.urbandictionary.com/v0/'

def urban(user, args):
    if args is None:
        url = API + 'random'
        params = {}
    else:
        url = API + 'define'
        params = { 'term': args }

    r = requests.get(url, params)

    first = r.json()['list'][0]
    word = first['word']
    definition = first['definition']
    example = first['example']

    return """\
*{}*

{}

_{}_
""".format(word, definition, example)

commands = {
    'urban': urban
}
