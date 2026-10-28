#!/usr/bin/env python3
"""Record the identity of the Data seed made by hdiutil in the workflow."""
import hashlib
import json
import plistlib

info = plistlib.load(open('data-info.plist', 'rb'))
data = open('owner-data-32.cdr', 'rb').read()
report = dict(
    volume_uuid=info.get('VolumeUUID'),
    bytes=len(data),
    sha256=hashlib.sha256(data).hexdigest(),
    source='iPad7,1 17.7.11 private/var excluding staged_system_apps',
    guest_mutable=True,
    production_storage_qualified=False,
)
open('seed.json', 'w').write(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
