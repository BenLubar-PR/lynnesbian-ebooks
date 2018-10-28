#!/usr/bin/env python3
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from mastodon import Mastodon
import argparse
import create

parser = argparse.ArgumentParser(description='Generate and post a toot.')
parser.add_argument('reply', metavar='reply', type=str, nargs='?', 
	help='ID of the status to reply to')
parser.add_argument('-s', '--simulate', dest='simulate', action='store_true',
	help="Print the toot to stdout without posting it")

args = parser.parse_args()

api_base_url = "https://botsin.space" #todo: this shouldn't be hardcoded

client = Mastodon(
        client_id="clientcred.secret", 
        access_token="usercred.secret", 
        api_base_url=api_base_url)

class nlt_fixed(markovify.NewlineText):
	def test_sentence_input(self, sentence):
		return True

toot = create.make_toot()
if not args.simulate:
	if toot['media'] != None:
		mediaID = client.media_post(toot['media'], description = toot['toot'])
		client.status_post(toot['toot'].replace("\n", " "),
			media_ids = [mediaID], visibility = "unlisted")
	else:
		client.status_post(toot['toot'], visibility = 'unlisted')
print(toot['toot'])
