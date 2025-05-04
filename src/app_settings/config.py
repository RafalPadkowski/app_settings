from pathlib import Path

from platformdirs import user_config_path
from pydantic_settings import SettingsConfigDict

from .settings import AppSettings

_app_name: str | None = None
_default_language: str | None = None


def configure(app_name: str, default_language: str) -> None:
    global _app_name, _default_language

    _app_name = app_name
    _default_language = default_language

    config_path: Path = user_config_path(app_name)
    config_path.mkdir(parents=True, exist_ok=True)

    config_file_path: Path = config_path / AppSettings.CONFIG_FILE
    AppSettings.model_config = SettingsConfigDict(env_file=str(config_file_path))
    AppSettings.CONFIG_FILE_PATH = config_file_path
