import requests

site_list = ["https://www.w3schools.com/ai/ai_tensorflow_intro.asp","https://www.chess.com/game/live/75653394137","https://jut.su/nanatsu-taizai/season-2/episode-3.html","https://www.youtube.com/watch?v=jvFULnNpNLg&ab_channel=egoroff_channel","https://www.dota2.com/newfrontiers?v=2"]

for link in site_list:
    status = requests.get(link).status_code
    if status == 200 or status == 302:
        print(f"'{link}' link is ok!")
    else:
        print(f"'{link}' link isn`t work :( ")



