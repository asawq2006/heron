# Copyright 2016 Twitter. All rights reserved.
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
''' opts.py '''
import logging
from heron.common.src.python.color import Log
from tornado.options import define


def set_verbose(cl_args):
  """ set verbose level """
  if cl_args['verbose']:
    Log.setLevel(logging.DEBUG)
  else:
    Log.setLevel(logging.INFO)


def set_tracker_url(cl_args):
  """ define global Tornado variable """
  define("tracker_url", cl_args["tracker_url"])
