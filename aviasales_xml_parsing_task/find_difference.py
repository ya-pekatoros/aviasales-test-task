from datetime import datetime


def find_data_differences(data1, data2, differences=None):  # noqa: C901

    if differences is None:
        differences = {}

    all_keys = set(data1.keys()) | (set(data2.keys()))

    for key in all_keys:
        if key not in data2:
            differences.setdefault(f'deleted {key}', data1[key])
        elif key not in data1:
            differences.setdefault(f'added {key}', data2[key])
        elif data1[key] == data2[key]:
            pass
        else:
            if not isinstance(data1[key], dict) or not isinstance(data2[key], dict):
                differences.setdefault(f'deleted {key}', data1[key])
                differences.setdefault(f'added {key}', data2[key])
                if 'time_stamp' in key:
                    date1 = datetime.strptime(data1[key], '%Y-%m-%dT%H%M')
                    date2 = datetime.strptime(data2[key], '%Y-%m-%dT%H%M')
                    difference = date2 - date1
                    print_ = (
                        f"{difference.days} days, {difference.seconds//3600} hours, "
                        f"{(difference.seconds//60)%60} minutes"
                    )
                    alert = 'arrival' if 'arrival' in key else 'departure'
                    differences.setdefault(f'Attention! The time of {alert} was change by', print_)

            else:
                differences.setdefault(key, find_data_differences(data1[key], data2[key]))

    dif_keys = list(differences.keys())
    dif_keys = sorted(dif_keys, key=lambda elem: 3 if "deleted" in elem else 2 if "added" in elem else 1)
    differences = {i: differences[i] for i in dif_keys}

    return differences
