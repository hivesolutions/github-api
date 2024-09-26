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

__copyright__ = "Copyright (c) 2008-2024 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

from . import base
from . import blob
from . import commit
from . import orgs
from . import repo
from . import search
from . import tree
from . import user

from .base import API_DOMAIN, SCOPE, API
from .blob import BLOBAPI
from .commit import CommitAPI
from .orgs import OrgAPI
from .repo import RepoAPI
from .search import SearchAPI
from .tree import TreeAPI
from .user import UserAPI
