from enum import Enum, auto
from pathlib import Path
from typing import ClassVar

from platformdirs import user_config_path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from .constants import APP_NAME
from .i18n import DEFAULT_LANGUAGE


class SettingType(Enum):
    OPTIONS = auto()


class Settings(BaseSettings):
    CONFIG_PATH: ClassVar[Path] = user_config_path(APP_NAME)
    CONFIG_FILE: ClassVar[str] = ".env"

    language: str = Field(
        default=DEFAULT_LANGUAGE,
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

    model_config = SettingsConfigDict(env_file=str(CONFIG_PATH / CONFIG_FILE))

    @classmethod
    def get_config_file_path(cls) -> Path:
        cls.CONFIG_PATH.mkdir(parents=True, exist_ok=True)
        return cls.CONFIG_PATH / cls.CONFIG_FILE

    def save(self) -> None:
        config_file_path: Path = self.get_config_file_path()

        with open(config_file_path, "w") as f:
            for key, value in self.model_dump().items():
                f.write(f"{key.upper()}={value}\n")
