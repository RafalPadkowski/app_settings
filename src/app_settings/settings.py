from enum import Enum, auto
from pathlib import Path
from typing import ClassVar

from platformdirs import user_config_path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from . import config


def get_app_name() -> str:
    if config._app_name is None:
        raise RuntimeError(
            "app_settings.configure() must be called before using this package"
        )

    return config._app_name


def get_default_language() -> str:
    if config._default_language is None:
        raise RuntimeError(
            "app_settings.configure() must be called before using this package"
        )

    return config._default_language


class SettingType(Enum):
    OPTIONS = auto()


class Settings(BaseSettings):
    CONFIG_FILE: ClassVar[str] = ".env"

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

    # This will be overwritten by config.configure()
    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict()

    @classmethod
    def get_config_path(cls) -> Path:
        return user_config_path(get_app_name())

    @classmethod
    def get_config_file_path(cls) -> Path:
        config_path: Path = cls.get_config_path()
        config_path.mkdir(parents=True, exist_ok=True)
        return config_path / cls.CONFIG_FILE

    def save(self) -> None:
        config_file_path: Path = self.get_config_file_path()

        with open(config_file_path, "w") as f:
            for key, value in self.model_dump().items():
                f.write(f"{key.upper()}={value}\n")
