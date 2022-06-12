Source code for neb.cx gitshortener
-------------

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
[![Active Development](https://img.shields.io/badge/Maintenance%20Level-Actively%20Developed-brightgreen.svg)](https://gist.github.com/cheerfulstoic/d107229326a01ff0f333a1d3476e068d)

Git-Shortener is a github/gitlab link shortener. I created this service around
2/22, but accedentily deleted it. This is a re-write.

This project uses the FLAW stack:
Flask sqLite Apache Waitress

To setup, 

```
pip3 install -r requirements.txt
```

Then you can edit `config.py` to your liking. After you are done with that you can

```
python3 app.py
```

to start.

IPs from links.sqlite are encoded, if you would like to decode an ip to view it you can run

```
python3 DecodeIP.py
```

and follow the steps it gives you

Note: I am not responsible for any vulnerabilities this program could have, or data leakage. Use at your own risk!
