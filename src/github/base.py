#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive GitHub API
# Copyright (c) 2008-2019 Hive Solutions Lda.
#
# This file is part of Hive GitHub API.
#
# Hive GitHub API is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive GitHub API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive GitHub API. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2019 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import time

import appier

from . import orgs
from . import repo
from . import search
from . import user

API_DOMAIN = "api.github.com"
""" The base domain from which the connection with the service
will be performed, this value will be used for the construction
of the base url that is going to be used by the api """

SCOPE = (
    "user:email",
)
""" The list of permissions to be used to create the
scope string for the oauth value """

class API(
    appier.OAuth2API,
    orgs.OrgAPI,
    repo.RepoAPI,
    search.SearchAPI,
    user.UserAPI
):

    def __init__(self, *args, **kwargs):
        appier.OAuth2API.__init__(self, *args, **kwargs)
        self.username = appier.conf("GITHUB_USERNAME", None)
        self.password = appier.conf("GITHUB_PASSWORD", None)
        self.client_id = appier.conf("GITHUB_ID", None)
        self.client_secret = appier.conf("GITHUB_SECRET", None)
        self.redirect_url = appier.conf("GITHUB_REDIRECT_URL", None)
        self.username = kwargs.get("username", self.username)
        self.password = kwargs.get("password", self.password)
        self.client_id = kwargs.get("client_id", self.client_id)
        self.client_secret = kwargs.get("client_secret", self.client_secret)
        self.login_url = kwargs.get("login_url", "https://github.com/login/")
        self.redirect_url = kwargs.get("redirect_url", self.redirect_url)
        self.access_token = kwargs.get("access_token", None)
        self.scope = kwargs.get("scope", SCOPE)
        self.mode = kwargs.get("mode", None) or self._get_mode()
        self._build_url()

    def get_many(self, url, **kwargs):
        page = 1
        result = []
        while True:
            items = self.get(url, page = page, **kwargs)
            if isinstance(items, dict): items = items["items"]
            if not items: break
            result.extend(items)
            page += 1
        return result

    def get_cached(self, url, retries = 5, sleep = 1.0, **kwargs):
        while True:
            retries -= 1
            contents, file = self.get(url, handle = True, **kwargs)
            code = file.getcode()
            if not code == 202: break
            if not retries > 0: break
            time.sleep(sleep)
        return contents

    def oauth_authorize(self, state = None):
        url = self.login_url + "oauth/authorize"
        values = dict(
            client_id = self.client_id,
            redirect_uri = self.redirect_url,
            response_type = "code",
            scope = " ".join(self.scope)
        )
        if state: values["state"] = state
        data = appier.legacy.urlencode(values)
        url = url + "?" + data
        return url

    def oauth_access(self, code):
        url = self.login_url + "oauth/access_token"
        contents = self.post(
            url,
            auth = False,
            token = False,
            client_id = self.client_id,
            client_secret = self.client_secret,
            grant_type = "authorization_code",
            redirect_uri = self.redirect_url,
            code = code
        )
        contents = contents.decode("utf-8")
        contents = appier.legacy.parse_qs(contents)
        self.access_token = contents["access_token"][0]
        self.trigger("access_token", self.access_token)
        return self.access_token

    def _build_url(self):
        if self.is_oauth(): self.base_url = "https://%s/" % API_DOMAIN; return
        if not self.username:
            raise appier.OperationalError(message = "No username provided")
        if not self.password:
            raise appier.OperationalError(message = "No password provided")
        self.base_url = "https://%s:%s@%s/" % (
            self.username,
            self.password,
            API_DOMAIN
        )

    def _get_mode(self):
        if self.username and self.password: return appier.OAuthAPI.DIRECT_MODE
        elif self.client_id and self.client_secret: return appier.OAuthAPI.OAUTH_MODE
        return appier.OAuthAPI.UNSET_MODE
