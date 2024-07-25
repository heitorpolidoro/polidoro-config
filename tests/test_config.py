import os
from copy import deepcopy
from unittest.mock import patch

import pytest

from pconfig.config import ConfigBase
from tests.conftest import change_dir
