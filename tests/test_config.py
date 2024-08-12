import importlib

from pydantic import BaseModel

from pconfig import ConfigBase, config
from pconfig.config_value import ConfigValue
from tests.conftest import import_error


def test_when_pydantic_is_not_installed():
    # noinspection PyGlobalUndefined

    with (import_error("pydantic"),):
        importlib.reload(config)

        class ConfigTest(ConfigBase):
            LOAD_ENV_VAR = None

        assert ConfigTest.LOAD_ENV_VAR is None
        assert config.BaseModel is None
    importlib.reload(config)


def test_repr():
    class ConfigTest(ConfigBase):
        file_path = "file_name"
        config = ConfigValue(var1=ConfigValue(var2="default"))

    assert (
        str(ConfigTest)
        == "ConfigTest(file_path='file_name', config=ConfigValue(var1=ConfigValue(var2=default)))"
    )


def test_repr_pydantic():
    class AnotherConfig(BaseModel):
        another_var1: str = "default1"
        another_var2: str = "default2"

    class MyConfig(BaseModel):
        var1: str = "default1"
        var2: str = "default2"
        another_config: AnotherConfig = AnotherConfig()

    class ConfigTest(ConfigBase):
        file_path = None
        config = MyConfig()

    assert str(ConfigTest) == (
        "ConfigTest(file_path=None, config=MyConfig(var1='default1', var2='default2', "
        "another_config=AnotherConfig(another_var1='default1', another_var2='default2')))"
    )
