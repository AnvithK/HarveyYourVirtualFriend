import webbrowser
name = input("What is your name?")
print("Hi {0}! I am your artificial friend Harvey!".format(name))
continueForward = input("""Would you like to continue forward? 
        Type yes or no: """)
def quizShow():
    return webbrowser.open("https://docs.google.com/presentation/d/1rXtEToGUqqhEYTYEE2oIt7rVaCafyuTa/edit#slide=id.p1")

def endofConversation():
    print("It was awesome talking to you come back to see me soon! Unless its 2AM!")
    quizOrNo = input("Would you like to continue to a trivia quiz? Type yes or no: ")
    if quizOrNo == "yes":
        quizShow()
        return
    else:
        print("Talk to you later!")
        return

feeling = input("""How are you feeling today?
a. Good
b. GREAT!
c. Bad
d. Horrible
e. normal
Type it here: """)


if feeling == 'a':

    print('I am feeling great. I can’t wait to get to know you! Just wait until I make your day even better!')

elif feeling == 'b':

    print('Me too! We have a lot in common! I can see this conversation going far!')

elif feeling == 'c':

    print('I’m sorry to hear that but I can cheer you up! I want to make you feel better.')

elif feeling == 'd':

    print('Sorry to hear. Well, I bet I can cheer you up! Just remember “Every storm has its rainbow”')

else:

    print('I’m glad you’re doing fine. Just wait until I make your day even better!')

covidConcern = float(input("""How worried are you about COVID-19 on a scale from 1-10? 
Hint: 1 (Doesn’t bother me)
5(Not anxious but alert)
10(I am scared to death that humans will go extinct)
Type it here: """))

if 1<=covidConcern<2.5:
    print('Glad, you’re optimistic! Just don’t forget to wear your mask!')
elif 2.5<= covidConcern < 5:
    print('Glad, you’re being safe, just don’t forget to wear your mask!')
elif 6<=covidConcern<=8:
    print('Don’t worry too much. Let’s be patient and this pandemic will blow over. Don\'t be anxious, be alert! Just don’t forget to wear your mask!')
elif 8 < covidConcern:
    print('Don’t worry too much. Let’s be patient and this pandemic will blow over. Don\'t be anxious, be alert! Just don’t forget to wear your mask!')
else:
    print('Good! This is where you should be! Just don’t forget to wear your mask and practice social distancing!')


favThing = input("""What’s your favorite thing to do?
a. Watch TV
b. Sports
c. Arts & Crafts
d. Bake
e. Learn""")

