"""All Rights Reserved.

    Licensed under the Apache License, Version 2.0 (the "License"); you may
    not use this file except in compliance with the License. You may obtain
    a copy of the License at

         http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
    License for the specific language governing permissions and limitations
    under the License.
"""

import time


class StopWatch:
    """Stop Watch class"""

    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def start(self):
        """Start the counter"""
        while True:
            text = "{:02}:{:02}:{:02}".format(
                self.hours, self.minutes, self.seconds)
            print(text, end="\r", flush=True)
            time.sleep(1)
            self.count()

    def count(self):
        """Increment seconds by one, and increment all the rest"""
        self.seconds += 1
        if self.seconds >= 60:
            self.seconds = 0

            self.minutes += 1
            if self.minutes >= 60:
                self.minutes = 0
                self.hours += 1

    def __str__(self):
        result = ("\n"
                  "Hours: {}\n"
                  "Minutes: {}\n"
                  "Seconds: {}")

        return result.format(self.hours, self.minutes, self.seconds)


if __name__ == "__main__":
    WATCH = StopWatch()
    try:
        WATCH.start()
    except KeyboardInterrupt:
        print(WATCH)
