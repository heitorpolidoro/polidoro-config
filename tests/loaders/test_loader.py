from unittest.mock import Mock, call, patch

import pytest

from pconfig.config import ConfigBase

loader_calls = []


# noinspection PyUnusedLocal
def test_loader():
    from pconfig.loaders.loader import ConfigLoader

    class LoaderTest0(ConfigLoader):

        @classmethod
        def load_config(cls, _config_class) -> dict[str, object]:
            loader_calls.append("LoaderTest0")
            return {"name": "value0"}

    class LoaderTest1(ConfigLoader):
        order = 100

        @classmethod
        def load_config(cls, _config_class) -> dict[str, object]:
            loader_calls.append("LoaderTest1")
            return {"name": "value1"}

    class Config(ConfigBase):
        name = None

    assert loader_calls == ["LoaderTest0", "LoaderTest1"]
    assert Config.name == "value1"


# noinspection PyAbstractClass,PyUnusedLocal
def test_raise_not_implemented_error():
    from pconfig.loaders.loader import ConfigLoader

    class LoaderTest(ConfigLoader):
        pass

    with pytest.raises(NotImplementedError) as err:

        class ConfigTest(ConfigBase):
            pass

    assert str(err.value) == "LoaderTest must implement this method."