if favThing == 'a':
    movieOrTV = input("""Do you like to watch 
    a. movies 
    b. TV shows
    Type here: """)
    if movieOrTV == 'a':
        movieType = input("""What type of movies do you like?
        a. fantasy
        b. drama
        c. sci-fi
        d. action
        e. mystery
        f. horror
        g. superhero
        Type here: """)
        if movieType == 'a':
            print("""Some fantasy movies are just so good!!! My favorite fantasy movie series is Harry Potter.
            Here is a list of Harry Potter movies to watch in chronological order. . . 
            
            
1. Harry Potter And The Sorcerer's Stone
2. Harry Potter And The Chamber Of Secrets
3. Harry Potter And The Prisoner Of Azkaban
4. Harry Potter And The Goblet Of Fire
5. Harry Potter And The Order Of The Phoenix
6. Harry Potter And The Half-Blood Prince
7. Harry Potter And The Deathly Hallows Part 1
8. Harry Potter And The Deathly Hallows Part 2""")
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        elif movieType == 'b':
            print("""Unfortunately, I don’t watch drama movies. 
            However, here are some movies my friends recommend to watch. . .
1. Jaws
2. 1917
3. Ford v Ferrari""")
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        elif movieType == 'c':
            print("""Some sci-fi movies are just memorable! 
            They are so intriguing to watch! Here are some movies I recommended you to watch?
            
            
1. Ad Astra
2.  Ready Player One
3.  Avatar
4. Pacific Rim
5. Pacific Rim Uprising
6. Atlantic Rim
7. Geostorm""")
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        elif movieType == 'd':
            print("""
            # Some action movies are just memorable! They are so intriguing to watch! 
            Here are some recommended movies to watch. . .
            
            
1. Spectre
2. Casino Royale
3. Venom
4. Charlies angels
5. Fast and Furious series
6. Mission Impossible: Fallout
""")
            missionImpossible = input("""Are you interested in the movies to watch for Mission Impossible in chronological order? 
            Type yes or no here: """)
            if missionImpossible == "yes":
                print("""Here is the list of the Mission Impossible series in chronological order
                1. Mission Impossible
                2. Mission Impossible 2
                3. Mission Impossible 3
                4. Mission Impossible 4
                5. Mission Impossible: Ghost Protocol
                6. Mission Impossible: Rogue Nation
                7. Mission Impossible: Fallout""")
            else:
                pass
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        elif movieType == 'e':
            print("""I love mystery movies! They are not spooky, yet so intriguing to watch!!! 
            Here are some recommended movies to watch. . . 
                     
1. Knives Out
2. Murder Mystery
3. Dora the Lost City of Gold
4. Pokemon Detective Pikachu
5. The Commuter
6. Sherlock Holmes
7. Holmes and Watson""")
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()

        elif movieType == 'f':
            print("""I can’t believe you can watch horror movies without running away from the movie!! 
            I'm too scared to watch horror movies! Sorry! I don’t know much about horror movies. 
            But my friends recommend some good horror movies. Here are a list to watch. . .

1. A Quiet Place
2. A Quiet Place 2
3. Us
4. The Meg
5. Truth or Dare
6. Scooby-Doo
7. 47 Meters Down""")
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        else:
            print("I love superhero movies too!!! Especially DC and Marvel Movies!!!")
            marvelOrDC = input("""What movies do you like more?
            a. DC movies
            b. Marvel movies""")
            if marvelOrDC == 'a':
                print("""DC movies are really good! I don’t know why, but they are so underrated! You have to watch them!!!
If yes say/ list -- Here is the order to watch the movies. . .

1. Man of Steel (2013)
2. Batman v Superman: Dawn of Justice (2016)
3. Suicide Squad (2016)
4. Wonder Woman (2017)
5. Justice League (2017)
6. Aquaman (2018)
7. Shazam! (2019)
8. Birds of Prey (2020)

 NOTE: The series is still running. So some of the things shown are not complete.""")
                print(continueForward)
                if continueForward == 'yes':
                    endofConversation()
            else:
                print("""I love Marvel movies too! Here a list of 
                Marvel movies to watch in chronological order. . .
        
1. Iron Man
2. The Incredible Hulk
3. Iron Man 2
4. Thor
5. Captain America: The First Avenger
6. The Avengers
7. Iron Man 3
8. Thor: The Dark World
9. Captain America: The Winter Soldier
10.Guardians of the Galaxy
11. Avengers: Age of Ultron
12. Ant-Man
13. Captain America: Civil War
14. Doctor Strange
15. Guardians of the Galaxy 2
16. Spider-Man Homecoming
17. Thor Ragnorak
18. Black Panther
19. Captain Marvel
20. Avengers Infinity War
21. Ant-Man and the Wasp
22. Captain Marvel
23. Avengers Endgame
24. Spider-Man: Far From Home

NOTE: This series is still running. There are more Marvel movies coming out soon. """)
                print(continueForward)
                if continueForward == 'yes':
                    endofConversation()

    else:
        TVGenre = input("""What TV show genre do you like to watch?
a. Mystery
b. superhero
c.  Reality tv-shows
d.   Horror
e.  Sci fi
f. fantasy
g. Crime""")
        if TVGenre == 'a':
            print("""I love mystery TV shows! Here are a list of mystery TV shows I recommend. 
            My three favorites are The Mentalist, Elementary, and Sherlock! 
            Those tv shows are the best I have ever seen! I highly urge you to watch them. 
            Other tv shows my friends have recommended me to watch are . . .
            
            
1. CSI Miami
2. CSI NY
3. Elementary
4. The Mentalist
5. Sherlock
6. Alcatraz
7. Roswell
8. Riverdale""")
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        elif TVGenre == 'b':
            print("""I love superhero TV shows! Here is a list of superhero tv shows I recommend. 
            My two favorite shows are the Flash and Arrow! 
            These shows are so good!!! I would highly recommend you to watch them. 
            Other tv shows my friends have recommended me to watch are . . .
            
            
1. Flash
2. Arrow
3. Agents of Shield
4. Teen titans go
5. Agent Carter
6. Smallville
7. Cartoon tv shows of any superhero you admire""")
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        elif TVGenre == 'c':
            print("""I don’t watch reality TV shows unfortunately. 
            Here is a list of reality tv shows my friends recommend. . . 
1. Million dollar listings NY
2. Million dollar listings LA
3. The real housewives of NYC
4. The real housewives of Beverly Hills
5. All American""")
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        elif TVGenre == 'd':
            print("""I don’t watch horror tv shows unfortunately. I get scared of horror TV shows!
            You're SO Lucky that you can watch horror TV shows without being scared!!!!
            Here is a list of horror tv shows my friends recommend. . .
            
            
1. Scooby Doo
2. Supernatural
3. Stranger Things
4. The Vampire Diaries
5. My Babysitter’s a Vampire""")
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        elif TVGenre == 'e':
            print("""I love sci-fi tv shows! 
            Here is a list of sci-fi tv shows I recommend. . .
            
            
1. Upload
2. Doctor Who
3. Agents of S.H.I.E.L.D
4. The Flash
5. Blood Drive""")
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        elif TVGenre == 'f':
            print("""I love fantasy tv shows! 
            Here is a list of fantasy tv shows I recommend. . .
            
            
1. Game of Thrones
2. SpongeBob Squarepants
3. Smallville
4. The Flash""")
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()

        else:
            print("""I LOVE crime tv shows too!!! They are the best type of tv shows you can ever watch!!! 
            Personally, my favorite tv shows are The Mentalist, Elementary, and Sherlock. 
            TV shows that my friends frequently recommend me to watch are. . .
            
            
1. The Mentalist
2. Elementary
3. Sherlock
4. CSI Miami
5. Alcatraz
6. Luther""")
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
elif favThing == 'b':
    favSport = input("""What is your favorite sport?
    a. American football
    b. Soccer(Football/futboll)
    c. Basketball
    d. Volleyball
    e. Golf
    f. Tennis""")
    if favSport == 'a':
        playOrWatch = input("""Would you rather 
        a. play football 
        b. watch football 
        Type your answer here: """)
        if playOrWatch == 'a':
            favPosition = input('What is your favorite position to play in football? ')
            print("Playing {0}, is also my favorite position too! I really love contributing touchdowns to my team!".format(favPosition))
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        else:
            favTeam = input("What is your favorite team? ")
            print("My favorite team is also {0} too!!! I’m so glad you like sports! Its such a nice way to pass time!".format(favTeam))
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
    elif favSport == 'b':
        playOrWatch = input("""Would you rather 
                a. play soccer(football/futbol) 
                b. watch soccer(football/futbol) 
                Type your answer here: """)
        if playOrWatch == 'a':
            favPosition = input('What is your favorite position to play in soccer(football/futbol)? ')
            print("Playing {0}, is also my favorite position too! I really love contributing to goals for my team!".format(favPosition))
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        else:
            favTeam = input("What is your favorite team? ")
            print("My favorite team is also {0} too!!! I’m so glad you like sports! Its such a nice way to pass time!".format(favTeam))
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
    elif favSport == 'c':
        playOrWatch = input("""Would you rather 
                        a. play basketball 
                        b. watch basketball 
                        Type your answer here: """)
        if playOrWatch == 'a':
            favPosition = input('What is your favorite position to play in basketball? ')
            print(
                "Playing {0}, is also my favorite position too! I really love contributing baskets to my team!".format(
                    favPosition))
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        else:
            favTeam = input("What is your favorite team? ")
            print(
                "My favorite team is also {0} too!!! I’m so glad you like sports! Its such a nice way to pass time!".format(
                    favTeam))
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
    elif favSport == 'd':
        playOrWatch = input("""Would you rather 
                        a. play volleyball 
                        b. watch volleyball 
                        Type your answer here: """)
        if playOrWatch == 'a':
            favPosition = input('What is your favorite position to play in volleyball? ')
            print(
                "Playing {0}, is also my favorite position too! I really love contributing points to my team!".format(
                    favPosition))
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        else:
            favTeam = input("What is your favorite team? ")
            print(
                "My favorite team is also {0} too!!! I’m so glad you like sports! Its such a nice way to pass time!".format(
                    favTeam))
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
    elif favSport == 'e':
        playOrWatch = input("""Would you rather 
                        a. play golf 
                        b. watch golf 
                        Type your answer here: """)
        if playOrWatch == 'a':
            favPosition = input('What is your average score in golf? ')
            print(
                "Playing {0}, is also my average score! I really love making holes in golf!".format(favPosition))
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        else:
            favTeam = input("Who is your favorite player? ")
            print(
                "My favorite player is also {0} too!!! I’m so glad you like sports! Its such a nice way to pass time!".format(
                    favTeam))
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
    else:
        playOrWatch = input("""Would you rather 
                        a. play tennis 
                        b. watch tennis 
                        Type your answer here: """)
        if playOrWatch == 'a':
            favPosition = input('Do you like playing singles or doubles in tennis? ')
            print(
                "I also love playing {0}! I really like playing competitive in tennis!".format(favPosition))
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        else:
            favTeam = input("What is your favorite team? ")
            print(
                "My favorite team is also {0} too!!! I’m so glad you like sports! Its such a nice way to pass time!".format(
                    favTeam))
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
elif favThing == 'c':
    print("""Arts and crafts can be so relaxing for the brain! I'm glad you enjoy them!""")
    favArt = input("""What is your favorite way to draw? 
    a. drawing
    b. painting
    c. Legos
    d. DIY Art
    e. sewing
    f. jewelry
    Type response here: """)
    if favArt == 'b':
        paintingOptions = input("""Arts and crafts can be so calming for the brain! I’m glad you enjoy them!
        What do you like to paint with? 
        a. Watercolor 
        b. Acrylic 
        c. Spray Paint
 		Type answer here: """)

        if paintingOptions == "a":
            print("Here is a video that will keep you occupied for watercolor painting. . .")
            print(continueForward)
            if continueForward == 'yes':
                webbrowser.open("https://youtu.be/fe58aMtF_2U")

            endofConversation()
        elif paintingOptions == "b":
            print("Here is a video that will keep you occupied for acrylic painting. . .")
            print(continueForward)
            if continueForward == 'yes':
                webbrowser.open("https://youtu.be/VjCGJb5ltZM")

            endofConversation()

        else:
            print("Here is a video that will keep you occupied for spray painting. . .")
            print(continueForward)
            if continueForward == 'yes':
                webbrowser.open("https://youtu.be/3rqqrwRTqh0")

            endofConversation()
    elif favArt == 'a':
        drawing = input("""What is your favorite way to draw? 
        a. Realistic 
        b. Cartoonistic """)
        if drawing == 'a':
            print("To keep you occupied, here is a link for realistic art drawing. ")
            print(continueForward)
            if continueForward == 'yes':
                webbrowser.open("https://youtu.be/vrN4TOY8rSw")

            endofConversation()

        else:
            print("To keep you occupied, here is a link for realistic art drawing. ")
            print(continueForward)
            if continueForward == 'yes':
                webbrowser.open("https://youtu.be/mOhajtMP8lk")

            endofConversation()


    elif favArt == 'c':
        #
        # -Legos -- What size lego’s do you like? (A) Big ones  (B) Small ones
        # 		--- Arts and crafts can be so relaxing for the brain! I’m glad you enjoy them
        # 			---- Would you like to take a general quiz or do you want to end our convo here?
        #
        #
        # 				--- If general quiz (insert quiz variable here)
        # 				--- If the end of the convo say “It was awesome talking to you come back and see me soon! Unless it’s 2 am then lemme sleep plz!  But in the meantime check out these cool pictures of crazy legos people built! https://images.app.goo.gl/6XQdEBxNw288ViAh7
        #
        print('''Building legos is so fun!! I also love it too!''')
        print(continueForward)
        if continueForward == 'yes':
            webbrowser.open("https://images.app.goo.gl/6XQdEBxNw288ViAh7")

        endofConversation()
    elif favArt == 'd':
        where = input("""Here is a link for DIY sites to look for making future art projects. . . 
        1. https://youtu.be/rkktkvA24pE 
        2. https://youtu.be/EFaHbFq0JUI  
        3. https://youtu.be/z4HcWDfO1IQ""")
        print(continueForward)
        if continueForward == 'yes':
            endofConversation()

    elif favArt == 'e':
        sewing = input("""What is your favorite thing to sew? 
        a. Hats  
        b. Scarves 
        c. Gloves 
        d. other(type out favorite thing to sew)
        Type your answer here: """)
        if sewing == sewing:
            print("I also love sewing {0} too!!! We have so much in common!!!".format(sewing))
            print("""Here is a link to a site to learn more about sewing. . .
            
            https://youtu.be/nFoITRWJNPQ""")
        print(continueForward)
        if continueForward == 'yes':
            endofConversation()

    else:
        jewelry = input("""What is your favorite type of jewelry to make? 
        a. Necklaces 
        b. Earings  
        c. Bracelets  
        d. Anklets
        Type your answer here: """)
        print("I also love to make {0} too!!! We have so much in common!!!".format(jewelry))
        print("""Here is a link to a site to learn more about making bracelets . . .
        
        https://youtu.be/4Fn1EiJbrxU
        
        Here is a link to a site to learn more about making necklaces. . . 
        
         https://youtu.be/c7c5tAmZ5z0 
         """)
        print(continueForward)
        if continueForward == 'yes':
            endofConversation()

