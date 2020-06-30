#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive GitHub API
# Copyright (c) 2008-2020 Hive Solutions Lda.
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

__copyright__ = "Copyright (c) 2008-2020 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import appier

from . import base

LABELS = [
    dict(
        name = "bug",
        description = "Something isn't working",
        color = "d73a4a"
    ),
    dict(
        name = "cant-repro",
        description = "Issue is not reproducible",
        color = "ffa500"
    ),
    dict(
        name = "client",
        description = "Issue was created or influenced by client",
        color = "73bace"
    ),
    dict(
        name = "design",
        description = "Requires design to be done",
        color = "c7a4f2"
    ),
    dict(
        name = "documentation",
        description = "Issue requires new documentation",
        color = "6da0ff"
    ),
    dict(
        name = "enhancement",
        description = "New feature or request",
        color = "a2eeef"
    ),
    dict(
        name = "fast-track",
        description = "Feature to be fixed or implemented ASAP",
        color = "c61193"
    ),
    dict(
        name = "p-high",
        description = "High priority issue",
        color = "d73a4a"
    ),
    dict(
        name = "p-low",
        description = "Low priority issue",
        color = "42e5a9"
    ),
    dict(
        name = "p-medium",
        description = "Medium priority issue",
        color = "dd9d11"
    ),
    dict(
        name = "poc",
        description = "Issue is a Proof of Concept",
        color = "bfd4f2"
    ),
    dict(
        name = "project",
        description = "Issue represents a project",
        color = "50e582"
    ),
    dict(
        name = "regression",
        description = "Issue is related to a regression in behaviour",
        color = "5619ff"
    ),
    dict(
        name = appier.legacy.u("reward 🏆️"),
        description = "There's a reward for whoever solves this issue",
        color = "f9e1ac"
    ),
    dict(
        name = "risky",
        description = "Seems to be risky",
        color = "d73a4a"
    ),
    dict(
        name = "talk",
        description = "Requires verbal communication",
        color = "fc88b6"
    ),
    dict(
        name = "triage",
        description = "Issue currently under triage",
        color = "e8cb5a"
    ),
    dict(
        name = "user-story",
        description = "Issue represents a user story",
        color = "f9f261"
    ),
    dict(
        name = "wontfix",
        description = "This will not be worked on",
        color = "ffffff"
    ),
    dict(
        name = "unit-testing",
        description = "Issue requires creation of unit tests",
        color = "ff8242"
    ),
    dict(
        name = "expired",
        description = "Issue has expired",
        color = "808080"
    ),
    dict(
        name = appier.legacy.u("reaper ☠️️"),
        description = "Dropped issues due to aging or/and business value",
        color = "000000"
    )
]

PROTECTED = [
    "dior",
    "sergio-rossi",
    appier.legacy.u("hermès")
]

def ensure_labels(owner, repo, labels = LABELS, protected = PROTECTED, cleanup = True):
    # prints a small information about the repository that
    # is going to have its labels updated
    print("Fixing %s/%s..." % (owner, repo))

    # gathers the reference to the API object to be used in
    # the remote calls that are gong to change the labels
    api = base.get_api()

    # gathers the complete set of labels currently present in
    # the repository, to compare them against the requested ones
    _labels = api.labels_repo(owner, repo)

    # adds the name prefix (name without emoji) to the label, effectively
    # empowering it for a better comparison operation
    for label in labels: label["prefix"] = label["name"].split(appier.legacy.u(" "), 1)[0]
    for label in _labels: label["prefix"] = label["name"].split(appier.legacy.u(" "), 1)[0]

    # builds both maps of labels indexing all of the labels by their
    # prefix name (name without emoji)
    _labels_m = dict((label["prefix"], label) for label in _labels)
    labels_m = dict((label["prefix"], label) for label in labels)

    for prefix, label in appier.legacy.iteritems(labels_m):
        if prefix in _labels_m:
            _label = _labels_m[prefix]
            name = appier.legacy.bytes(_label["name"], encoding= "utf-8", force = True)
            is_equal = label["name"] == _label["name"] and\
                label["description"] == _label["description"] and\
                label["color"] == _label["color"]
            if not is_equal:
                print("Updating label %s..." % name)
                api.update_label_repo(owner, repo, name, label)
        else:
            name = appier.legacy.bytes(label["name"], encoding= "utf-8", force = True)
            print("Creating label %s..." % name)
            api.create_label_repo(owner, repo, label)

    if not cleanup: return

    for prefix, label in appier.legacy.iteritems(_labels_m):
        if prefix in labels_m: continue
        if prefix in protected: continue
        name = appier.legacy.bytes(label["name"], encoding= "utf-8", force = True)
        print("Deleting label %s..." % name)
        api.delete_label_repo(owner, repo, name)

if __name__ == "__main__":
    owner = appier.conf("OWNER", None)
    repos = appier.conf("REPOS", [], cast = list)
    for repo in repos: ensure_labels(owner, repo)
else:
    __path__ = []
