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

import os
import json

import appier

import base

LABELS = []

PROTECTED = []

REPOS = []

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

def res_data(name, dir_path = None):
    if dir_path == None:
        base_path = os.path.dirname(os.path.abspath(__file__))
        dir_path = os.path.join(base_path, "res")
    file_path = os.path.join(dir_path, name)
    file = open(file_path, "rb")
    try: data = file.read()
    finally: file.close()
    if appier.legacy.is_bytes(data): data = data.decode("utf-8")
    data_j = json.loads(data)
    return data_j

if __name__ == "__main__":
    owner = appier.conf("OWNER", None)
    repos = appier.conf("REPOS", [], cast = list)
    config_load = appier.conf("CONFIG_LOAD", False, cast = bool)
    config_path = appier.conf("CONFIG_PATH", None)
    config_load = config_load or bool(config_path)
    labels = LABELS
    protected = PROTECTED
    if config_load:
        config = res_data("config.json", dir_path = config_path)
        base_labels = res_data("labels/base.json", dir_path = config_path)
        extra_labels = res_data("labels/extra.json", dir_path = config_path)
        repos = config.get("repos", repos)
        protected = config.get("protected", protected)
        labels.extend(base_labels)
        labels.extend(extra_labels)
    for repo in repos: ensure_labels(owner, repo)
else:
    __path__ = []
