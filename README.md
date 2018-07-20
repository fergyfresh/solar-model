# Solar Model

## How to setup

You're going to need python3 because I only tested it with python3.6
it will probably work with python2, but just to be safe lets get python3.6
```
$ sudo apt-get install python3.6-dev
```

You're also going to want to have virtualenv installed as well.
```
sudo apt-get install virtualenv
```


Last thing you're wanna do before heading into the step by step walk through is go to
[NREL's developer website](https://developer.nrel.gov) and get an API Key for PVWatts.

```
# Download this repo
# Run this if you have virtualenv installed
$ virtualenv .venv -p python3.6
$ source .venv/bin/activate

# Skip to here if you have virtualenv installed
$ pip install -r requirements.txt
$ export API_KEY="thisisnotmyrealapikey"

$ python server.py
```

Now you can go to 127.0.0.1:4000 and input values within the ranges specified and click submit.

The data gets displayed after clicking submit and a CSV file gets created/appended to in the output directory.
