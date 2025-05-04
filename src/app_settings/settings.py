from enum import Enum, auto
from pathlib import Path
from typing import ClassVar

from pydantic import Field
from pydantic_settings import BaseSettings

from . import config


def get_default_language() -> str:
    if config._default_language is None:
        raise RuntimeError(
            "app_settings.configure() must be called before using this package"
        )

    return config._default_language


class SettingType(Enum):
    OPTIONS = auto()


class AppSettings(BaseSettings):
    CONFIG_FILE: ClassVar[str] = ".env"

    CONFIG_FILE_PATH: ClassVar[Path]

    language: str = Field(
        default_factory=get_default_language,
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
        with open(self.CONFIG_FILE_PATH, "w") as f:
            for key, value in self.model_dump().items():
                f.write(f"{key.upper()}={value}\n")
