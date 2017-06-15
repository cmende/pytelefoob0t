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

import random

def decide(user, args):
    # roll yes/no
    if args is None:
        return random.choice(['yes','no'])

    # roll between args
    return random.choice(args.split())

commands = {
    'decide': decide
}
