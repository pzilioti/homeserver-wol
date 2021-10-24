#!/bin/bash
count=$(ps aux | grep '[g]unicorn' | wc -l)
if [ $count -lt 2 ]
then
        echo "reiniciar"
        cd /opt/homeserver-wol/
        source env/bin/activate
        nohup gunicorn -b :8000 app:app &
else
        echo "tudo ok"
fi