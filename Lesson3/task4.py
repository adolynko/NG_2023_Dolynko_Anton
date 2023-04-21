import requests

site_list = ["https://www.w3schools.com/ai/ai_tensorflow_intro.asp","https://www.chess.com/game/live/75653394137","https://jut.su/nanatsu-taizai/season-2/episode-3.html","https://www.youtube.com/watch?v=jvFULnNpNLg&ab_channel=egoroff_channel","https://www.dota2.com/newfrontiers?v=2"]

status = [f"{link}, is ok" if requests.get(link).status_code == 200 or requests.get(link).status_code == 302 else f"{link} , is fail" for link in site_list]
[print(item) for item in status]



