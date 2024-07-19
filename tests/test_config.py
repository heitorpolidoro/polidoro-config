import os
import sys
from copy import deepcopy
from unittest.mock import patch

import pytest

from pconfig.config import ConfigBase
from tests.conftest import change_dir


@pytest.fixture(autouse=True)
def clean_env():
    original_environ = deepcopy(os.environ)
    yield
    os.environ.clear()
    os.environ.update(original_environ)


def test_get_default(monkeypatch):
    class ConfigTest(ConfigBase):
        MY_ENV = "default_value"

    assert ConfigTest.MY_ENV == "default_value"


def test_get_from_environ(monkeypatch):
    monkeypatch.setenv("MY_ENV", "my_value")

    class ConfigTest(ConfigBase):
        MY_ENV = None

    assert ConfigTest.MY_ENV == "my_value"


def test_load_dotenv(tmp_path):
    dotenv_file = tmp_path / ".env"
    dotenv_file.write_text("LOAD_ENV_VAR=load_value")

    with (
        change_dir(tmp_path),
        patch("dotenv.main.find_dotenv", return_value=dotenv_file),
    ):

        class ConfigTest(ConfigBase):
            LOAD_ENV_VAR = None

        assert ConfigTest.LOAD_ENV_VAR == "load_value"


def test_load_dotenv_when_dotenv_is_not_installed(tmp_path):
    dotenv_file = tmp_path / ".env"
    dotenv_file.write_text("LOAD_ENV_VAR=load_value")

    with (
        change_dir(tmp_path),
        patch("dotenv.main.find_dotenv", return_value=dotenv_file),
        patch("pconfig.config.dotenv", None),
    ):

        class ConfigTest(ConfigBase):
            LOAD_ENV_VAR = None

        assert ConfigTest.LOAD_ENV_VAR is None


def test_load_dotenv_when_there_is_no_dotenv_file():
    with (patch("dotenv.main.find_dotenv", return_value=None),):

        class ConfigTest(ConfigBase):
            LOAD_ENV_VAR = None

        assert ConfigTest.LOAD_ENV_VAR is None
