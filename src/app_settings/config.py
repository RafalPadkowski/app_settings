from pathlib import Path
from typing import Any

from platformdirs import user_config_path
from pydantic_settings import SettingsConfigDict

defaults: dict[str, Any] = {
    "language": "en",
}

config_file_path: Path | None = None


def configure(app_name: str) -> None:
    config_path: Path = user_config_path(app_name)
    config_path.mkdir(parents=True, exist_ok=True)

    global config_file_path
    config_file_path = config_path / ".env"

    from .settings import AppSettings

    AppSettings.model_config = SettingsConfigDict(env_file=str(config_file_path))


def get_config_file_path() -> Path:
    if config_file_path is None:
        raise RuntimeError(
            "app_settings.configure() must be called before using this package"
        )

    return config_file_path
