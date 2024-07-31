import pytest

from pconfig.config import ConfigBase
from pconfig.error import ConfigError

# noinspection PyUnresolvedReferences
from tests.conftest import change_dir, import_error


def test_load_yaml(tmp_path):
    yaml_file = tmp_path / ".yaml"
    yaml_file.write_text("LOAD_ENV_VAR: 'load_value'")

    with change_dir(tmp_path):

        class ConfigTest(ConfigBase):
            file_path = yaml_file.name
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
            file_path = yaml_file.name
            LOAD_ENV_VAR = None

    assert (
        str(c_err.value)
        == "Must install pyyaml to use this feature. `pip install pyyaml`"
    )


def test_load_with_falsy_file_path():
    class ConfigTest(ConfigBase):
        file_path = None
        LOAD_ENV_VAR = None

    assert ConfigTest.LOAD_ENV_VAR is None


def test_load_with_not_eligible_file_path(tmp_path):
    yaml_file = tmp_path / ".not_yaml"
    yaml_file.write_text("LOAD_ENV_VAR: 'load_value'")

    with change_dir(tmp_path):

        class ConfigTest(ConfigBase):
            file_path = yaml_file.name
            LOAD_ENV_VAR = None

        assert ConfigTest.LOAD_ENV_VAR is None
