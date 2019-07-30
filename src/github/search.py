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

__author__ = "Hugo Gomes <hugo@hugogomes.eu>"
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

class SearchAPI(object):

    def repositories_search(self, query, text_match = False, *args, **kwargs):
        url = self.base_url + "search/repositories"
        kwargs.update(q = query)
        headers = {} if not text_match else {"Accept": "application/vnd.github.v3.text-match+json"}
        contents = self.get_many(url, headers = headers, **kwargs)
        return contents

    def commits_search(self, query, text_match = False, *args, **kwargs):
        url = self.base_url + "search/commits"
        kwargs.update(q = query)
        headers = {} if not text_match else {"Accept": "application/vnd.github.v3.text-match+json"}
        contents = self.get_many(url, headers = headers, **kwargs)
        return contents

    def code_search(self, query, text_match = False, *args, **kwargs):
        url = self.base_url + "search/code"
        kwargs.update(q = query)
        headers = {} if not text_match else {"Accept": "application/vnd.github.v3.full.text-match+json"}
        contents = self.get_many(url, headers = headers, **kwargs)
        return contents

    def issues_search(self, query, text_match = False, *args, **kwargs):
        url = self.base_url + "search/issues"
        kwargs.update(q = query)
        headers = {} if not text_match else {"Accept": "application/vnd.github.v3.text-match+json"}
        contents = self.get_many(url, headers = headers, **kwargs)
        return contents

    def users_search(self, query, text_match = False, *args, **kwargs):
        url = self.base_url + "search/issues"
        kwargs.update(q = query)
        headers = {} if not text_match else {"Accept": "application/vnd.github.v3.text-match+json"}
        contents = self.get_many(url, headers = headers, **kwargs)
        return contents

    def topics_search(self, query, text_match = False, *args, **kwargs):
        url = self.base_url + "search/topics"
        kwargs.update(q = query)
        headers = {} if not text_match else {"Accept": "application/vnd.github.v3.text-match+json"}
        contents = self.get_many(url, headers = headers, **kwargs)
        return contents

    def labels_search(self, repository_id, query, text_match = False, *args, **kwargs):
        url = self.base_url + "search/labels"
        kwargs.update(dict(repository_id = repository_id, q = query))
        headers = {} if not text_match else {"Accept": "application/vnd.github.v3.text-match+json"}
        contents = self.get_many(url, headers = headers, **kwargs)
        return contents
