# -*- coding: utf-8 -*-
from __future__ import print_function

import json
import requests
from time import sleep
from pprint import pprint


API_URL = 'https://api-v3.mojepanstwo.pl/dane'
MP_URL = API_URL + '/poslowie.json'


def get_mp_data():
    params = {
        'page': 1,
        'limit': 1000,
        'conditions[poslowie.kadencja]': 8,
    }
    output = []
    while True:
        response = requests.get(API_URL, params=params)
        data = response.json().get('Dataobject', None)
        if (data is None) or (not data):
            break
        output += data
        params['page'] += 1
    return output


def get_twitter_info(twitter_account_id):
    url = API_URL + '/twitter_accounts/' + str(twitter_account_id)
    sleep(1) # be nice to the api
    response = requests.get(url)
    data = response.json()['data']
    twitter_id = data['twitter_accounts.twitter_id']
    twitter_name = data['twitter_accounts.twitter_name']
    return twitter_id, twitter_name


if __name__ == '__main__':
    mps = get_mp_data()
    mps_out = []

    for posel in mps:
        posel_id = posel['id']
        slug = posel['slug']
        imiona = posel['data']['poslowie.imiona']
        nazwisko = posel['data']['poslowie.nazwisko']
        twitter_account_id = posel['data']['poslowie.twitter_account_id']
        twitter_id = None
        twitter_name = None
        if twitter_account_id and int(twitter_account_id) > 0:
            twitter_id, twitter_name = get_twitter_info(twitter_account_id)
        mps_out.append({
            'id': posel_id,
            'slug': slug,
            'imiona': imiona,
            'nazwisko': nazwisko,
            'twitter_id': twitter_id,
            'twitter_name': twitter_name,
        })
        pprint(mps_out[-1])

    with open('data/poslowie.json', 'wt') as f:
        f.write(json.dumps(mps_out))

