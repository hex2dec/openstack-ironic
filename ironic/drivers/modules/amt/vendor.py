#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
"""
AMT Vendor Methods
"""

from ironic.common import boot_devices
from ironic.conductor import task_manager
from ironic.drivers import base
from ironic.drivers.modules import pxe


class AMTPXEVendorPassthru(pxe.VendorPassthru):

    @base.passthru(['POST'], method='pass_deploy_info')
    @task_manager.require_exclusive_lock
    def _continue_deploy(self, task, **kwargs):
        task.driver.management.ensure_next_boot_device(task.node,
                                                       boot_devices.PXE)
        super(AMTPXEVendorPassthru, self)._continue_deploy(task, **kwargs)
