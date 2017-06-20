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

def help(user, args):
    if args is None:
        return "wat?! go help yourself"

    return args

def version(user, args):
    try:
        with open('.git/refs/heads/master', 'r') as f:
            rev = f.read()[:8]
        with open('.git/COMMIT_EDITMSG', 'r') as f:
            msg = f.read()
        return '{}: {}'.format(rev, msg)
    except:
        return 'unknown'

commands = {
    'help': help,
    'version': version
}
