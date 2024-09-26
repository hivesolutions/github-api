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


class CommitAPI(object):

    def create_commit(
        self,
        owner,
        repo,
        parent_sha,
        tree_sha,
        message,
    ):
        url = self.base_url + "repos/%s/%s/git/commits" % (owner, repo)
        contents = self.post(
            url,
            data_j=dict(
                parents=[parent_sha],
                tree=tree_sha,
                message=message,
            ),
        )
        return contents

    def get_commit(self, owner, repo, commit_sha):
        url = self.base_url + "repos/%s/%s/git/commits/%s" % (owner, repo, commit_sha)
        contents = self.get(url)
        return contents

    def latest_commit(self, owner, repo, branch="master"):
        url = self.base_url + "repos/%s/%s/git/ref/heads/%s" % (owner, repo, branch)
        contents = self.get(url)
        return contents

    def set_branch_commit(self, owner, repo, commit_sha, branch="master", force=True):
        url = self.base_url + "repos/%s/%s/git/refs/heads/%s" % (owner, repo, branch)
        contents = self.patch(url, data_j=dict(sha=commit_sha, force=force))
        return contents

    def latest_commit_sha(self, owner, repo, branch="master"):
        latest_commit = self.latest_commit(owner, repo, branch=branch)
        return latest_commit["object"]["sha"]

    def tree_sha(self, owner, repo, commit_sha):
        commit = self.get_commit(owner, repo, commit_sha)
        return commit["tree"]["sha"]

    def create_custom_commit(self, owner, repo, message, files, branch="master"):
        parent_sha = self.latest_commit_sha(owner, repo, branch=branch)
        base_tree_sha = self.tree_sha(owner, repo, parent_sha)

        files_tree = []
        for file in files:
            blob = self.create_blob(owner, repo, file["content"])
            files_tree.append(
                {
                    "path": file["path"],
                    "sha": blob["sha"],
                    "mode": "100644",
                    "type": "blob",
                }
            )

        tree = self.create_tree(owner, repo, base_tree_sha, files=files_tree)
        commit = self.create_commit(owner, repo, parent_sha, tree["sha"], message)
        self.set_branch_commit(owner, repo, commit["sha"], branch=branch)

        return commit
