from pathlib import Path
from typing import Any

from platformdirs import user_config_path
from pydantic_settings import SettingsConfigDict

from .settings import AppSettings

config_file_path: Path
_defaults: dict[str, Any] = {}


def configure(app_name: str, **defaults: Any) -> None:
    config_path: Path = user_config_path(app_name)
    config_path.mkdir(parents=True, exist_ok=True)

    global config_file_path
    config_file_path = config_path / ".env"
    AppSettings.model_config = SettingsConfigDict(env_file=str(config_file_path))

    _defaults.update(defaults)


def get_default_value(key: str) -> Any:
    try:
        return _defaults[key]
    except KeyError:
        raise RuntimeError(
            f"app_settings.configure() must be called "
            f"before using default value for '{key}'"
        )
