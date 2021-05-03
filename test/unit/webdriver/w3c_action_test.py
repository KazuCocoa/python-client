#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import httpretty
import pytest
from selenium.webdriver.common.action_chains import ActionChains

from test.unit.helper.test_helper import android_w3c_driver, appium_command, get_httpretty_request_body


class TestMultiAction(object):
    @httpretty.activate
    def test_json(self):
        expected_json = {
            "actions": [
                {
                    "type": "pointer",
                    "parameters": {"pointerType": "mouse"},
                    "id": "mouse",
                    "actions": [
                        {"type": "pointerMove", "duration": 250, "x": 1, "y": 2, "origin": "pointer"},
                        {"type": "pointerDown", "duration": 0, "button": 0},
                        {"type": "pointerUp", "duration": 0, "button": 0},
                    ],
                },
                {
                    "type": "key",
                    "id": "key",
                    "actions": [
                        {"type": "pause", "duration": 0},
                        {"type": "pause", "duration": 0},
                        {"type": "pause", "duration": 0},
                    ],
                },
            ]
        }
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/actions'),
        )
        actions = ActionChains(driver)
        actions.move_by_offset(1, 2)
        actions.click()
        actions.perform()
        assert expected_json == get_httpretty_request_body(httpretty.last_request())
