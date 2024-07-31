from pconfig.config import ConfigBase


def test_get_from_environ(monkeypatch):
    monkeypatch.setenv("MY_ENV", "my_value")

    class ConfigTest(ConfigBase):
        MY_ENV = None
        MY_DEFAULT_VALUE = "default_value"

    assert ConfigTest.MY_ENV == "my_value"
    assert ConfigTest.MY_DEFAULT_VALUE == "default_value"
