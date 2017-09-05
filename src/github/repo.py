#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive GitHub API
# Copyright (c) 2008-2017 Hive Solutions Lda.
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

__copyright__ = "Copyright (c) 2008-2017 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

class RepoAPI(object):

    def get_repo(self, owner, repo, type = "owner"):
        url = self.base_url + "repos/%s/%s" % (owner, repo)
        contents = self.get(url, type = type)
        return contents

    def issues_repo(self, owner, repo, state = "all"):
        url = self.base_url + "repos/%s/%s/issues" % (owner, repo)
        contents = self.get_many(url, state = state)
        return contents

    def stats_contrib_repo(self, owner, repo):
        url = self.base_url + "repos/%s/%s/stats/contributors" % (owner, repo)
        contents = self.get_cached(url)
        return contents

    def stats_activity_repo(self, owner, repo):
        url = self.base_url + "repos/%s/%s/stats/commit_activity" % (owner, repo)
        contents = self.get_cached(url)
        return contents

    def stats_participation_repo(self, owner, repo):
        url = self.base_url + "repos/%s/%s/stats/participation" % (owner, repo)
        contents = self.get_cached(url)
        return contents

    def contents_repo(self, owner, repo, path, ref = None):
        url = self.base_url + "repos/%s/%s/contents/%s" % (owner, repo, path)
        contents = self.get_cached(url, ref = ref)
        return contents

    def issue_repo(self, owner, repo, number):
        url = self.base_url + "repos/%s/%s/issues/%s" % (owner, repo, number)
        contents = self.get_cached(url)
        return contents

    def create_issue(self, owner, repo, issue):
        url = self.base_url + "repos/%s/%s/issues" % (owner, repo)
        contents = self.post(url, data_j = issue)
        return contents

    def update_issue(self, owner, repo, number, issue):
        url = self.base_url + "repos/%s/%s/issues/%s" % (owner, repo, number)
        contents = self.patch(url, data_j = issue)
        return contents
