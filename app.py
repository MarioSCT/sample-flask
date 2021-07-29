from flask import Flask
from flask import render_template
import time
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("a.html")

@app.route("/p2/<nombres>")
def hello_world2(nombres):
    api_key = "RGAPI-b25e0415-0e10-46f1-9f4c-fc8a9135d37b"
    #Nombres recibido de parametro
    x = nombres.split(",")
    ts = int(round(time.time() * 1000))
    ts7 = ts - 604800000
    ts14 = ts - 1209600000


    fallos = []
    champs7 = []
    times7 = []
    wins7 = []
    kda7 = []
    wr7 = []
    champs14 = []
    times14 = []
    wins14 = []
    kda14 = []
    wr14 = []
    gameserror = 0
    gameposition = 0
    champsplayed = []
    enemychamps = []
    timesenemychamps = []
    contador14 = 0
    contador7 = 0
    for nombre in x:
        time.sleep(100)
        try:
            response = requests.get("https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + nombre + "?api_key=" + api_key + "")
            data = response.json()

            puuid = data["puuid"]

            try:
                response = requests.get("https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/" + puuid + "/ids?start=0&count=100&api_key=" + api_key + "")
                data = response.json()

                for i in range(0, len(data)):
                    matchid = data[i]

                    try:
                        response = requests.get("https://europe.api.riotgames.com/lol/match/v5/matches/" + matchid + "?api_key=" + api_key + "")
                        data2 = response.json()

                        if data2["info"]["gameStartTimestamp"] >= ts14:
                            if data2["info"]["queueId"] == 420:
                                contador14 = contador14 + 1
                                if data2["info"]["gameStartTimestamp"] >= ts7:
                                    contador7 = contador7 + 1
                                    print("7")
                                    for j in range(0, len(data2["metadata"]["participants"])):
                                        if data2["metadata"]["participants"][j] == puuid:
                                            gameposition = j

                                            esta = False
                                            pos = 0
                                            for k in range(0, len(champs7)):
                                                if champs7[k] == data2["info"]["participants"][gameposition]["championName"]:
                                                    esta = True
                                                    pos = k

                                            if esta == True:
                                                times7[pos] = times7[pos] + 1
                                                if gameposition < 5:
                                                    if data2["info"]["teams"][0]["win"] == True:
                                                        wins7[pos] = wins7[pos] + 1
                                                else:
                                                    if data2["info"]["teams"][1]["win"] == True:
                                                        wins7[pos] = wins7[pos] + 1

                                                kda7[pos][0] = kda7[pos][0] + data2["info"]["participants"][gameposition]["kills"]
                                                kda7[pos][1] = kda7[pos][1] + data2["info"]["participants"][gameposition]["deaths"]
                                                kda7[pos][2] = kda7[pos][2] + data2["info"]["participants"][gameposition]["assists"]

                                            else:
                                                champs7.append(data2["info"]["participants"][gameposition]["championName"])
                                                times7.append(1)
                                                if gameposition < 5:
                                                    if data2["info"]["teams"][0]["win"] == True:
                                                        wins7.append(1)
                                                    else:
                                                        wins7.append(1)
                                                else:
                                                    if data2["info"]["teams"][1]["win"] == True:
                                                        wins7.append(1)
                                                    else:
                                                        wins7.append(0)
                                                kda7.append([data2["info"]["participants"][gameposition]["kills"],
                                                             data2["info"]["participants"][gameposition]["deaths"],
                                                             data2["info"]["participants"][gameposition]["assists"]])

                                            #AQUI

                                else:
                                    print("14")
                                    for j in range(0, len(data2["metadata"]["participants"])):
                                        if data2["metadata"]["participants"][j] == puuid:
                                            gameposition = j

                                            esta = False
                                            pos = 0
                                            for k in range(0, len(champs14)):
                                                if champs14[k] == data2["info"]["participants"][gameposition]["championName"]:
                                                    esta = True
                                                    pos = k

                                            if esta == True:
                                                times14[pos] = times14[pos] + 1
                                                if gameposition < 5:
                                                    if data2["info"]["teams"][0]["win"] == True:
                                                        wins14[pos] = wins14[pos] + 1
                                                else:
                                                    if data2["info"]["teams"][1]["win"] == True:
                                                        wins14[pos] = wins14[pos] + 1

                                                kda14[pos][0] = kda14[pos][0] + data2["info"]["participants"][gameposition]["kills"]
                                                kda14[pos][1] = kda14[pos][1] + data2["info"]["participants"][gameposition]["deaths"]
                                                kda14[pos][2] = kda14[pos][2] + data2["info"]["participants"][gameposition]["assists"]

                                            else:
                                                champs14.append(data2["info"]["participants"][gameposition]["championName"])
                                                times14.append(1)

                                                if gameposition < 5:
                                                    if data2["info"]["teams"][0]["win"] == True:
                                                        wins14.append(1)
                                                    else:
                                                        wins14.append(1)
                                                else:
                                                    if data2["info"]["teams"][1]["win"] == True:
                                                        wins14.append(1)
                                                    else:
                                                        wins14.append(0)

                                                kda14.append([data2["info"]["participants"][gameposition]["kills"],
                                                              data2["info"]["participants"][gameposition]["deaths"],
                                                              data2["info"]["participants"][gameposition]["assists"]])

                                esta = False
                                pos = 0
                                for k in range(0, len(champs14)):
                                    if champs14[k] == data2["info"]["participants"][gameposition]["championName"]:
                                        esta = True
                                        pos = k

                                if esta == True:
                                    times14[pos] = times14[pos] + 1
                                    if gameposition < 5:
                                        if data2["info"]["teams"][0]["win"] == True:
                                            wins14[pos] = wins14[pos] + 1
                                    else:
                                        if data2["info"]["teams"][1]["win"] == True:
                                            wins14[pos] = wins14[pos] + 1

                                """
                                temp_lane = data2["info"]["participants"][gameposition]["individualPosition"]
                                temp_cont_lane = 1
                                temp_team = ""
                                temp_enemy = ""
                                if gameposition < 5:
                                    temp_team = "Blue"
                                else:
                                    temp_team = "Red"

                                for k in range(0, len(champs14)):
                                    if champs14[k] == data2["info"]["participants"][gameposition]["championName"]:
                                        if temp_team == "Blue":
                                            for l in range(5,10):
                                                print("linea: ", data2["info"]["participants"][l]["individualPosition"])
                                                if data2["info"]["participants"][l]["individualPosition"] == temp_lane:
                                                    temp_cont_lane = temp_cont_lane + 1
                                                    temp_enemy = data2["info"]["participants"][l]["championName"]
                                        elif temp_team == "Red":
                                            for l in range(0,5):
                                                print("linea: ", data2["info"]["participants"][l]["individualPosition"])
                                                if data2["info"]["participants"][l]["individualPosition"] == temp_lane:
                                                    temp_cont_lane = temp_cont_lane + 1
                                                    temp_enemy = data2["info"]["participants"][l]["championName"]

                                        print("linea temporal: ",temp_lane)
                                        print("contador de lineas: ",temp_cont_lane)
                                        if temp_cont_lane == 2:
                                            esta = False
                                            pos1 = ""
                                            for m in range(0,len(champsplayed)):
                                                if champsplayed[m] == data2["info"]["participants"][gameposition]["championName"]:
                                                    esta = True
                                                    pos1 = m

                                            if esta == True:
                                                esta2 = False
                                                for n in range(0,enemychamps[pos1]):
                                                    if enemychamps[pos1][n] == temp_enemy:
                                                        esta2 = True
                                                        timesenemychamps[pos1][n] = timesenemychamps[pos1][n] + 1

                                                if esta2 == False:
                                                    enemychamps[pos1].append(temp_enemy)
                                                    timesenemychamps[pos1].append(1)
                                            else:
                                                champsplayed.append(data2["info"]["participants"][gameposition]["championName"])
                                                enemychamps.append([temp_enemy])
                                                timesenemychamps.append([1])
                                    """



                                            

                    except:
                        gameserror = gameserror + 1

            except:
                fallos.append("No se ha encontrado el invocador " + nombre + "")

        except:
            fallos.append("No se ha encontrado el invocador " + nombre + "")

    for a in range(0,len(wins7)):
        wr7.append(round(wins7[a]/times7[a]*100))

    for a in range(0,len(wins14)):
        wr14.append(round(wins14[a]/times14[a]*100))

    for a in range(0,len(kda7)):
        kda7[a] = [round(kda7[a][0]/times7[a],1),round(kda7[a][1]/times7[a],1),round(kda7[a][2]/times7[a],1)]

    for a in range(0,len(kda14)):
        kda14[a] = [round(kda14[a][0]/times14[a],1),round(kda14[a][1]/times14[a],1),round(kda14[a][2]/times14[a],1)]

    for a in range(0,len(kda7)):
        if kda7[a][1] != 0:
            kda7[a].append(round((kda7[a][0]+kda7[a][2])/kda7[a][1],1))
        else:
            kda7[a].append(round(kda7[a][0] + kda7[a][2], 1))

    for a in range(0,len(kda14)):
        if kda14[a][1] != 0:
            kda14[a].append(round((kda14[a][0]+kda14[a][2])/kda14[a][1],1))
        else:
            kda14[a].append(round(kda14[a][0]+kda14[a][2],1))

    print("7 DIAS")
    print(champs7)
    print(times7)
    print(wr7)
    print(kda7)
    times7, wr7, champs7, kda7 = (list(t) for t in zip(*sorted(zip(times7,wr7,champs7,kda7),reverse=True)))
    print("7 DIAS NEW")
    print(champs7)
    print(times7)
    print(wr7)
    print(kda7)
    print("14 DIAS")
    print(champs14)
    print(times14)
    print(wr14)
    print(kda14)
    times14, wr14, champs14, kda14 = (list(t) for t in zip(*sorted(zip(times14, wr14, champs14, kda14), reverse=True)))
    print("14 DIAS NEW")
    print(champs14)
    print(times14)
    print(wr14)
    print(kda14)
    print("----------------------------")
    print("Games error",gameserror)
    print("Fallos",fallos)
    print("Nombres",nombres)

    winfinal7 = 0
    winfinal14 = 0
    timefinal7 = 0
    timefinal14 = 0
    for i in range(0,len(wins7)):
        winfinal7 = winfinal7 + wins7[i]
    for i in range(0, len(wins14)):
        winfinal14 = winfinal14 + wins14[i]
    for i in range(0,len(times7)):
        timefinal7 = timefinal7 + times7[i]
    for i in range(0,len(times14)):
        timefinal14 = timefinal14 + times14[i]

    wrfinal7 = round((winfinal7/timefinal7)*100)
    wrfinal14 = round((winfinal14/timefinal14)*100)
    print(wrfinal7)
    print(wrfinal14)
    print(winfinal7)
    print(timefinal7)
    print(winfinal14)
    print(timefinal14)


    posi = x
    rcchamps = []
    rcpercentage = []
    for i in range(0, len(champs14)):
        esta = False
        campeon = champs14[i]
        rcchamps.append(campeon)

        for j in range(0, len(champs7)):
            if champs7[j] == campeon:
                esta = True
                posi = j

        if esta == True:
            rcpercentage.append(round((times7[posi]/times14[i])*100))
        else:
            rcpercentage.append(0)

    print(rcchamps)
    print(rcpercentage)

    print("A1")
    rcpercentage, rcchamps = (list(t) for t in zip(*sorted(zip(rcpercentage, rcchamps), reverse=True)))
    print("A2")
    print(rcchamps)
    print(rcpercentage)

    print("////////////////////////////////////////////////////////")
    print("games 7: ",contador7)
    print("games 14: ", contador14)
    """
    print(champsplayed)
    print(enemychamps)
    print(timesenemychamps)

    
    fallos = []
    gameserror = 0
    gameposition = 0
    champsplayed = []
    timesplayed = []
    wins = []
    rol = []
    roltimes = []
    for nombre in x:

        try:
            response = requests.get("https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + nombre + "?api_key=" + api_key + "")
            data = response.json()

            puuid = data["puuid"]

            try:
                response = requests.get("https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/" + puuid + "/ids?start=0&count=20&api_key=" + api_key + "")
                data = response.json()

                for i in range(0,len(data)):
                    matchid = data[i]

                    try:
                        response = requests.get("https://europe.api.riotgames.com/lol/match/v5/matches/" + matchid + "?api_key=" + api_key + "")
                        data2 = response.json()

                        if data2["info"]["queueId"] == 420:

                            for j in range(0,len(data2["metadata"]["participants"])):
                                if data2["metadata"]["participants"][j] == puuid:
                                    gameposition = j

                            esta = False
                            pos = 0
                            for k in range(0,len(champsplayed)):
                                if champsplayed[k] == data2["info"]["participants"][gameposition]["championName"]:
                                    esta = True
                                    pos = k

                            lane = data2["info"]["participants"][gameposition]["individualPosition"]

                            if esta == True:
                                timesplayed[pos] = timesplayed[pos] + 1
                                if gameposition < 5:
                                    if data2["info"]["teams"][0]["win"] == True:
                                        wins[pos] = wins[pos] + 1
                                else:
                                    if data2["info"]["teams"][1]["win"] == True:
                                        wins[pos] = wins[pos] + 1

                                estarol = False
                                for l in range(0,len(rol[pos])):
                                    if rol[pos][l] == lane:
                                        roltimes[pos][l] = roltimes[pos][l] + 1
                                        estarol = True

                                if estarol == False:
                                    rol[pos].append(lane)
                                    roltimes[pos].append(1)

                            else:
                                champsplayed.append(data2["info"]["participants"][gameposition]["championName"])
                                timesplayed.append(1)
                                wins.append(1)
                                rol.append([lane])
                                roltimes.append([1])

                        else:
                            print("Fallo")

                    except:
                        gameserror = gameserror + 1

            except:
                fallos.append("No se ha encontrado el matchlist de "+nombre+"")

        except:
            fallos.append("No se ha encontrado el invocador "+nombre+"")

    wr = []
    for a in range(0,len(wins)):
        tmp = (wins[a]/timesplayed[a])*100
        wr.append(round(tmp,2))

    print("Champs",champsplayed)
    print("Wins", wr)
    print("Veces",timesplayed)
    print("Roles", rol)
    print("Veces", roltimes)
    """
    print(ts)
    print(ts7)
    print(ts14)
    minombre="Julian"
    return render_template("index.html",nombre=minombre,len7 = len(champs7),len14 = len(champs14),champs7 = champs7,times7=times7,wr7=wr7,kda7=kda7,champs14 = champs14,times14=times14,wr14=wr14,kda14=kda14,wrfinal7 = wrfinal7,wrfinal14 = wrfinal14,timefinal7 = timefinal7, timefinal14 = timefinal14,rcchamps=rcchamps,rcpercentage=rcpercentage,lenchanges = len(rcchamps))

@app.route("/scout/<nombres>")
def soloqScout(nombres):
    api_key = "RGAPI-ab5f4662-525a-4faa-bd72-e9d8ee80d339"
    # Nombres recibido de parametro
    x = nombres.split(",")

    #Timestamp
    ts = int(round(time.time() * 1000))
    ts7 = ts - 604800000
    ts14 = ts - 1209600000

    #Variables
    fallos = []
    champs7 = []
    times7 = []
    wins7 = []
    kda7 = []
    wr7 = []
    champs14 = []
    times14 = []
    wins14 = []
    kda14 = []
    wr14 = []
    gameserror = 0
    gameposition = 0
    contador14 = 0
    contador7 = 0
    champsplayed = []
    enemychamps = []
    timesenemychamps = []
    winsenemychamps = []

    #Main function
    for nombre in x:
        time.sleep(100)
        try:
            response = requests.get("https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + nombre + "?api_key=" + api_key + "")
            data = response.json()

            puuid = data["puuid"]

            try:
                response = requests.get("https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/" + puuid + "/ids?start=0&count=100&api_key=" + api_key + "")
                data = response.json()

                for i in range(0, len(data)):
                    matchid = data[i]

                    try:
                        response = requests.get("https://europe.api.riotgames.com/lol/match/v5/matches/" + matchid + "?api_key=" + api_key + "")
                        data2 = response.json()

                        if data2["info"]["gameStartTimestamp"] >= ts14:

                            if data2["info"]["queueId"] == 420:
                                contador14 = contador14 + 1
                                if data2["info"]["gameStartTimestamp"] >= ts7:
                                    contador7 = contador7 + 1

                                    for j in range(0, len(data2["metadata"]["participants"])):
                                        if data2["metadata"]["participants"][j] == puuid:
                                            gameposition = j

                                            esta = False
                                            pos = 0
                                            for k in range(0, len(champs7)):
                                                if champs7[k] == data2["info"]["participants"][gameposition]["championName"]:
                                                    esta = True
                                                    pos = k

                                            if esta == True:
                                                times7[pos] = times7[pos] + 1
                                                if gameposition < 5:
                                                    if data2["info"]["teams"][0]["win"] == True:
                                                        wins7[pos] = wins7[pos] + 1
                                                else:
                                                    if data2["info"]["teams"][1]["win"] == True:
                                                        wins7[pos] = wins7[pos] + 1

                                                kda7[pos][0] = kda7[pos][0] + data2["info"]["participants"][gameposition]["kills"]
                                                kda7[pos][1] = kda7[pos][1] + data2["info"]["participants"][gameposition]["deaths"]
                                                kda7[pos][2] = kda7[pos][2] + data2["info"]["participants"][gameposition]["assists"]

                                            else:
                                                champs7.append(data2["info"]["participants"][gameposition]["championName"])
                                                times7.append(1)
                                                kda7.append([data2["info"]["participants"][gameposition]["kills"],
                                                             data2["info"]["participants"][gameposition]["deaths"],
                                                             data2["info"]["participants"][gameposition]["assists"]])
                                                if gameposition < 5:
                                                    if data2["info"]["teams"][0]["win"] == True:
                                                        wins7.append(1)
                                                    else:
                                                        wins7.append(0)
                                                else:
                                                    if data2["info"]["teams"][1]["win"] == True:
                                                        wins7.append(1)
                                                    else:
                                                        wins7.append(0)


                                            #14 AQUI
                                            esta = False
                                            pos = 0
                                            for k in range(0, len(champs14)):
                                                if champs14[k] == data2["info"]["participants"][gameposition]["championName"]:
                                                    esta = True
                                                    pos = k

                                            if esta == True:
                                                times14[pos] = times14[pos] + 1
                                                if gameposition < 5:
                                                    if data2["info"]["teams"][0]["win"] == True:
                                                        wins14[pos] = wins14[pos] + 1
                                                else:
                                                    if data2["info"]["teams"][1]["win"] == True:
                                                        wins14[pos] = wins14[pos] + 1

                                                kda14[pos][0] = kda14[pos][0] + data2["info"]["participants"][gameposition]["kills"]
                                                kda14[pos][1] = kda14[pos][1] + data2["info"]["participants"][gameposition]["deaths"]
                                                kda14[pos][2] = kda14[pos][2] + data2["info"]["participants"][gameposition]["assists"]

                                            else:
                                                champs14.append(data2["info"]["participants"][gameposition]["championName"])
                                                times14.append(1)
                                                kda14.append([data2["info"]["participants"][gameposition]["kills"],data2["info"]["participants"][gameposition]["deaths"],data2["info"]["participants"][gameposition]["assists"]])
                                                if gameposition < 5:
                                                    if data2["info"]["teams"][0]["win"] == True:
                                                        wins14.append(1)
                                                    else:
                                                        wins14.append(0)
                                                else:
                                                    if data2["info"]["teams"][1]["win"] == True:
                                                        wins14.append(1)
                                                    else:
                                                        wins14.append(0)

                                            temp_lane = data2["info"]["participants"][gameposition]["individualPosition"]
                                            temp_cont_lane = 1
                                            temp_enemy = ""
                                            if gameposition < 5:
                                                temp_team = "Blue"
                                            else:
                                                temp_team = "Red"

                                            if temp_team == "Blue":
                                                for l in range(5, 10):

                                                    if data2["info"]["participants"][l]["individualPosition"] == temp_lane:
                                                        temp_cont_lane = temp_cont_lane + 1
                                                        temp_enemy = data2["info"]["participants"][l]["championName"]
                                            elif temp_team == "Red":
                                                for l in range(0, 5):

                                                    if data2["info"]["participants"][l]["individualPosition"] == temp_lane:
                                                        temp_cont_lane = temp_cont_lane + 1
                                                        temp_enemy = data2["info"]["participants"][l]["championName"]

                                            if temp_cont_lane == 2:

                                                esta = False
                                                pos = 0
                                                for k in range(0, len(champsplayed)):
                                                    if champsplayed[k] == data2["info"]["participants"][gameposition]["championName"]:
                                                        esta = True
                                                        pos = k

                                                if esta == True:

                                                    esta2 = False
                                                    pos2 = 0
                                                    for l in range(0, len(enemychamps[pos])):
                                                        if enemychamps[pos][l] == temp_enemy:
                                                            esta2 = True
                                                            pos2 = l

                                                    if esta2 == True:
                                                        timesenemychamps[pos][pos2] = timesenemychamps[pos][pos2] + 1
                                                        if gameposition < 5:
                                                            if data2["info"]["teams"][0]["win"] == True:
                                                                winsenemychamps[pos][pos2] = winsenemychamps[pos][pos2] + 1
                                                        else:
                                                            if data2["info"]["teams"][1]["win"] == True:
                                                                winsenemychamps[pos][pos2] = winsenemychamps[pos][pos2] + 1

                                                    else:
                                                        enemychamps[pos].append(temp_enemy)
                                                        timesenemychamps[pos].append(1)
                                                        if gameposition < 5:
                                                            if data2["info"]["teams"][0]["win"] == True:
                                                                winsenemychamps[pos].append(1)
                                                            else:
                                                                winsenemychamps[pos].append(0)
                                                        else:
                                                            if data2["info"]["teams"][1]["win"] == True:
                                                                winsenemychamps[pos].append(1)
                                                            else:
                                                                winsenemychamps[pos].append(0)

                                                else:
                                                    champsplayed.append(data2["info"]["participants"][gameposition]["championName"])
                                                    enemychamps.append([temp_enemy])
                                                    timesenemychamps.append([1])

                                                    if gameposition < 5:
                                                        if data2["info"]["teams"][0]["win"] == True:
                                                            winsenemychamps.append([1])
                                                        else:
                                                            winsenemychamps.append([0])
                                                    else:
                                                        if data2["info"]["teams"][1]["win"] == True:
                                                            winsenemychamps.append([1])
                                                        else:
                                                            winsenemychamps.append([0])


                                else:
                                    for j in range(0, len(data2["metadata"]["participants"])):
                                        if data2["metadata"]["participants"][j] == puuid:
                                            gameposition = j

                                            esta = False
                                            pos = 0
                                            for k in range(0, len(champs14)):
                                                if champs14[k] == data2["info"]["participants"][gameposition]["championName"]:
                                                    esta = True
                                                    pos = k

                                            if esta == True:
                                                times14[pos] = times14[pos] + 1
                                                if gameposition < 5:
                                                    if data2["info"]["teams"][0]["win"] == True:
                                                        wins14[pos] = wins14[pos] + 1
                                                else:
                                                    if data2["info"]["teams"][1]["win"] == True:
                                                        wins14[pos] = wins14[pos] + 1

                                                kda14[pos][0] = kda14[pos][0] + data2["info"]["participants"][gameposition]["kills"]
                                                kda14[pos][1] = kda14[pos][1] + data2["info"]["participants"][gameposition]["deaths"]
                                                kda14[pos][2] = kda14[pos][2] + data2["info"]["participants"][gameposition]["assists"]

                                            else:
                                                champs14.append(data2["info"]["participants"][gameposition]["championName"])
                                                times14.append(1)
                                                kda14.append([data2["info"]["participants"][gameposition]["kills"],data2["info"]["participants"][gameposition]["deaths"],data2["info"]["participants"][gameposition]["assists"]])
                                                if gameposition < 5:
                                                    if data2["info"]["teams"][0]["win"] == True:
                                                        wins14.append(1)
                                                    else:
                                                        wins14.append(0)
                                                else:
                                                    if data2["info"]["teams"][1]["win"] == True:
                                                        wins14.append(1)
                                                    else:
                                                        wins14.append(0)

                                            temp_lane = data2["info"]["participants"][gameposition]["individualPosition"]
                                            temp_cont_lane = 1
                                            temp_enemy = ""
                                            if gameposition < 5:
                                                temp_team = "Blue"
                                            else:
                                                temp_team = "Red"

                                            if temp_team == "Blue":
                                                for l in range(5, 10):

                                                    if data2["info"]["participants"][l]["individualPosition"] == temp_lane:
                                                        temp_cont_lane = temp_cont_lane + 1
                                                        temp_enemy = data2["info"]["participants"][l]["championName"]
                                            elif temp_team == "Red":
                                                for l in range(0, 5):

                                                    if data2["info"]["participants"][l]["individualPosition"] == temp_lane:
                                                        temp_cont_lane = temp_cont_lane + 1
                                                        temp_enemy = data2["info"]["participants"][l]["championName"]

                                            if temp_cont_lane == 2:

                                                esta = False
                                                pos = 0
                                                for k in range(0, len(champsplayed)):
                                                    if champsplayed[k] == data2["info"]["participants"][gameposition]["championName"]:
                                                        esta = True
                                                        pos = k

                                                if esta == True:

                                                    esta2 = False
                                                    pos2 = 0
                                                    for l in range(0, len(enemychamps[pos])):
                                                        if enemychamps[pos][l] == temp_enemy:
                                                            esta2 = True
                                                            pos2 = l

                                                    if esta2 == True:
                                                        timesenemychamps[pos][pos2] = timesenemychamps[pos][pos2] + 1
                                                        if gameposition < 5:
                                                            if data2["info"]["teams"][0]["win"] == True:
                                                                winsenemychamps[pos][pos2] = winsenemychamps[pos][pos2] + 1
                                                        else:
                                                            if data2["info"]["teams"][1]["win"] == True:
                                                                winsenemychamps[pos][pos2] = winsenemychamps[pos][pos2] + 1

                                                    else:
                                                        enemychamps[pos].append(temp_enemy)
                                                        timesenemychamps[pos].append(1)

                                                        if gameposition < 5:
                                                            if data2["info"]["teams"][0]["win"] == True:
                                                                winsenemychamps[pos].append(1)
                                                            else:
                                                                winsenemychamps[pos].append(0)
                                                        else:
                                                            if data2["info"]["teams"][1]["win"] == True:
                                                                winsenemychamps[pos].append(1)
                                                            else:
                                                                winsenemychamps[pos].append(0)

                                                else:
                                                    champsplayed.append(data2["info"]["participants"][gameposition]["championName"])
                                                    enemychamps.append([temp_enemy])
                                                    timesenemychamps.append([1])

                                                    if gameposition < 5:
                                                        if data2["info"]["teams"][0]["win"] == True:
                                                            winsenemychamps.append([1])
                                                        else:
                                                            winsenemychamps.append([0])
                                                    else:
                                                        if data2["info"]["teams"][1]["win"] == True:
                                                            winsenemychamps.append([1])
                                                        else:
                                                            winsenemychamps.append([0])


                    except:
                        gameserror = gameserror + 1

            except:
                fallos.append("No se ha encontrado el invocador " + nombre + "")

        except:
            fallos.append("No se ha encontrado el invocador " + nombre + "")

    print("////////////////////////////////////////////////////////")
    print("Games error", gameserror)
    print("Fallos", fallos)
    print("Nombres", nombres)
    print("////////////////////////////////////////////////////////")
    print("games 7: ", contador7)
    print("games 14: ", contador14)
    print("////////////////////////////////////////////////////////")
    print("champs: ", champsplayed)
    print("enemy: ", enemychamps)
    print("times: ", timesenemychamps)
    print("wins: ", winsenemychamps)
    print("////////////////////////////////////////////////////////")

    for a in range(0, len(wins7)):
        wr7.append(round(wins7[a] / times7[a] * 100))

    for a in range(0, len(wins14)):
        wr14.append(round(wins14[a] / times14[a] * 100))

    for a in range(0, len(kda7)):
        kda7[a] = [round(kda7[a][0] / times7[a], 1), round(kda7[a][1] / times7[a], 1), round(kda7[a][2] / times7[a], 1)]

    for a in range(0, len(kda14)):
        kda14[a] = [round(kda14[a][0] / times14[a], 1), round(kda14[a][1] / times14[a], 1),
                    round(kda14[a][2] / times14[a], 1)]

    for a in range(0, len(kda7)):
        if kda7[a][1] != 0:
            kda7[a].append(round((kda7[a][0] + kda7[a][2]) / kda7[a][1], 1))
        else:
            kda7[a].append(round(kda7[a][0] + kda7[a][2], 1))

    for a in range(0, len(kda14)):
        if kda14[a][1] != 0:
            kda14[a].append(round((kda14[a][0] + kda14[a][2]) / kda14[a][1], 1))
        else:
            kda14[a].append(round(kda14[a][0] + kda14[a][2], 1))
    print(champs7)
    print(times7)
    print(wr7)
    print(kda7)
    times7, wr7, champs7, kda7 = (list(t) for t in zip(*sorted(zip(times7, wr7, champs7, kda7), reverse=True)))
    print(champs14)
    print(times14)
    print(wr14)
    print(kda14)
    times14, wr14, champs14, kda14 = (list(t) for t in zip(*sorted(zip(times14, wr14, champs14, kda14), reverse=True)))

    winfinal7 = 0
    winfinal14 = 0
    timefinal7 = 0
    timefinal14 = 0
    for i in range(0, len(wins7)):
        winfinal7 = winfinal7 + wins7[i]
    for i in range(0, len(wins14)):
        winfinal14 = winfinal14 + wins14[i]
    for i in range(0, len(times7)):
        timefinal7 = timefinal7 + times7[i]
    for i in range(0, len(times14)):
        timefinal14 = timefinal14 + times14[i]

    wrfinal7 = round((winfinal7 / timefinal7) * 100)
    wrfinal14 = round((winfinal14 / timefinal14) * 100)

    posi = x
    rcchamps = []
    rcpercentage = []
    for i in range(0, len(champs14)):
        esta = False
        campeon = champs14[i]
        rcchamps.append(campeon)

        for j in range(0, len(champs7)):
            if champs7[j] == campeon:
                esta = True
                posi = j

        if esta == True:
            rcpercentage.append(round((times7[posi] / times14[i]) * 100))
        else:
            rcpercentage.append(0)

    htmlchamps = []
    htmlenemy = []
    htmltimes = []
    htmlwins = []
    for i in range(0,len(timesenemychamps)):
        for j in range(0, len(timesenemychamps[i])):
            if timesenemychamps[i][j] > 1:
                htmlchamps.append(champsplayed[i])
                htmlenemy.append(enemychamps[i][j])
                htmltimes.append(timesenemychamps[i][j])
                htmlwins.append(round( (winsenemychamps[i][j]/timesenemychamps[i][j]) * 100))



    return render_template("index.html", len7=len(champs7), len14=len(champs14), champs7=champs7,
                           times7=times7, wr7=wr7, kda7=kda7, champs14=champs14, times14=times14, wr14=wr14,
                           kda14=kda14, wrfinal7=wrfinal7, wrfinal14=wrfinal14, timefinal7=timefinal7,
                           timefinal14=timefinal14, rcchamps=rcchamps, rcpercentage=rcpercentage,
                           lenchanges=len(rcchamps),htmlchamps = htmlchamps,htmltimes=htmltimes,htmlenemy=htmlenemy,lenhtml=len(htmlchamps),htmlwins=htmlwins)