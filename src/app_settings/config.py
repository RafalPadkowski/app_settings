_app_name: str | None = None
_default_language: str | None = None


def configure(app_name: str, default_language: str) -> None:
    global _app_name
    global _default_language

    _app_name = app_name
    _default_language = default_language