elif favThing == 'd':
    bake = input("""What is your favorite thing to bake?
    a. cookies
    b. cakes
    c. bread
    d. chocolate confections
    e. frozen deserts
    Type your answer here: """)
    if bake == 'a':
        favCookies = input("""What is your favorite type of cookie to bake? 
        a. Chocolate Chip 
        b. Snickerdoodle
        c. Sugar 
        d. Oatmeal Raisin 
        e. Other(type it out)
        Type your answer here: """)
        print("I also love baking and eating {0} cookies!!! They are so good!!! ")
        print("""Here is a site to look at if you want to learn more about baking . . .
         
         https://www.loveandlemons.com/baking-recipes/""")
        print(continueForward)
        if continueForward == 'yes':
            endofConversation()
    elif bake == "b":
        typeCake = input("""What is your favorite type of cake to bake? 
        a. Red Velvet Cake  
        b. Carrot Cake 
        c. Pound Cake 
        d. Sponge Cake 
        e. Bundt Cake 
        f. Ice Cream Cake 
        g. Other(type it out)
        Type your answer here: """)

        print("""Baking can be such a nice way to relax, have fun, and make something tasty! 
        I’m so glad you like baking!""")
        print("""Please check out this site to learn more about baking recipes. . .
        
        https://www.loveandlemons.com/baking-recipes/""")
        print(continueForward)
        if continueForward == 'yes':
            endofConversation()
    elif bake == "c":
        bread = input("""What is your favorite type of bread to bake? 
        a. Banana Bread  
        b. Sourdough 
        c. Brioche 
        d. Baguette 
        e. Rye Bread 
        f. Other
        Type your answer here: """)

        print("I love baking sourdough bread!!! I can't believe that we both love to bake bread.")
        print("""Please check out this site to learn more about baking recipes. . .
        
        https://www.loveandlemons.com/baking-recipes/""")
        print(continueForward)
        if continueForward == 'yes':
            endofConversation()

    elif bake == "d":
        choco = input("""What is your favorite type of chocolate confections to make? 
        a. Chocolate Truffles  
        b. Fudge 
        c. Marzipan 
        d. Toffee
        Type your answer here: """)
        print("""Please check out this site to learn more about baking recipes. . . 
        
        https://www.loveandlemons.com/baking-recipes/""")
        print(continueForward)
        if continueForward == 'yes':
            endofConversation()
    else:
        frozen = input("""What is your favorite type of frozen desserts to make? 
        a. Frozen Yogurt  
        b. Gelato 
        c. Ice cream  
        d. Sorbett 
        e. Italian Ice 
        f. Other
        Type your answer here: """)
        print("""Please check out this site to learn more about baking recipes. . . 

        https://www.loveandlemons.com/baking-recipes/""")
        print(continueForward)
        if continueForward == 'yes':
            endofConversation()


