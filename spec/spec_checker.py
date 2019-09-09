import subprocess
import tempfile

import requests


def check_spec(id, spec_file):
    print('Detecting changes in the {0}'.format(id))
    base_url = 'https://develop.battle.net/assets/api/'
    spec_url = '{0}{1}'.format(base_url, spec_file)

    response = requests.get(spec_url)
    new_spec_file = tempfile.NamedTemporaryFile()
    new_spec_file.write(response.content)
    new_spec_file.seek(0)

    result = subprocess.run(["diff", spec_file, new_spec_file.name], capture_output=True)
    changed = bool(result.stdout)
    if bool(result.stdout):
        print('Changes in the {0} have been detected since last release!'.format(id))
        print('I need a human to look for possible deprecations..')
        print('-----------------------------------------------------')

        lines = result.stdout.decode('utf-8').split('\n')
        [print(l) for l in lines]
        print('-----------------------------------------------------')
    else:
        print('No API changes detected..')
    return changed


if __name__ == '__main__':
    assert not check_spec('WoW Community API', 'wow-community-api.json')
    assert not check_spec('WoW Game Data API', 'wow-game-data-api.json')
