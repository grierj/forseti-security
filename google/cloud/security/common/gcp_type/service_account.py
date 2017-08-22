# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A Service Account

See: https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts
"""


class ServiceAccount(object):
    """Represents Service Account resource."""

    def __init__(self, **kwargs):
        """Service Account resource.

        Args:
            **kwargs (dict): The keyworded variable args.
        """
        self.project_id = kwargs.get('project_id')
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.oauth2_client_id = kwargs.get('oauth2_client_id')
        self.keys = kwargs.get('keys')
        self.raw_service_account = kwargs.get('raw_service_account')