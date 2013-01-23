# The FixMyStreet Game

NOTE: This is a work in progress, and not currently running on the web.
Contributions welcome, unfortunately the core team at mySociety don't have the
resources to work on this project at the moment.

The idea behind the FMS game is that anyone with some time could start the game,
it would geolocate them and then it would list nearby issues that need
attention. It would then guide the user to walk there (a bit of exercise!) and
let them update the status of the report and add info if needed (more
description, another photo, etc).

Currently the game is a web app that you can access using the browser on your
mobile phone. There is no reason why it could not be a mobile app as well
though.

# Getting started

## Dev instance of FixMyStreet

To work with this code you'll need an instance of
[FixMyStreet](https://github.com/mysociety/fixmystreet) running - there are
[extensive install notes](http://code.fixmystreet.com/install/) on the
FixMyStreet documentation site.

## Postgres running locally

We use a postgres database. Other databases might work too, but we've not tried
them.

## Setting up the FMS Game code

FMS Game is written in python using the Django framework. These instructions
should get a local instance running for you. These instructions assume an
installation onto a *nix platform.

```bash
# clone this repo locally (or create a fork and then clone that)
git clone https://github.com/mysociety/fmsgame.git
```

```bash
# go to the directory just created, create a virtualenv and activate it
cd fmsgame
virtualenv .venv
source .venv/bin/activate
````

```bash
# install the python requirements
pip install -r requirements.txt
```

```bash
# create the config_local.py file and fill in the values
cp fmsgame_project/config_local.py.example fmsgame_project/config_local.py
$EDITOR fmsgame_project/config_local.py
 ```

```bash
# create the database needed and create the tables in it
createdb fmsgame
./manage.py syncdb
```

