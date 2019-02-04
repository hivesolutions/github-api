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

import base64

import appier

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

    def create_contents_repo(
        self,
        owner,
        repo,
        path,
        content,
        message = None,
        sha = None,
        branch = None,
        committer = None,
        author = None
    ):
        message = message or "%s '%s' file" % ("Updated" if sha else "Created", path)
        content = appier.legacy.bytes(content)
        content_b64 = base64.b64encode(content)
        content_b64 = appier.legacy.str(content_b64)
        data_j = dict(message = message, content = content_b64)
        if sha: data_j["sha"] = sha
        if branch: data_j["branch"] = branch
        if committer: data_j["committer"] = committer
        if author: data_j["author"] = author
        url = self.base_url + "repos/%s/%s/contents/%s" % (owner, repo, path)
        contents = self.put(url, data_j = data_j)
        return contents

    def issue_repo(self, owner, repo, number):
        url = self.base_url + "repos/%s/%s/issues/%s" % (owner, repo, number)
        contents = self.get_cached(url)
        return contents

    def events_issue_repo(self, owner, repo, number):
        url = self.base_url + "repos/%s/%s/issues/%s/events" % (owner, repo, number)
        contents = self.get_cached(url)
        return contents

    def event_issue_repo(self, owner, repo, number):
        url = self.base_url + "repos/%s/%s/issues/events/%s" % (owner, repo, number)
        contents = self.get_cached(url)
        return contents

    def create_issue_repo(self, owner, repo, issue):
        url = self.base_url + "repos/%s/%s/issues" % (owner, repo)
        contents = self.post(url, data_j = issue)
        return contents

    def update_issue_repo(self, owner, repo, number, issue):
        url = self.base_url + "repos/%s/%s/issues/%s" % (owner, repo, number)
        contents = self.patch(url, data_j = issue)
        return contents
