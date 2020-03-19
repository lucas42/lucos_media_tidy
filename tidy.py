#! /usr/local/bin/python3

import requests, sys, json, os

def trackExists(url):
	if "rowan" in url:
		return False
	try:
		trackres = requests.head(url)
		return trackres.ok
	except requests.exceptions.RequestException:
		return False

if not os.environ.get("MEDIA_API"):
	sys.exit("\033[91mMEDIA_API not set\033[0m")
apiurl = os.environ.get("MEDIA_API")
pagecount = 0
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

		# First track has blank details, fix manually later
		if (track['trackid'] == 1):
			continue
		if trackExists(track['url']):
			#print("Track "+str(track["trackid"])+" exists")
			continue
		url = track['url']
		url = url.replace("http://", "https://")
		url = url.replace("medlib/ceol srl", "medlib/import/black/ceol srl")
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
		url = url.replace("rowan/Moosic/Sinead O'Connor", "black/ceol srl/artists/Sinead OConnor")
		url = url.replace("import/rowan/Moosic/Keane", "black/ceol srl/artists/Keane")
		url = url.replace("rowan/Moosic/Zutons, The/Tired Of Hanging Around (2006)", "black/ceol srl/artists/Zutons, The/Zutons - Tired Of Hanging Around", )
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
		url = url.replace("rowan/Moosic/Snow Patrol", "black/ceol srl/artists/Snow Patrol")
		url = url.replace("rowan/Moosic/View, The/Hats Off To The Buskers (2007)", "black/ceol srl/artists/View, The/The View - Hats Off To The Buskers")
		url = url.replace("rowan/Moosic/Kano/Home Sweet Home (2005)", "black/ceol srl/artists/Kano")
		url = url.replace("rowan/Moosic/Paris/Sonic Jihad (2003)", "black/ceol srl/artists/Paris/Sonic Jihad")
		url = url.replace("rowan/Moosic/Van Morrison", "black/ceol srl/artists/Van the Man")
		url = url.replace("rowan/Moosic/Leftfield/Leftism (1995)", "black/ceol srl/artists/Leftfield/Leftism")
		url = url.replace("Media to sort/Savage Garden Discography", "artists/Savage Garden")
		url = url.replace("Media to sort/Camper Van Beethoven", "artists/Camper Van Beethoven")
		url = url.replace("Media to sort/Sigur Ros", "artists/Sigur Ros")
		url = url.replace("Cranberries, The", "Cranberries")
		url = url.replace("rowan/Moosic/Game, The/The Documentary (2005)", "black/ceol srl/artists/Game/Game - The Documentary")
		url = url.replace("rowan/Moosic/Mamas & The Papas/Dream A Little Dream Of Me.mp3", "black/ceol srl/artists/Mamas and the Papas, The/Mamas And The Papas - Dream A Little Dream Of Me.mp3")
		url = url.replace("rowan/Moosic/Muse", "black/ceol srl/artists/Muse")
		url = url.replace(".wma", ".wma.ogg")
		url = url.replace("99%", "99%25")
		url = url.replace("rowan/Moosic/Kanye West", "black/ceol srl/artists/Kanye West")
		url = url.replace("Jackson, Micheal", "Jackson, Michael")
		url = url.replace("rowan/Moosic/View, The/Hats Off To The Buskers (2007)", "black/ceol srl/artists/View, The/The View - Hats Off To The Buskers")
		url = url.replace("rowan/Moosic/Kano/Home Sweet Home (2005)", "black/ceol srl/artists/Kano")
		url = url.replace("rowan/Moosic/Paris/Sonic Jihad (2003)", "black/ceol srl/artists/Paris/Sonic Jihad")
		url = url.replace("rowan/Moosic/Flogging Molly", "black/ceol srl/artists/Flogging Molly")
		url = url.replace("PussyCat Dolls &", "PussyCat Dolls %2526 ")
		url = url.replace("import/rowan/Moosic/Keane", "black/ceol srl/artists/Keane")
		url = url.replace("rowan/Moosic/Sinead O'Connor", "black/ceol srl/artists/O'Connor, Sinéad")
		url = url.replace("rowan/Moosic/Watercress", "black/ceol srl/artists/Watercress")
		url = url.replace("Watercress/Bummer (2001)", "Watercress/Bummer")
		url = url.replace("rowan/Moosic/Animaniacs, The", "black/ceol srl/Kids")
		url = url.replace("rowan/Moosic/Divers (French)", "black/ceol srl/Kids/Divers (French)")
		url = url.replace("rowan/Moosic/Game, The/The Documentary (2005)", "black/ceol srl/artists/Game/Game - The Documentary")
		url = url.replace("rowan/Moosic/Mamas & The Papas/California Dreaming.mp3", "black/ceol srl/artists/Mamas and the Papas, The/Mamas And The Papas - California Dreaming.mp3")
		url = url.replace("rowan/Moosic/Muse", "black/ceol srl/artists/Muse")
		url = url.replace("Absolution (2003)", "Muse - Absolution")
		url = url.replace("Origin Of Symmetry (2001)", "Muse - Origin Of Symmetry")
		url = url.replace("rowan/Moosic/Maximo Park/A Certain Trigger (2005)", "black/ceol srl/artists/Maximo Park/Maximo Park - A Certain Trigger")
		url = url.replace("rowan/Moosic/Levellers, The/Too Real (EP) (1998)", "black/ceol srl/artists/levellers/Too Real")
		url = url.replace("rowan/Moosic/Levellers, The/Just The One (EP) (1995)", "black/ceol srl/artists/levellers/Just The One EP")
		url = url.replace("Black Holes And Revelations (2006)", "Muse - Black Holes And Revelations")
		url = url.replace("Final Straw (2003)", "Final Straw")
		url = url.replace("When It's All Over We Still Have To Clear Up (2001)", "When It's All Over We Still Have To Clear Up")
		url = url.replace("Songs For Polarbears (1998)", "Songs For Polarbears")
		url = url.replace("Eyes Open (2006)", "Eyes Open")
		url = url.replace("Tired Of Hanging Around (2006)", "Tired Of Hanging Around")
		url = url.replace("rowan/Moosic/Ukulele Orchestra of GB", "black/ceol srl/artists/Ukulele Orchestra of GB")
		url = url.replace("", "")
		url = url.replace("", "")
		url = url.replace("", "")
		url = url.replace("", "")
		url = url.replace("", "")

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

		print("\033[91mTrack still doesn't exist: "+url+" (page "+str(pagecount)+")\033[0m")
	print("\033[92mPage "+str(pagecount)+" completed\033[0m")
	pagecount += 1
