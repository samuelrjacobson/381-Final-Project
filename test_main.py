from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "status": "Hello, world"
    }

def test_get_video_list():
    response = client.get("/moviereviews/Harry_Potter")
    assert response.status_code == 200
    reviews_list = response.json()

    assert len(reviews_list) == 10  
    
    for review in reviews_list:
        assert not review['id'] == None
        assert not review['title'] == None
        assert not review['description'] == None

    assert "Harry Potter".upper() in str(reviews_list).upper()

def test_get_description():
    response = client.get("/descriptions/OBEVMnbPiRI")
    assert response.status_code == 200
    assert response.json() == "Hey Flick fanatics, here is a video exploring Peter Jackson's Lord of the Rings trilogy and why I believe it to be a masterpiece!\nEnjoy!\n\n#lotr"
    
    response = client.get("/descriptions/uXMAgwcP7e8")
    assert response.status_code == 200
    assert response.json() == "The Lord of the Rings trilogy is one of the best series of films ever made. The Fellowship of the Ring, The Two Towers, and The Return of the King are 3 perfect movies. Peter Jackson helped realize J.R.R. Tolkien's world into something great. But in this video essay, I'm going to take a look at all the aspects that went behind making the lord of the rings trilogy. So in this video essay, let's take a look at The Lord of the Rings... 19 Years Later\n\n__CHAPTERS____\n0:00 - Lord of the Rings... 19 Years Later\n2:15 - Tolkien's Influences\n9:30 - An Impossibly Great Production\n20:01 - Breakdown of a Battle\n25:37 - The Controversial Ending\n29:35 - An Unending Passion\n\nThis video took an immaculate amount of research, so I wanted to give a special thanks to the articles and videos that I researched:\n-https://www.youtube.com/watch?v=_3bAUqT9C18&t=25s\n-https://www.youtube.com/watch?v=gu0kVaRnrQg\n-https://www.youtube.com/watch?v=OrAT0cD4pvA&t=348s\n-https://www.youtube.com/watch?v=94yh1GIwiko&t=10s\n-https://denvercatholic.org/the-catholic-origins-of-the-lord-of-the-rings-and-other-truths-about-j-r-r-tolkien/\n-https://en.wikipedia.org/wiki/Production_of_The_Lord_of_the_Rings_film_series#filming \n-A special thanks to Kimer Lorens for posting many high quality clips of the lord of the rings movies on youtube!\n\nFor business inquiries please email:\n-thegoldmanbusiness@gmail.com\n\n✪ WHERE TO FIND THE GOLD MAN? ✪ \nTik Tok: www.tiktok.com/@the.gold.man\nInstagram: https://www.instagram.com/the.gold.man.yt/\nYouTube Shorts Channel: https://www.youtube.com/channel/UCo0gSn_jGnw_pwfTvPH7xjQ\nTwitter: https://twitter.com/TheGoldMan25\nMemes Subreddit: https://www.reddit.com/r/TheGoldManMemes/\n\n❗️WANT TO WATCH MORE OF ME?❗️\nTik Tok: www.tiktok.com/@the.gold.man\nInstagram: https://www.instagram.com/the.gold.man.yt/\nYouTube Shorts Channel: https://www.youtube.com/channel/UCo0gSn_jGnw_pwfTvPH7xjQ\n🍿2nd Channel🍿: https://www.youtube.com/channel/UCo0gSn_jGnw_pwfTvPH7xjQ\n🔶The Chatooine Show🔶: https://www.youtube.com/channel/UCwOnK_mz0A0yoGKIkFDalow/videos\n\nMemes Subreddit: https://www.reddit.com/r/TheGoldManMemes/\nTwitter: https://twitter.com/TheGoldMan25\nGold Man Is Live (Second Channel): https://www.youtube.com/channel/UCo0gSn_jGnw_pwfTvPH7xjQ\nThe Chatooine Show: https://www.youtube.com/playlist?list=PLc6_WgvDPz7TPPP4zMjw5Qh3vgLNXi4Lw\n\nThumbnail made by: Render Driver: https://instagram.com/renderdriver\n\n#lordoftherings #theringsofpower #videoessay\n\nA long time ago in 1937, JRR Tolkien decided to write the Hobbit. A book for children about a short guy who goes on an adventure. Little did he know how popular his story would become, but when it did he decided to write a more mature story afterwards. This time it was a trilogy called the Lord of the rings trilogy. And little did he know how popular that would become. Throughout history as movies and tv became more popular, there were Tolkien’s grand epic. Such as this animated movie that is frankly a lot of fun to watch. But in 1995, a man named Peter Jackson sent off on an adventure to adapt this Lord of the Rings trilogy to the big screen. After years of hard work at pre production, the actual production, and post production. The Lord of the Rings trilogy began with the fellowship of the ring in 2001, and concluded with the return of the king in 2003. These films went on to become 3 of the most successful films imaginable. Not only were these films huge hits amongst casual audiences, but hardcore Tolkien fans were mostly pleased and critics themselves loved the films. Return of the king to this day is tied for the most successful movies at the Oscars, winning 11 Oscars including best picture. Almost never does it happen where a blockbuster movie wins best picture, but Lord of the Rings managed to pull it off. This trilogy managed to capture the awe and imagination of almost everyone who watched it. I remember when I was younger and these movies came out, and for years all I could think about was rewatching the movies, playing the video game adaptations of the movies, and running around with my plastic swords pretending I was Aragorn fighting a bunch of orcs. Even with all this passion for the trilogy in the 2000s, that passion has not faded all these years later. This trilogy was so popular that Amazon decided to gamble over 1 billion dollars on the most expensive show ever made in the history of TV. So what made Lord of the Rings so popular? How did a story that was originally written in the 1950s move so many people decades upon decades later. What makes these movies arguably 3 of the best movies ever made? Well let’s go back in time almost a century to the beginning, and I mean the beginning.\nJohn Ronald Reuel Tolkein’s influence on the fantasy genre is immeasurable. He wrote The Hobbit in 1937 and went on to write his The Lord of the Rings Trilogy in the 1950s."

def test_get_in_other_language():
    response = client.get("/descriptions/fr/Avatar")
    reviews_list = response.json()
    assert response.status_code == 200
    
    assert len(reviews_list) == 10  
    
    for review in reviews_list:
        assert not review['id'] == None
        assert not review['title'] == None
        assert not review['description'] == None

    assert "Avatar".upper() in str(reviews_list).upper()
