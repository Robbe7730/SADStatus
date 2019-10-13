#!/usr/bin/env python3

from app.app import db, models

db.create_all()

services = {
    "Website": "https://robbevanherck.be/",
    "DelayMap": "https://delaymap.robbevanherck.be/",
    "CommaFeed": "https://commafeed.robbevanherck.be/",
    "Radicale": "https://radicale.robbevanherck.be/",
}

for name, url in services.items():
    db.session.add(models.Service(name, url))
db.session.commit()
