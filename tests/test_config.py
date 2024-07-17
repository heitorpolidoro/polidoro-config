import os
import sys
from copy import deepcopy
from unittest.mock import patch

import pytest

from pconfig import Config, ConfigError
from tests.conftest import change_dir


@pytest.fixture(autouse=True)
def clean_env():
    original_environ = deepcopy(os.environ)
    yield
    os.environ.clear()
    os.environ.update(original_environ)




def test_get_from_environ(monkeypatch):
    monkeypatch.setenv("MY_ENV", "my_value")
    assert Config.MY_ENV == "my_value"


def test_config_not_found():
    with pytest.raises(ConfigError) as config_error:
        assert Config.NOT_FOUND

    assert (
        str(config_error.value)
        == "No such environment variable with the name 'NOT_FOUND'."
    )


def test_load_dotenv(tmp_path):
    dotenv_file = tmp_path / ".env"
    dotenv_file.write_text("LOAD_ENV_VAR=load_value")

    with (
        change_dir(tmp_path),
        patch("dotenv.main.find_dotenv", return_value=dotenv_file),
    ):
        assert "LOAD_ENV_VAR" not in os.environ
        assert Config.load_dotenv() is True
        assert "LOAD_ENV_VAR" in os.environ

    assert Config.LOAD_ENV_VAR == "load_value"


def test_load_dotenv_when_dotenv_is_not_installed(tmp_path):
    dotenv_file = tmp_path / ".env"
    dotenv_file.write_text("LOAD_ENV_VAR=load_value")

    with (
        change_dir(tmp_path),
        patch("dotenv.main.find_dotenv", return_value=dotenv_file),
        patch.dict(sys.modules, {"dotenv": None}),
    ):
        assert "LOAD_ENV_VAR" not in os.environ
        assert Config.load_dotenv() is False
        assert "LOAD_ENV_VAR" not in os.environ

    with pytest.raises(ConfigError) as config_error:
        assert Config.LOAD_ENV_VAR

    assert (
        str(config_error.value)
        == "No such environment variable with the name 'LOAD_ENV_VAR'."
    )


def test_load_dotenv_when_there_is_no_dotenv_file():
    assert "LOAD_ENV_VAR" not in os.environ
    assert Config.load_dotenv() is False
    assert "LOAD_ENV_VAR" not in os.environ

    with pytest.raises(ConfigError) as config_error:
        assert Config.LOAD_ENV_VAR

    assert (
        str(config_error.value)
        == "No such environment variable with the name 'LOAD_ENV_VAR'."
    )
