# Change IP Alert

A simple but useful python script, that alert you via Pushbullet when the IP of your device changes.

## Instalation

- Requests
```bash
pip install public-ip
```
- Pushbullet
```bash
pip3 install pushbullet.py
```

## Configuration

Just update the file config.json with your own api key from Pushbullet then run the script:
```
python ChangeIPAlert.py
```

If you are on linux, you can use cron to schedule the task. See [crontab guru](https://crontab.guru/examples.html) to more details.
Thanks to vterron for the [public-ip](https://github.com/vterron/public-ip) module, that's a great job.