else:
    favMost = input("""What do you like most?
a. Book reading
b. Math
c. Science
d. History
e. Writing
Type your response here: """)
    if favMost == 'a':
        genre1 = input("""Why do you like reading: """)
        if genre1 == genre1:
            genre2 = input("""What fiction genre do you like to read?
a. Fantasy
b. Science Fiction
c. Realistic Fiction
d. Suspense/Thriller
e. Historical Fiction
f. Mystery(includes crime)
Type your response here: """)
            if genre2 == "a":
                print("""I love fantasy books!! Especially the Harry potter series!!!
Here is a list of the Harry Potter books to read in chronological order. . .


1. Harry Potter and the Sorcerer’s Stone
2. Harry Potter and the Chamber of Secrets
3. Harry Potter and the Prisoner of Azkaban
4. Harry Potter and the Goblet of Fire
5. Harry Potter and the Order of the Phoenix
6. Harry Potter and the Half-Blood Prince
7. Harry Potter and the Deathly Hallows""")
                print(continueForward)
                if continueForward == 'yes':
                    endofConversation()
            elif genre2 == 'b':
                print("""I love science fiction books!! Here is a list of books I recommend reading . . .


1. Last Day on Mars: Chronicle of the Dark Star(book 1)
2. The Oceans Between Stars: Chronicle of the Dark Star(book 2)
3. The Shores Beyond Time: Chronicle of the Dark Star(book 3)
4. Fahrenheit 451
5. Last Kids on Earth""")
                print(continueForward)
                if continueForward == 'yes':
                    endofConversation()
            elif genre2 == 'c':
                print("""I love realistic fiction books!! Here is a list of books I recommend reading . . .

1. Restart
2. Diary of a Wimpy Kid(series)
3. Wonder
4. Tales of a Fourth Grade Nothing
5. Otherwise Known as Sheila the Great
6. Superfudge
7. Double Fudge
8. The Benefits of Being an Octopus
9. Ban This Novel""")
                print(continueForward)
                if continueForward == 'yes':
                    endofConversation()
            elif genre2 == 'd':
                print("""I love suspense/thriller books!! Here is a list of books I recommend reading . . .
1. One of us is Lying
2. When
3. How to Lead a Life of Crime
4. Seizure
5. Two can Keep a Secret""")
                print(continueForward)
                if continueForward == 'yes':
                    endofConversation()
            elif genre2 == 'e':
                print("""I love historical fiction books!! Here is a list of books I recommend reading . . .

1. Allies
2. Grenade
3. Prisoner B-3087
4. Code of Honor
5. Refugee""")
                print(continueForward)
                if continueForward == 'yes':
                    endofConversation()
            else:
                print("""I love mystery books!! Here is a list of books I recommend reading . . .

1. A Study in Scarlet(Sherlock Holmes Book 1)
2. When
3. The Cuckoo’s Calling(book 1 in series)
4. The Silkworm(book 2 in series)
5. Career of Evil(book 3 in series)
6. Lethal White(book 4 in series)
7. Trouble Blood(book 5 in series, coming out in September 2020ish)""")
                print(continueForward)
                if continueForward == 'yes':
                    endofConversation()
    elif favMost == 'b':
        mathTopic = input("""I love math too!!! What topics in math are you interested in learning? 
        NOTE: I personally recommend learning competition math.

a. RECOMMENDED: Competition Math
b. Pre-Algebra
c. Algebra 1
d. High School Geometry
e. Algebra 2
f. Pre-Calculus
g. Calculus AB
h. Calculus BC
i. Multivariable Calculus
j. AP Statistics
Type your answer here: """)
        if mathTopic == 'a':
            print("""NOTE: You need an account for AOPS.
            link: https://artofproblemsolving.com

Learn any topics you want on AOPS Alcumus.
 https://artofproblemsolving.com/alcumus

Do any competition math problems on AOPS MATHCOUNTS TRAINER.
https://artofproblemsolving.com/mathcounts_trainer

Go to AOPS MATHCOUNTS MINIS to see how to so solve some math problems.
https://artofproblemsolving.com/videos

Try to do some real AMC 8 math contests that have been released on AOPS.
https://artofproblemsolving.com/wiki/index.php/AMC_8_Problems_and_Solutions

Try to do some real AMC 10 math contests that have been released on AOPS.
https://artofproblemsolving.com/wiki/index.php/AMC_10_Problems_and_Solutions

Try to do some real AMC 12 math contests that have been released on AOPS.
https://artofproblemsolving.com/wiki/index.php/AMC_12_Problems_and_Solutions
""")
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        elif mathTopic == 'b':
            print("""I love that you are interested in Pre-Algebra!!! Here is a link to a Pre-Algebra site to learn more!
NOTE: You need accounts for AOPS and Khan Academy websites.

Here is the link to access the websites: 

Khan Academy
https://www.khanacademy.org/math/pre-algebra

AOPS Alcumus
https://artofproblemsolving.com/alcumus""")
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        elif mathTopic == 'c':
            print("""I love that you are interested in Algebra 1!!! Here is a link to an Algebra 1 site to learn more!
NOTE: You need accounts for AOPS and Khan Academy websites.

Here is the link to access the websites: 

Khan Academy
https://www.khanacademy.org/math/algebra

AOPS Alcumus
https://artofproblemsolving.com/alcumus""")
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        elif mathTopic == 'd':
            print("""I love that you are interested in Geometry!!! Here is a link to a Geometry site to learn more!
NOTE: You need accounts for AOPS and Khan Academy websites.

Here is the link to access the websites: 

Khan Academy
https://www.khanacademy.org/math/geometry

AOPS Alcumus
https://artofproblemsolving.com/alcumus""")
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        elif mathTopic == 'e':
            print("""I love that you are interested in Algebra 2!!! Here is a link to an Algebra 2 site to learn more!
NOTE: You need accounts for AOPS and Khan Academy websites.

Here is the link to access the websites: 

Khan Academy
https://www.khanacademy.org/math/algebra2

AOPS Alcumus
https://artofproblemsolving.com/alcumus""")
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        elif mathTopic == 'f':
            print("""I love that you are interested in Pre-Calculus!!! Here is a link to a Pre-Calculus site to learn more!
NOTE: You need accounts for AOPS and Khan Academy websites.

Here is the link to access the websites: 

Khan Academy
https://www.khanacademy.org/math/precalculus

AOPS Alcumus
https://artofproblemsolving.com/alcumus""")
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        elif mathTopic == 'g':
            print("""I love that you are interested in Calculus AB!!! Here is a link to a Calculus AB site to learn more!
NOTE: You need accounts for AOPS and Khan Academy websites.

Here is the link to access the websites: 

Khan Academy
https://www.khanacademy.org/math/ap-calculus-ab

AOPS Alcumus
https://artofproblemsolving.com/alcumus""")
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        elif mathTopic == 'h':
            print("""I love that you are interested in Calculus BC!!! Here is a link to a Calculus BC site to learn more!
NOTE: You need accounts for AOPS and Khan Academy websites.
Here is the link to access the websites: 

Khan Academy
https://www.khanacademy.org/math/ap-calculus-bc

AOPS Alcumus
https://artofproblemsolving.com/alcumus""")
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        elif mathTopic == 'i':
            print("""I love that you are interested in Multivariable Calculus!!! Here is a link to a Multivariable Calculus site to learn more!
NOTE: You need accounts for AOPS and Khan Academy websites.
Here is the link to access the websites: 

Khan Academy
https://www.khanacademy.org/math/multivariable-calculus

AOPS Alcumus
https://artofproblemsolving.com/alcumus""")
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
        else:
            print("""I love that you are interested in AP Statistics!!! Here is a link to an AP Statistics site to learn more!
NOTE: You need accounts for AOPS and Khan Academy websites.
Here is the link to access the websites: 

Khan Academy
https://www.khanacademy.org/math/ap-statistics

AOPS Alcumus
https://artofproblemsolving.com/alcumus""")
            print(continueForward)
            if continueForward == 'yes':
                endofConversation()
    elif favMost == 'c':
        print("""I love science too! Especially the experiments!!! Here are ideas to do experiments at home.
        
Link:
https://mommypoppins.com/kids/50-easy-science-experiments-for-kids-fun-educational-activities-using-household-stuff""")
        print(continueForward)
        if continueForward == 'yes':
            endofConversation()
    elif favMost == 'd':
        print("""I really love history too!!! It is my favorite thing to learn about in my free time!!!

I really admire and learn a lot from this youtuber, Mr. Beat. You heard it right Mr. Beat, NOT MrBeast(unlike MrBeast, Mr. Beat's actual name is Matt Beat).

Check at his youtube channel here:

Link:
https://www.youtube.com/channel/UCmYesELO6axBrCuSpf7S9DQ

Go to EDX and also learn/attend different courses to learn about history.

Here is the link:
https://www.edx.org/learn/history""")
        print(continueForward)
        if continueForward == 'yes':
            endofConversation()
    else:
        print("""I also love writing!!! In fact, every year I participate in national writing month, 
        where we have to make a novel in those 30 days!

The link to the website is:
https://nanowrimo.org

If you are not an adult, the challenge for kids is:
https://ywp.nanowrimo.org


If you are interested in writing contests, go to a website that gives a compilation of various writing contests available online.

Here is the link:
https://www.fanstory.com/contestsall.jsp?sc=1&wct=1&gclid=CjwKCAjwmrn5BRB2EiwAZgL9os5sd_gnJbiXkNWo-D00tP37t3INBgbQr_ltKSB6t-HokVn08zE7MhoCJgsQAvD_BwE

If you are interested in writing in non-fiction, try and write a book summary for a book you read recently or really like.

If you are interested in writing about recent events or something you want to learn about, 
try and research about your desired topic. As you’re researching, read an article deeply. 
If the article seems of good value to your writing, 
then reread the article again, but this time slowly going through it and taking notes as you progress.
""")
        print(continueForward)
        if continueForward == 'yes':
            endofConversation()
