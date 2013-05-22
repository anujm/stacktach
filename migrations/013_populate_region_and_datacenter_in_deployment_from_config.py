# Copyright (c) 2013 - Rackspace Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
import json

import os
import sys

POSSIBLE_TOPDIR = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]),
                                                os.pardir, os.pardir))
if os.path.exists(os.path.join(POSSIBLE_TOPDIR, 'stacktach')):
    sys.path.insert(0, POSSIBLE_TOPDIR)

from stacktach import models

if __name__ != '__main__':
    sys.exit(1)

config_filename = os.environ.get('STACKTACH_DEPLOYMENTS_FILE',
                                 'stacktach_worker_config.json')

def add_deployment_info():
    config = None
    with open(config_filename, "r") as f:
        config = json.load(f)

    deployments = config['deployments']
    for deployment in deployments:
        update_count = models.Deployment.objects.filter(
            name=deployment['name']).update(region=deployment['region'],
                                            data_center=deployment['data_center'])
    print "Updated %d rows" % update_count

add_deployment_info()

