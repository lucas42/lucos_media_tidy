#! /usr/local/bin/python3

import requests, sys, json, os

def trackExists(url):
	try:
		trackres = requests.head(url)
		return trackres.ok
	except requests.exceptions.RequestException:
		return False

if not os.environ.get("MEDIA_API"):
	sys.exit("\033[91mMEDIA_API not set\033[0m")
apiurl = os.environ.get("MEDIA_API")
pagecount = 520
pagecount = 142
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
		if trackExists(track['url']):
			#print("Track "+str(track["trackid"])+" exists")
			continue
		url = track['url']
		url = url.replace("http://", "https://")
		url = url.replace("medlib/ceol srl", "medlib/import/black/ceol srl")
		url = url.replace("import/black/ceol srl/artists/Watercress", "import/rowan/Moosic/Watercress")
		url = url.replace("Watercress/Bummer", "Watercress/Bummer (2001)")
		url = url.replace("Media to sort/Chumbawamba - ABCDEFG (2010) - Alternative [www.torrentazos.com]", "artists/Chumbawamba/ABCDEFG%20(2010)")
		url = url.replace("Media to sort/Chumbawamba - ","artists/Chumbawamba/")
		url = url.replace("Media to sort/Yes . Discography", "artists/Yes")
		url = url.replace("#", "%23")
		url = url.replace("Media to sort/Symphony No. 1 (The Lord of the Rings)", "Themes%20Soundtrack/Symphony No. 1 (The Lord of the Rings)")
		url = url.replace("Media to sort/Bloodhound gang", "artists/Bloodhound gang")
		url = url.replace("Media to sort/OMD - Discography", "artists/OMD")
		url = url.replace("Media to sort/Slade - 1969-2007", "artists/Slade")
		url = url.replace("Media to sort/The human league-Albums", "artists/Human League, The")
		url = url.replace("Media to sort/Noah And The Whale", "artists/Noah and the Whale/Noah And The Whale")
		url = url.replace("Media to sort/Clannad (Celtic) - 19 Albums Reseeded", "artists/Clannad")
		url = url.replace("Enya %26 P.Diddy", "Enya %2526 P.Diddy")
		url = url.replace("help%21", "help%2521")
		url = url.replace("...and", "and")
		url = url.replace("...And", "And")
		url = url.replace("A_singsong_and_a_scrap/Chumbawamba - A Singsong And A Scrap (2005) - Folk - www.torrentazos.com By FEFE2003", "A Singsong And A Scrap (2005)")
		url = url.replace("...Here's", "Here's")
		url = url.replace("Phill Collins %2526 Eric Clapton", "Phil Collins & Eric Clapton")
		url = url.replace("Sting %2526 The Police", "Sting & The Police")
		url = url.replace("black/ceol srl/artists/Sinead OConnor", "rowan/Moosic/Sinead O'Connor")
		url = url.replace("black/ceol srl/artists/Keane", "import/rowan/Moosic/Keane")
		url = url.replace("black/ceol srl/artists/Zutons, The/Zutons - Tired Of Hanging Around", "rowan/Moosic/Zutons, The/Tired Of Hanging Around (2006)")
		url = url.replace("black/ceol srl/artists/Ukulele Orchestra of GB", "rowan/Moosic/Ukulele Orchestra of GB")
		url = url.replace("%252526 ", "& ")
		url = url.replace("%2526 ", "& ")
		url = url.replace("%26 ", "&")
		url = url.replace("&Whitney", "& Whitney")
		url = url.replace("black/ceol srl/artists/Game/Game - The Documentary", "rowan/Moosic/Game, The/The Documentary (2005)")
		url = url.replace("black/ceol srl/artists/Mamas and the Papas, The/Mamas And The Papas - ", "rowan/Moosic/Mamas & The Papas/")
		url = url.replace("Trio  Ill", "Trio Ill")
		url = url.replace("black/ceol srl/artists/Muse/Muse - Black Holes And Revelations", "rowan/Moosic/Muse/Black Holes And Revelations (2006)")
		url = url.replace("black/ceol srl/artists/Muse/Muse - Absolution", "rowan/Moosic/Muse/Absolution (2003)")
		url = url.replace("black/ceol srl/artists/Muse/Muse - Origin Of Symmetry", "rowan/Moosic/Muse/Origin Of Symmetry (2001)")
		url = url.replace("black/ceol srl/artists/Muse", "rowan/Moosic/Muse")
		url = url.replace("black/ceol srl/Kids/Animaniacs", "rowan/Moosic/Animaniacs, The/Animaniacs")
		url = url.replace("black/ceol srl/Kids/Divers  (French)", "rowan/Moosic/Divers (French)")
		url = url.replace("black/ceol srl/artists/Flogging Molly", "rowan/Moosic/Flogging Molly")
		url = url.replace("black/ceol srl/artists/Maximo Park/A Certain Trigger", "rowan/Moosic/Maximo Park/A Certain Trigger (2005)")
		url = url.replace("black/ceol srl/artists/Maximo Park/Maximo Park - A Certain Trigger", "rowan/Moosic/Maximo Park/A Certain Trigger (2005)")
		url = url.replace("black/ceol srl/artists/Kanye West", "rowan/Moosic/Kanye West")
		url = url.replace("Jackson, Micheal", "Jackson, Michael")
		url = url.replace("black/ceol srl/artists/levellers/Too Real", "rowan/Moosic/Levellers, The/Too Real (EP) (1998)")
		url = url.replace("black/ceol srl/artists/levellers/Just The One EP", "rowan/Moosic/Levellers, The/Just The One (EP) (1995)")
		url = url.replace("black/ceol srl/artists/Snow Patrol", "rowan/Moosic/Snow Patrol")
		url = url.replace("black/ceol srl/artists/View, The/The View - Hats Off To The Buskers", "rowan/Moosic/View, The/Hats Off To The Buskers (2007)")
		url = url.replace("black/ceol srl/artists/Kano", "rowan/Moosic/Kano/Home Sweet Home (2005)")
		url = url.replace("black/ceol srl/artists/Paris/Sonic Jihad", "rowan/Moosic/Paris/Sonic Jihad (2003)")
		url = url.replace("black/ceol srl/artists/Van the Man", "rowan/Moosic/Van Morrison")
		url = url.replace("Snow Patrol/Snow Patrol - ", "Snow Patrol/")
		url = url.replace("/When It's All Over We Still Have To Clear Up/", "/When It's All Over We Still Have To Clear Up (2001)/")
		url = url.replace("/Songs For Polarbears", "/Songs For Polarbears (1998)")
		url = url.replace("/Eyes Open", "/Eyes Open (2006)")
		url = url.replace("black/ceol srl/artists/Leftfield/Leftism", "rowan/Moosic/Leftfield/Leftism (1995)")
		url = url.replace("", "")
		url = url.replace("", "")
		url = url.replace("", "")
		url = url.replace("", "")
		url = url.replace("", "")
		url = url.replace("", "")
		url = url.replace("", "")
		url = url.replace("", "")
		url = url.replace("", "")

		tracksToDelete = [
			1239,  # Old flac file I don't care about
			14079, # Duplicate file
		]
		if track['trackid'] in tracksToDelete:
			continue

		if trackExists(url):
			trackdata = {
				"url": url,
				"duration": track["duration"],
				"fingerprint": track["fingerprint"],
			}
			result = requests.put(apiurl+"/tracks/"+str(track['trackid']), data=json.dumps(trackdata), allow_redirects=False, headers={"If-None-Match": "*"})
			if result.status_code == 500 and result.text == "UNIQUE constraint failed: track.url\n":
				print("\033[91mDuplicate track "+str(track['trackid'])+", url: "+url+" - Skipping\033[0m")
				continue
			if result.status_code != 200:
				sys.exit("\033[91m** Error ** HTTP Status code "+str(result.status_code)+" returned by API "+apiurl+"/tracks/"+str(track['trackid'])+" : " +  result.text + "\033[0m")
			print("Updated track "+str(track["trackid"])+" to "+url)
			continue

		knownMissing = [
			"Savage Garden",
			"Eurovision 2006 - Finlandia - Lordi - Hard Rock Hallelujah",
			"Camper Van Beethoven",
			"Sigur Ros",
			"Abba",
			"little britain - only gay in the village (little britian mix).mp3",
			"Sound FX",
			"Danny Kaye - The Ugly Duckling",
			"Tweenies - The Wheels On The Bus",
			"The Fast Food Rockers - The Fast Food Song",
			"Trup, Trup a Chapillín",
			"Hello Children Everywhere",
			"Bob the Builder -Mambo No.5",
			#"Clash",
			"Lionel Richie & The Commodors",
			"Françoise Hardy",
			#"Pink Floyd",
			#"Sum 41",
			#"Hayseed Dixie",
			"The Cranberries",
			#"Editors",
			"Shitmat",
			#"Fleetwood Mac",
			"Donovon Frankenreiter",
			#"Housemartins",
			"Jason Donovan",
			"All Saints",
			"Spice Girls",
			#"Game, The",
			#"The Game",
			"Sclub 7",
			#"Razorlight",
			"Jackson and his computer band",
			"Babylon Zoo",
			#"Mamas and the Papas",
			#"Mamas & The Papas",
			#"Blunt, James",
			"Fíréin, Na",
			#"Alanis Morissette",
			"Oldfield, Mike",
			"manfredd mann",
			#"Coldplay",
			#"KRS One",
			#"Rage Against the Machine",
			"Atomic Kitten",
			"Simon & Garfunkel",
			"Stefani, Gwen",
			"Tony Benn",
			#"Daft Punk",
			"Lighthouse Family",
			"Bananarama",
			#"Cat Empire",
			"Déanta",
			#"Half man half biscuit",
			"Crimera, The",
			"Imogen Heap",
			"Kíla",
			"Larrikin Love",
			#"Jackson, Michael",
			"Seal",
			"Taylor, James",
			#"Muse - The String Quartet",
			".wma.ogg",
			#"Kanye West",
			"Wild Flowers",
			"Warwick, Dionne",
			"Ultravox",
			#"Sex Pistols",
			#"levellers/One way of life",
			"Tiesto, DJ",
			"Simply Red",
			"Réalta 2000",
			#"Pouges",
			"Talitha MacKenzie",
			"Tatu",
			#"Kano",
			#"Hats Off To The Buskers",
			#"Paris/Sonic Jihad",
		]
		if any(missing in url for missing in knownMissing):
			continue
		print("\033[91mTrack still doesn't exist: "+url+" (page "+str(pagecount)+")\033[0m")
	print("\033[92mPage "+str(pagecount)+" completed\033[0m")
	pagecount += 1
