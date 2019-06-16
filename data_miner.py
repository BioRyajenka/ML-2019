import requests
import time

from collections import defaultdict



def get_all_traders():
    params = {}
    params['limit'] = 10
    params['offset'] = 0
    params['sort'] = 'rating.asc'
    r = requests.get('https://alpari.com/invest/pamm.json', params=params).json()

    return r['data']['items']


def ids_of_traders(traders):
    return [trader[0] for trader in traders]


def get_trader_hourly_monitoring(id):
    r = requests.get(f'https://alpari.com/chart/pamm/{id}/return/hourly.json').json()
    return r['data']


traders = get_all_traders()
traders_ids = ids_of_traders(traders)

time_data = defaultdict(lambda: {})


for trader_id in traders_ids:
    print(f'collecting data for trader with id={trader_id}')
    for dtime, return_ in get_trader_hourly_monitoring(trader_id):
        time_data[dtime][trader_id] = return_
    time.sleep(0.1)


with open('mini_data.txt', 'w') as f:
    print(", ".join(['TIME'] + [str(trader_id) for trader_id in traders_ids]), file=f)
    for dtime in sorted(time_data.keys()):
        print(", ".join(map(str, [dtime] + [time_data[dtime][trader_id] for trader_id in traders_ids])), file=f)

