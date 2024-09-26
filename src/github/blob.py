#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive GitHub API
# Copyright (c) 2008-2024 Hive Solutions Lda.
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

__author__ = "João Magalhães <joamag@hive.pt> & Hugo Gomes <hugo@hugogomes.eu>"
""" The author(s) of the module """

__copyright__ = "Copyright (c) 2008-2024 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import base64

import appier


class BLOBAPI(object):

    def blobs_data(self, owner, repo, file_sha):
        url = self.base_url + "repos/%s/%s/git/blobs/%s" % (owner, repo, file_sha)
        contents = self.get_cached(url)
        return contents

    def create_blob(self, owner, repo, content):
        url = self.base_url + "repos/%s/%s/git/blobs" % (owner, repo)
        content = appier.legacy.bytes(content)
        content_b64 = base64.b64encode(content)
        content_b64 = appier.legacy.str(content_b64)
        contents = self.post(url, data_j=dict(content=content_b64, encoding="base64"))
        return contents
