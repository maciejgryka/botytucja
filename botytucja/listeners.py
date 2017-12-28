# -*- coding: utf-8 -*-
from __future__ import print_function

import logging

import tweepy


logger = logging.getLogger('botytucja')


class FollowStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        logger.info(status)
        logger.info(status.text)
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            return False
