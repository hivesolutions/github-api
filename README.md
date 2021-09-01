# [GitHub API](http://github-api.hive.pt)

Standard GitHub API implementation in python.

## Configuration

| Name                    | Type  | Default | Description                                                        |
| ----------------------- | ----- | ------- | ------------------------------------------------------------------ |
| **GITHUB_USERNAME**     | `str` | `None`  | The username to be used in the authentication with the GitHub API. |
| **GITHUB_PASSWORD**     | `str` | `None`  | The password to be used in the authentication with the GitHub API. |
| **GITHUB_ID**           | `str` | `None`  | While using OAuth provides a way to define the client identifier.  |
| **GITHUB_SECRET**       | `str` | `None`  | While using OAuth provides a way to define the client secret.      |
| **GITHUB_REDIRECT_URL** | `str` | `None`  | To be used in the OAuth process as the target redirect URL.        |
| **GITHUB_TOKEN**        | `str` | `None`  | If defined allows a statically generated OAuth Token to be used.   |

## License

GitHub API is currently licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/).

## Build Automation

[![Build Status](https://app.travis-ci.com/hivesolutions/github_api.svg?branch=master)](https://travis-ci.com/github/hivesolutions/github_api)
[![Coverage Status](https://coveralls.io/repos/hivesolutions/github_api/badge.svg?branch=master)](https://coveralls.io/r/hivesolutions/github_api?branch=master)
[![PyPi Status](https://img.shields.io/pypi/v/github_api_python.svg)](https://pypi.python.org/pypi/github_api_python)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/)
