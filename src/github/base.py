#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive GitHub API
# Copyright (C) 2008-2014 Hive Solutions Lda.
#
# This file is part of Hive GitHub API.
#
# Hive GitHub API is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive GitHub API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive GitHub API. If not, see <http://www.gnu.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2014 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import appier

from github import org
from github import repo
from github import user

API_DOMAIN = "api.github.com"

class Api(
    appier.Api,
    org.OrgApi,
    repo.RepoApi,
    user.UserApi
):

    def __init__(self, *args, **kwargs):
        appier.Api.__init__(self, *args, **kwargs)
        self.username = kwargs.get("username", None)
        self.password = kwargs.get("password", None)
        self._build_url()

    def get(self, url, **kwargs):
        return self.request(
            appier.get,
            url,
            params = kwargs
        )

    def post(self, url, data = None, data_j = None, **kwargs):
        return self.request(
            appier.post,
            url,
            params = kwargs,
            data = data,
            data_j = data_j
        )

    def put(self, url, data = None, data_j = None, **kwargs):
        return self.request(
            appier.put,
            url,
            params = kwargs,
            data = data,
            data_j = data_j
        )

    def delete(self, url, **kwargs):
        return self.request(
            appier.delete,
            url,
            params = kwargs
        )

    def request(self, method, *args, **kwargs):
        try:
            result = method(*args, **kwargs)
        except appier.exceptions.HTTPError as exception:
            self.handle_error(exception)

        return result

    def handle_error(self, error):
        raise

    def _build_url(self):
        if not self.username:
            raise appier.OperationalError(message = "No username provided")
        if not self.password:
            raise appier.OperationalError(message = "No password provided")
        self.base_url = "https://%s:%s@%s/" % (
            self.username,
            self.password,
            API_DOMAIN
        )
