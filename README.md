# Polidoro Config
Polidoro Config it is a configuration manager for you project

[![Code Quality](https://github.com/heitorpolidoro/polidoro-config/actions/workflows/code_quality.yml/badge.svg)](https://github.com/heitorpolidoro/polidoro-config/actions/workflows/code_quality.yml)
[![Upload Python Package](https://github.com/heitorpolidoro/polidoro-config/actions/workflows/pypi-publish.yml/badge.svg)](https://github.com/heitorpolidoro/polidoro-config/actions/workflows/pypi-publish.yml)
<br>
![GitHub branch check runs](https://img.shields.io/github/check-runs/heitorpolidoro/polidoro-config/master?nameFilter=Code%20Quality%20%2F%20Tests%20(3.9)&logo=python&label=3.9)
![GitHub branch check runs](https://img.shields.io/github/check-runs/heitorpolidoro/polidoro-config/master?nameFilter=Code%20Quality%20%2F%20Tests%20(3.10)&logo=python&label=3.10)
![GitHub branch check runs](https://img.shields.io/github/check-runs/heitorpolidoro/polidoro-config/master?nameFilter=Code%20Quality%20%2F%20Tests%20(3.11)&logo=python&label=3.11)
![GitHub branch check runs](https://img.shields.io/github/check-runs/heitorpolidoro/polidoro-config/master?nameFilter=Code%20Quality%20%2F%20Tests%20(3.12)&logo=python&label=3.12)
<br>
[![Latest Version](https://img.shields.io/github/v/release/heitorpolidoro/polidoro-config?label=Latest%20Version)](https://github.com/heitorpolidoro/polidoro-config/releases/latest)
![GitHub Release Date](https://img.shields.io/github/release-date/heitorpolidoro/polidoro-config)
![GitHub commits since latest release (by SemVer including pre-releases)](https://img.shields.io/github/commits-since/heitorpolidoro/polidoro-config/latest)
![GitHub last commit](https://img.shields.io/github/last-commit/heitorpolidoro/polidoro-config)
<br>
[![GitHub issues](https://img.shields.io/github/issues/heitorpolidoro/polidoro-config)](https://github.com/heitorpolidoro/polidoro-config/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/heitorpolidoro/polidoro-config)](https://github.com/heitorpolidoro/polidoro-config/pulls)

[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=heitorpolidoro_polidoro-config&metric=coverage)](https://sonarcloud.io/summary/new_code?id=heitorpolidoro_polidoro-config)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=heitorpolidoro_polidoro-config&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=heitorpolidoro_polidoro-config)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=heitorpolidoro_polidoro-config&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=heitorpolidoro_polidoro-config)
<br>
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=heitorpolidoro_polidoro-config&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=heitorpolidoro_polidoro-config)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=heitorpolidoro_polidoro-config&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=heitorpolidoro_polidoro-config)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=heitorpolidoro_polidoro-config&metric=bugs)](https://sonarcloud.io/summary/new_code?id=heitorpolidoro_polidoro-config)

## Usage
Create a class inheriting from ConfigBase
```python
from pconfig import ConfigBase

class Config(ConfigBase):
	DB_HOST = 'localhost'
	ENVIRONMENT = 'development'
	...
```

When the class is instantiated will load from environment variables.

```python
# script.py
from pconfig import ConfigBase

class Config(ConfigBase):
	MY_VAR = 'default_value'

print(Config.MY_VAR)
```
```shell
>>> python script.py
default_value

>>> MY_VAR="new_value" python script.py
new_value
```
