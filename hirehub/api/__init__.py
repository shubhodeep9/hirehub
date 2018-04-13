#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

class GitAPI:
    """Class to operate on api.github.com and provide details"""

    def __init__(self):
        """Constructs a GitAPI instance"""

        self.endpoint = "https://api.github.com"
        self.type = "application/javascript"

    def search_users(self, location = 'India', language = 'any', sort_by = 'followers', order = 'desc'):
        """Searches users using github api and gives list of users.
        :arg location: Desired location for target developers.
        :arg language: Specific programming language filter.
        :arg sort_by: Sort by followers or repositories.
        :arg order: Order by Ascending (asc) or Descending (desc)
        """

        users_endpoint = self.endpoint + "/search/users"

        q = '+location:' + location
        if(language != 'any'):
            q = q + '+language:' + language

        payload = {
                'q'     : q,
                'sort'  : sort_by
                'order' : order
            }

        requests.get(users_endpoint,
                params=payload)

