from typing import TextIO
from unittest.mock import patch, Mock

import pytest

from pconfig import ConfigError
from pconfig.config import ConfigBase

# noinspection PyUnresolvedReferences
from tests.conftest import change_dir, import_error


# noinspection PyUnusedLocal
def test_when_is_match_is_not_implemented():
    from pconfig.loaders.file_loader import ConfigFileLoader

    # noinspection PyAbstractClass
    class FileLoaderTest(ConfigFileLoader):
        pass

    with pytest.raises(NotImplementedError) as err:

        class ConfigTest(ConfigBase):
            _config_file_path = "file"

    assert str(err.value) == "FileLoaderTest must implement this method."


# noinspection PyUnusedLocal
def test_when_get_content_is_not_implemented(tmp_path):
    from pconfig.loaders.file_loader import ConfigFileLoader

    file = tmp_path / "file"
    file.write_text("")

    # noinspection PyAbstractClass
    class FileLoaderTest(ConfigFileLoader):
        @classmethod
        def is_match(cls, file_path: str) -> bool:
            return True

    with pytest.raises(NotImplementedError) as err, change_dir(tmp_path):

        class ConfigTest(ConfigBase):
            _config_file_path = file

    assert str(err.value) == "FileLoaderTest must implement this method."


# noinspection PyUnusedLocal
def test_when_get_data_is_not_implemented(tmp_path):
    from pconfig.loaders.file_loader import ConfigFileLoader

    file = tmp_path / "file"
    file.write_text("")

    # noinspection PyAbstractClass
    class FileLoaderTest(ConfigFileLoader):
        @classmethod
        def is_match(cls, file_path: str) -> bool:
            return True

        @classmethod
        def get_content(cls, file_path: str) -> str:
            return "content"

    with pytest.raises(NotImplementedError) as err, change_dir(tmp_path):

        class ConfigTest(ConfigBase):
            _config_file_path = file

    assert str(err.value) == "FileLoaderTest must implement this method."


def test_load_yaml(tmp_path):
    yaml_file = tmp_path / ".yaml"
    yaml_file.write_text("LOAD_ENV_VAR: 'load_value'")

    with change_dir(tmp_path):

        class ConfigTest(ConfigBase):
            _config_file_path = yaml_file
            LOAD_ENV_VAR = None

        assert ConfigTest.LOAD_ENV_VAR == "load_value"


def test_load_yaml_when_yaml_is_not_installed(tmp_path):
    # noinspection PyGlobalUndefined
    dotenv_file = tmp_path / ".env"
    dotenv_file.write_text("LOAD_ENV_VAR=load_value")

    yaml_file = tmp_path / ".yaml"
    yaml_file.write_text("LOAD_ENV_VAR: 'load_value'")

    with (
        change_dir(tmp_path),
        import_error("yaml"),
        pytest.raises(ConfigError) as c_err,
    ):
        # noinspection PyUnusedLocal
        class ConfigTest(ConfigBase):
            _config_file_path = yaml_file
            LOAD_ENV_VAR = None

    assert (
        str(c_err.value)
        == "Must install pyyaml to use this feature. `pip install pyyaml`"
    )
