# -*- coding: utf-8 -*-
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

from __future__ import print_function
import argparse
import time

parser = argparse.ArgumentParser(description='Pour some beers.')


parser.add_argument('beers', metavar='beers_to_pour', type=int,
                    help='how many beers to pour.')


parser.add_argument('--scale', metavar='scale', type=int, default=1,
                    help='how many nodes pouring beer.')


def pour(beers):
    return u"🍺" * beers


def main():
    args = parser.parse_args()

    print("\nPouring beers...\n")

    for beer in pour(args.beers):
        time.sleep(.7 / args.scale)
        print(beer, end="", flush=True)

    time.sleep(.7)
    print("\n\nCheers! 🍻")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nNo Beers for you guys 😢")
