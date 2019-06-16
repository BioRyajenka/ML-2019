import requests
import time

from datetime import datetime
from dateutil.relativedelta import relativedelta
from collections import defaultdict

last_months = 12
sleep_seconds = 0.02
traders_number = 500


def get_all_traders():
    params = {'limit': traders_number, 'offset': 0, 'sort': 'rating.asc'}
    r = requests.get('https://alpari.com/invest/pamm.json', params=params).json()
    time.sleep(sleep_seconds)

    return r['data']['items']


def ids_of_traders(traders):
    return [trader[0] for trader in traders]


def get_trader_hourly_monitoring(id):
    ret = []
    print(f'Getting data for trader with id={id}')

    for r in range(last_months):
        params = {
            'start': str(datetime.utcnow().date() - relativedelta(months=r+1)),
            'end': str(datetime.utcnow().date() - relativedelta(months=r))
        }

        r = requests.get(f'https://alpari.com/api/ru/pamm/{id}/monitoring/hourly_all_candle.json', params=params).json()
        time.sleep(sleep_seconds)
        ret += r['data']
    return ret


def write_data_to_file(traders_ids, filename):
    time_data = defaultdict(lambda: {})

    for trader_id in traders_ids:
        print(get_trader_hourly_monitoring(trader_id))
        for dtime, \
                return_open, return_high, return_low, return_close, \
                trding_open, trding_high, trding_low, trding_close, \
                invest \
                in get_trader_hourly_monitoring(trader_id):
            time_data[dtime][trader_id] = return_close

    with open(filename, 'w') as f:
        print(",".join(['TIME'] + [str(trader_id) for trader_id in traders_ids]), file=f)
        for dtime in sorted(time_data.keys()):
            print(",".join([str(dtime)] +
                            [(str(time_data[dtime][trader_id]) if trader_id in time_data[dtime] else "")
                             for trader_id in traders_ids]), file=f)


traders = get_all_traders()
traders_ids = ids_of_traders(traders)

print(traders_ids)
# write_data_to_file(traders_ids, "data/data.txt")