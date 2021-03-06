# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from .errors import *
from .local import *
from .local import LocalRunner as Runner
from .remote import *

runners = local_runners
runners.update(remote_runners)
