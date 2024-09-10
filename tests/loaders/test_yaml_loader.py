import pytest

from pconfig.config import BaseModel, ConfigBase, ConfigValue
from pconfig.error import ConfigError
from tests.conftest import change_dir, import_error


def test_load_yaml(tmp_path):
    yaml_tmp_file = tmp_path / ".yaml"
    yaml_tmp_file.write_text("LOAD_ENV_VAR: 'load_value'")

    with change_dir(tmp_path):

        class ConfigTest(ConfigBase):
            yaml_file = yaml_tmp_file.name
            LOAD_ENV_VAR = None

        assert ConfigTest.LOAD_ENV_VAR == "load_value"


def test_load_yaml_when_yaml_is_not_installed(tmp_path, monkeypatch):
    monkeypatch.setenv("LOAD_ENV_VAR", "load_value")

    yaml_tmp_file = tmp_path / ".yaml"
    yaml_tmp_file.write_text("LOAD_ENV_VAR: 'load_value'")

    with (
        change_dir(tmp_path),
        import_error("yaml"),
        pytest.raises(ConfigError) as c_err,
    ):
        # noinspection PyUnusedLocal
        class ConfigTest(ConfigBase):
            yaml_file = yaml_tmp_file.name
            LOAD_ENV_VAR = None

    assert (
        str(c_err.value)
        == "Must install pyyaml to use this feature. `pip install pyyaml`"
    )


def test_load_yaml_when_yaml_is_not_installed_and_not_used(monkeypatch):
    monkeypatch.setenv("LOAD_ENV_VAR", "load_value")

    with (import_error("yaml"),):

        class ConfigTest(ConfigBase):
            LOAD_ENV_VAR = None

    assert ConfigTest.LOAD_ENV_VAR == "load_value"


def test_load_with_falsy_yaml_file():
    class ConfigTest(ConfigBase):
        yaml_file = None
        LOAD_ENV_VAR = None

    assert ConfigTest.LOAD_ENV_VAR is None


def test_load_without_yaml_file():
    class ConfigTest(ConfigBase):
        LOAD_ENV_VAR = None

    assert ConfigTest.LOAD_ENV_VAR is None


def test_load_with_not_eligible_yaml_file(tmp_path):
    yaml_tmp_file = tmp_path / ".not_yaml"
    yaml_tmp_file.write_text("LOAD_ENV_VAR: 'load_value'")

    with change_dir(tmp_path):

        class ConfigTest(ConfigBase):
            yaml_file = yaml_tmp_file.name
            LOAD_ENV_VAR = None

        assert ConfigTest.LOAD_ENV_VAR is None


def test_load_yaml_config(tmp_path):
    yaml_tmp_file = tmp_path / ".yaml"
    yaml_tmp_file.write_text(
        """config: 
        var1: 1"""
    )

    with change_dir(tmp_path):

        class ConfigTest(ConfigBase):
            yaml_file = yaml_tmp_file.name
            config = ConfigValue(var1=None, var2="default")

        assert ConfigTest.config.var1 == 1
        assert ConfigTest.config.var2 == "default"


def test_load_yaml_complex_config(tmp_path):
    yaml_tmp_file = tmp_path / ".yaml"
    yaml_tmp_file.write_text(
        """config: 
        var1: 
            var2: 2"""
    )

    with change_dir(tmp_path):

        class ConfigTest(ConfigBase):
            yaml_file = yaml_tmp_file.name
            config = ConfigValue(var1=ConfigValue(var2="default"))

        assert ConfigTest.config.var1.var2 == 2


def test_load_yaml_wrong_complex_config(tmp_path):
    yaml_tmp_file = tmp_path / ".yaml"
    yaml_tmp_file.write_text(
        """config: 
        var1: 1"""
    )

    with change_dir(tmp_path):

        class ConfigTest(ConfigBase):
            yaml_file = yaml_tmp_file.name
            config = ConfigValue(var1=ConfigValue(var2="default"))

        assert ConfigTest.config.var1 == 1
