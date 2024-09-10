from pconfig.config import BaseModel, ConfigBase
from tests.conftest import change_dir


def test_load_yaml_complex_config_with_pydantic(tmp_path):
    yaml_tmp_file = tmp_path / ".yaml"
    yaml_tmp_file.write_text(
        """config:
        var1: "1"
        another_config:
            another_var2: "2" """
    )

    with change_dir(tmp_path):

        class AnotherConfig(BaseModel):
            another_var1: str = "default1"
            another_var2: str = "default2"

        class MyConfig(BaseModel):
            var1: str = "default1"
            var2: str = "default2"
            another_config: AnotherConfig = AnotherConfig()

        class ConfigTest(ConfigBase):
            yaml_file = yaml_tmp_file.name
            config = MyConfig()

        assert ConfigTest.config.var1 == "1"
        assert ConfigTest.config.var2 == "default2"
        assert ConfigTest.config.another_config.another_var1 == "default1"
        assert ConfigTest.config.another_config.another_var2 == "2"
