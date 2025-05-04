from pydantic_settings import SettingsConfigDict

from .settings import Settings

_app_name: str | None = None
_default_language: str | None = None


def configure(app_name: str, default_language: str) -> None:
    global _app_name, _default_language

    _app_name = app_name
    _default_language = default_language

    # Dynamically set model_config for Settings to use the right .env file
    Settings.model_config = SettingsConfigDict(
        env_file=str(Settings.get_config_file_path())
    )
