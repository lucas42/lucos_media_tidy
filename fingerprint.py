#! /usr/local/bin/python3

import os, sys
import requests, taglib, acoustid, json
from urllib.parse import unquote

if not os.environ.get("MEDIA_API"):
	sys.exit("\033[91mMEDIA_API not set\033[0m")
apiurl = os.environ.get("MEDIA_API")
pagecount = 0
verbose = False
print("\033[0mStarting")
while True:
	dataresponse = requests.get(apiurl+"/tracks?page="+str(pagecount))
	if not dataresponse.ok:
		sys.exit("\033[91m** Error ** HTTP Status code "+str(dataresponse.status_code)+" returned by API: " +  dataresponse.text + "\033[0m")
	data = dataresponse.json()
	if (len(data) == 0):
		print("Have read all tracks")
		break
	for track in data:
		try:
			path = "/medlib" + unquote(track['url'].split("/medlib", 1)[1])
			id = str(track['trackid'])
			print(id, path)
			duration, fingerprint = acoustid.fingerprint_file(path, maxlength=60)
			trackdata = {
				"fingerprint": fingerprint.decode('UTF-8'),
				"duration": int(duration),
			}
			result = requests.patch(apiurl+"/tracks/"+id, data=json.dumps(trackdata), allow_redirects=False)
			if result.ok:
				if verbose:
					print ("\033[92m** OK**\033[0m", file=sys.stderr)
				tagresult = requests.put(apiurl+"/tags/"+id+"/fingerprint_version", data="2.0", allow_redirects=False)
			elif result.text.startswith("Duplicate"):
				dupid = result.text.split("track ", 1)[1].split(" ", 1)[0]
				print("\033[93m** Duplicate of "+dupid+"**\033[0m", file=sys.stderr)
				tagresult = requests.put(apiurl+"/tags/"+id+"/duplicates", data=dupid, allow_redirects=False)
			else:
				print ("\033[91m** Error ** HTTP Status code "+str(result.status_code)+" returned by API: " +  result.text.strip() + "\033[0m", file=sys.stderr)
				continue

			if tagresult.ok:
				if verbose:
					print ("\033[92m** Tag OK**\033[0m", file=sys.stderr)
			else:
				print ("\033[91m** Error ** HTTP Status code "+str(tagresult.status_code)+" returned by tag call to API: " +  result.text.strip() + "\033[0m", file=sys.stderr)
				continue
		except Exception as error:
			print ("\033[91m** Error ** " + str(error) + "\033[0m", file=sys.stderr)
	print("\033[92mPage "+str(pagecount)+" completed\033[0m")
	pagecount += 1


# VALIDATION SQL:
# SELECT fp.value, dup.value IS NOT NULL, COUNT(*) FROM track LEFT JOIN tag AS fp ON track.id = fp.trackid AND fp.predicateid = "fingerprint_version" LEFT JOIN tag AS dup ON track.id = dup.trackid AND dup.predicateid = "duplicates" GROUP BY fp.value, dup.value IS NOT NULL;