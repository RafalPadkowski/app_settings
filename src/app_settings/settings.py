from enum import Enum, auto

from pydantic import Field
from pydantic_settings import BaseSettings

from . import config


class SettingType(Enum):
    OPTIONS = auto()


class AppSettings(BaseSettings):
    language: str = Field(
        default=config.defaults["language"],
        title="Language",
        description="Language of the application",
        json_schema_extra={
            "type": SettingType.OPTIONS.value,
            "choices": [
                {"text": "English", "data": "en"},
                {"text": "Polish", "data": "pl"},
            ],
        },
    )

    def save(self) -> None:
        with open(config.get_config_file_path(), "w") as f:
            for key, value in self.model_dump().items():
                f.write(f"{key.upper()}={value}\n")
