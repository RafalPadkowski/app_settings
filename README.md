# app-settings

A simple configuration management package using `pydantic-settings` and `platformdirs`.

This package allows you to define application settings in a `.env` file stored in the user's configuration directory.

## Features

- Automatically determines the appropriate configuration file location using `platformdirs`
- Uses `pydantic-settings` for settings validation and management
- Supports configuration before use via the `configure()` function
- Provides a `.save()` method to persist settings

## Installation

```bash
pip install git+https://github.com/RafalPadkowski/app_settings.git
```

## Usage

### 1. Configure the app

You must configure the package with app name.

```python
import app_settings

app_settings.configure("my_app")
```

### 2. Use the AppSettings class

```python
from app_settings import AppSettings

settings = AppSettings()
```

### 3. Save settings

```python
settings.language = "pl"
settings.save()  # Saves to ~/.config/my_app/.env (Linux)
```

## Configuration Path

The configuration file is stored in the user config directory provided by `platformdirs`, e.g.:

- **Linux**: `~/.config/<app_name>/.env`
- **macOS**: `~/Library/Application Support/<app_name>/.env`
- **Windows**: `C:\Users\<User>\AppData\Local\<app_name>\.env`

## Fields

Currently, the settings class includes:

- `language`: Application language (default "en", supports "en" and "pl")

## Errors

If `configure()` is not called before saving `AppSettings`, a `RuntimeError` will be raised.

## License

MIT
