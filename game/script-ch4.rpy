# Chapter 4: The 21st Milestone & The Secret Project
# Script for "Another Year, Another Page"

label ch4_main:
    $ chapter = 4

    # --- SCENE 1: The Evening Walk & The Crossroads — 05:00 PM ---
    stop music fadeout 2.0
    scene bg street_night
    with dissolve_scene_full

    play music t9

    "The autumn air hit my face the moment I stepped past the school gates."
    "It was crisp and biting enough to clear the fog that had lingered in my head all day."
    "I took a long, slow breath."
    "My breath curled into a faint wisp of white in the chill."
    "Five o'clock."
    "The quiet hum of the neighborhood was settling in around me."
    "Distant train whistles echoed in the distance, followed by the hum of cars along the main avenue."
    "Dry maple leaves scraped softly across the curbs in the evening breeze."
    "I looked down at my worn sneakers as they hit the asphalt with an even rhythm."
    "Man... what a day."
    "Twelve hours ago, waking up at dawn had felt like staring down an executioner's block."
    "Twenty-one."
    "The big milestone that was supposed to magically turn me into a bulletproof adult."
    "Someone who knew exactly how to navigate inflation, hiring algorithms, and corporate career ladders."
    "Instead, I had spent the morning nursing a tension headache and dreading my boss's Slack pings."
    "A soft chuckle escaped my lips."
    "And then came the club."
    "First, bumping into Sayori at the intersection—her silly, boundless energy bulldozing through my gloom."
    "Then Natsuki in the clubroom, furiously trying to hide flour on her sleeves with that custom cake."
    "And Yuri... sitting with me in the quiet corner, pouring lavender tea and handing me an 1884 novel."
    "Reminding me that human feelings don't have an expiration date."
    "I reached back and patted my backpack."
    "The hard rectangular edge of Yuri's green book was tucked safely inside, resting against my laptop."
    "I'm really glad I joined this club."
    "If I hadn't let Sayori drag me through that door back in the spring, where would I be right now?"
    "Probably hunched over three monitors in my bedroom, eating cold onigiri and staring at API docs."
    "Wondering why my twenties felt so lonely."
    "Instead, for the first time in months, my chest actually felt light."
    "I crossed the small bridge over the canal, watching the amber lamppost lights reflect in the water."
    "So... what now?"
    "Semester five is more than halfway done. Next year is senior year. Then what?"
    "Do I go straight into full-time corporate software engineering?"
    "My internship boss already dropped hints this morning about locking me down through semester eight."
    "The paycheck would be steady, but the thought of forty years of daily standups makes my stomach twist."
    "What about graduate school? A Master's degree... a Magister in Computer Science?"
    "I frowned, kicking a stray pebble across the pavement."
    "Magister sounds fancy on LinkedIn, sure."
    "But do I actually want two more years of academic papers and thesis defense?"
    "Or am I just looking for an excuse to delay real life?"
    "And then there's KUVART."
    "A secret platform built from scratch with three of my closest college friends."
    "No corporate oversight. No venture capital suits breathing down our necks."
    "Just pure code, clean architecture, and the crazy dream of building something people actually love."
    "If KUVART takes off... do I dare bet on ourselves?"
    "I smiled faintly, turning onto my street."
    "Twenty-one. You're supposed to have answers, Danish."
    "But maybe having good questions is enough for tonight."

    scene bg house_night
    with wipeleft_scene

    "A light breeze rustled the maple trees along the sidewalk as my house came into view."
    "I reached into my pocket, feeling for my keys."
    "Then I stopped dead in my tracks."
    "Wait."
    "The warm yellow living room curtains were drawn shut, but behind the fabric, lights were flickering."
    "And from the driveway... was that music?"
    "I blinked, taking a cautious step closer."
    "A muffled squeak echoed from inside, followed by a sharp, hushed hiss:"
    "'Shh! Turn that down, you idiot! He's gonna hear it from the street!'"
    "My heart jumped straight into my throat."
    "Did someone break into my house?!"

    # --- SCENE 2: The Infiltration & The Spare Key Mystery — 05:25 PM ---
    scene bg entry_night
    with wipeleft_scene

    "I held my breath, resting one hand against the doorframe."
    "Slowly, gently, I inserted my key into the brass deadbolt and turned it."

    play sound audio.door_open

    scene black
    with wipeleft_scene

    mc "Hello...? Mom? Dad...?"
    "The foyer was pitch black."
    "I slipped my shoes off at the genkan, my heart pounding against my ribs."
    "I took two quiet, cautious steps toward the living room entrance."
    mc "I swear, if this is a burglar with terrible music taste, I have an umbrella and I'm not afraid to—"

    stop music fadeout 0.5
    play sound audio.surprise

    scene bg danish_livingroom_surprise
    with hpunch

    "POP! POP-POP-POP!"
    "A loud explosion of colorful paper confetti rained down on my head."
    "Cardboard party blowers shrieked in unison right in front of my face."

    play music never_be_alone

    s "SURPRIIIIIIIISE!"

    "I jumped three feet in the air, nearly tripping backward into the umbrella stand."
    mc "WHOA! WHAT THE—!"
    "Standing together in the center of my living room with broad, triumphant grins were all four of them."
    "Natsuki held a glowing, two-tiered birthday cake right in front, blushing with a proud smile."
    "Sayori was leaning in with pure joy, while Monika and Yuri smiled warmly around them."
    "I froze."
    "My mouth fell open. My backpack slid off my shoulder, landing with a soft thud on the floor."
    mc "You... you guys?!"

    s "HAPPY BIRTHDAY, DANISH!"

    scene bg danish_livingroom
    with dissolve_scene_half

    show sayori 1ba at t41
    show natsuki 1ba at t42
    show yuri 1ba at t43
    show monika 1ba at t44

    mc "Hold on! Wait! Time out!"
    mc "How did you... what are you doing in my house?! How did you even GET IN?!"

    show sayori 1bq at t41
    "Sayori puffed her chest out with immense pride, twirling a shiny brass key around her finger."
    s "Ehehehe! The Master of Infiltration strikes again!"

    "I stared at the key. The small green plastic tag attached to the ring looked terrifyingly familiar."
    mc "Wait... is that my spare house key?!"

    show sayori 1ba at t41
    s "Bingo!"
    s "Remember two semesters ago during finals week?"
    s "You locked yourself out at two in the morning because you were half-asleep from cramming..."
    s "And you gave me the emergency spare so you wouldn't have to climb through the bathroom window again!"

    mc "That was eight months ago! I thought I lost that key in my dresser!"

    show sayori 1bq at t41
    s "Nope! Safe and sound on my frog keychain!"
    s "And today, it served the greatest purpose of its mechanical life!"

    mc "You used my emergency lockout key to commit coordinated breaking and entering?!"

    show monika 1bb at t44
    m "It's not breaking and entering if you invited us into your life, Danish."
    show monika 1bc at t44
    m "Though legally speaking, Sayori did threaten to climb through your laundry room window."

    show sayori 1bl at h41
    s "I did not! I only said the window was very accessible!"

    show sayori 1ba at t41
    mc "And WHEN did you even coordinate this?!"
    mc "Natsuki, you were baking with me at school until four!"
    mc "Yuri, we were literally sitting by the window drinking barley tea thirty minutes ago!"
    mc "How did you beat me to my own house?!"

    show natsuki 1bd at t42
    n "A master baker never reveals her logistical supply chain, birthday boy."
    n "Let's just say while you were taking your dramatic, emo walk home, Monika had a cab waiting."

    show yuri 1bb at t43
    y "I... I assisted with transporting the decorations."
    y "We took the express avenue. Monika drove with great... efficiency."

    show monika 1bc at t44
    m "Don't expose my driving habits, Yuri."
    show monika 1ba at t44
    m "The point is, the Literature Club leaves no member behind on their twenty-first milestone."
    m "Especially our resident tech wizard."

    # --- SCENE 3: The Blushing Quad & The Unfiltered Truth — 05:35 PM ---
    "I stood in the center of the room, looking around in utter disbelief."
    "Streamers were taped across the ceiling, and balloons floated near the bookshelves."

    show banner_zoom zorder 3 at truecenter with dissolve
    "Draped across the back wall was a handmade garland banner that proudly spelled out 'HAPPY 21ST DANISH'."
    "Flanked by pastel stars, balloons, and streamers, it transformed my living room into a real celebration."
    hide banner_zoom with dissolve

    "And then my gaze drifted from the decorations... to the four of them."
    "My brain suddenly stuttered to a halt."
    "They weren't in their school blazers."
    "They weren't wearing the stiff brown uniforms, cream vests, or dark skirts I saw every afternoon."
    "They were in their real, everyday, casual outfits."
    "Sayori was in a coral-pink shirt over a white top, sleeves rolled up, with blue denim shorts."
    "Natsuki wore a fitted white top with a cute cat print, a ruffled pink skirt, and twin pigtails."
    "Yuri wore a cozy beige cable-knit turtleneck with cold-shoulder cutouts and black leggings."
    "And Monika wore a crisp white sleeveless tank top, a gold necklace, and form-fitting dark jeans."
    "Under the warm living room lights, the contrast was staggering."
    "I stood there, staring like an idiot."
    "The silence stretched for three seconds. Four."

    show natsuki 1bd at t42
    n "What? What are you staring at? Do I have frosting on my nose again?!"

    mc "No."
    "The word left my mouth before my brain's internal firewall could stop it."
    mc "You guys look... really, really pretty."

    "Dead silence dropped over the living room like an anvil."
    "Sayori froze. Natsuki's jaw dropped. Yuri's eyes widened. Even Monika was caught off-guard."

    show natsuki 1bl at h42
    n "H-Haaaaah?! What did you just say, you absolute moron?!"

    mc "I mean it."
    "Maybe it was turning twenty-one, or the relief of being home, but the words tumbled out with total sincerity."
    mc "Sayori, you look so bright. The pink shirt and the rolled sleeves... it's just so you."
    mc "You look like pure sunshine walked right through my front door."

    show sayori 1bv at t41
    "Sayori let out a tiny, high-pitched squeak, her face flushing the exact shade of a ripe strawberry."
    s "E-Ehehe... D-Danish, stop it! Sunshine?! That's... that's too much...!"

    mc "And Natsuki, that outfit is ridiculously stylish. The ruffles, the cat print, the skirt..."
    mc "You put so much care into putting that together. You look incredible."

    show natsuki 1bv at h42
    n "D-D-DUMMY!"
    n "Who authorized you to analyze my clothes like a fashion critic?!"
    n "Shut up right now or I'm throwing a paper plate at your head!"
    "Her hands self-consciously smoothed the pleats of her skirt, hiding a suppressed smile."

    mc "Yuri... that knit sweater with the cut-out shoulders. The way your hair rests against it..."
    mc "You look like an author on a book jacket. It's so elegant and graceful."

    show yuri 1bd at t43
    "A deep, radiant pink flooded Yuri's porcelain cheeks."
    "She let out a mortified gasp and pulled both oversized sweater sleeves over her face, trembling."
    y "I... I... merciful heavens, Danish... please... my heart cannot endure this..."

    mc "And Monika... that white tank top, the necklace, and your high ponytail."
    mc "You always look put-together at school, but like this? You look stunning. Athletic, effortless, and radiant."

    show monika 1bd at t44
    "Monika froze. A soft, rosy flush crept up her neck and dusted her cheekbones."
    "She raised one hand to her throat, letting out an awkward, breathless chuckle as she looked away."
    m "Danish... goodness."
    show monika 1bc at t44
    m "Where did all this confidence come from? You're turning twenty-one, not running for office."

    mc "I'm just speaking the truth."
    mc "I'm used to seeing you guys across classroom desks in school blazers."
    mc "Seeing you here... in my home, like this... it just hit me how lucky I am."

    "The four of them stood in a half-circle, all four faces varying shades of pink."
    show monika 1ba at t44
    m "Well... flattery aside, we didn't break into your house just to model for you."

    # --- SCENE 4: The Masterpiece Cake & The 21 Candles — 05:50 PM ---
    show natsuki 1be at t11
    n "A-Alright! Enough standing around getting all sentimental! Step aside!"
    "Natsuki rushed toward the coffee table with a large, square white bakery box tied in crimson ribbon."
    "With dramatic flair, she untied the satin bow and lifted the lid."
    "A collective 'Oooooh' filled the living room."
    "Sitting on an embossed gold foil platter was a two-tiered triumph of pastry engineering."
    "The exterior was draped in glossy, dark chocolate ganache, smooth as obsidian."
    "Cascading down the upper tier was a thick, buttery salted caramel drip and rolled chocolate truffles."
    "Standing proudly at the very top were two large, metallic-gold number candles: '2' and '1'."

    mc "Holy crap, Natsuki... you made this?! From scratch?!"

    show natsuki 1bd at t11
    n "Of course I made it from scratch!"
    n "You think I'd buy some generic supermarket sponge cake for your twenty-first?!"
    n "I caramelized the sugar at five in the morning! I tempered the ganache three times!"

    show sayori 1ba at t21
    show natsuki 1bd at t22
    s "She almost burnt her kitchen curtains down!"

    show natsuki 1bl at h22
    n "SAYORI, I WILL REVOKE YOUR SLICE!"

    show yuri 1ba at t11
    y "It truly is magnificent, Natsuki. The symmetry of the tiers is flawless."

    show monika 1ba at t11
    m "Alright, everyone. Let's dim the room lights."

    "Sayori sprang to the wall switch and clicked the chandelier off."
    "The living room fell into soft twilight, lit only by amber streetlights through the windows."
    "Monika struck a long wooden match. A sulfur flare hissed in the dark."
    "She touched the flame to the twin wicks, and two bright, golden teardrops of fire bloomed."
    "The flickering light danced against the chocolate, reflecting in five pairs of eyes."

    show sayori 1ba at t41
    show natsuki 1ba at t42
    show yuri 1ba at t43
    show monika 1ba at t44

    s "Gather round! Three, two, one—"
    "And right there, in my living room at quarter to six, the four of them sang."
    "Sayori sang at top volume, off-pitch and full of unbridled joy."
    "Natsuki sang with a self-conscious mumble, rolling her eyes but hitting the harmony anyway."
    "Yuri sang in a delicate, angelic vibrato, and Monika led them with steady, resonant warmth."
    "'...Happy birthday dear Daaa-niiish... Happy birthday to you!'"

    show sayori 1bc at h41
    s "WOOOOOO! Make a wish! Blow them out!"

    scene cake_candle_on
    with dissolve_scene_half

    "I looked down at the flickering twin flames."
    "Twenty-one."
    "An hour ago, that number had felt like an insurmountable wall."
    "Now, looking at the warm reflections dancing across the chocolate... the future didn't feel scary anymore."
    "'Just let me keep making things that matter,' I wished silently."
    "'Let me protect this warmth. And don't let me lose the people who make this life good.'"
    "I took a deep breath, leaned in, and blew."

    stop music fadeout 1.5
    "Fwoosh."

    scene black
    with dissolve_scene_half
    pause 1.0

    scene cake_candle_off
    with dissolve_scene_half

    "A slender curl of white smoke drifted upward, carrying the sweet scent of caramel and burnt sugar."
    "The room erupted into cheers and clapping as Sayori flicked the lights back on."

    # --- SCENE 5: The Discord Storm & KUVART Exposed — 06:10 PM ---
    scene bg danish_livingroom
    with dissolve_scene_half

    show sayori 1ba at t41
    show natsuki 1ba at t42
    show yuri 1ba at t43
    show monika 1ba at t44

    "Paper plates of rich chocolate caramel cake and cups of cider were spread across the table."
    "I sat cross-legged on the floor, happily devouring a massive slice."

    play sound audio.phone
    pause 0.2
    play sound audio.phone
    pause 0.2

    "BZZ-BZZ-BZZ-BZZ-BZZ!"
    "My phone didn't just vibrate—it rattled against the coffee table like an out-of-control blender."
    "The screen lit up with a blinding barrage of Discord alerts:"

    "{b}[[Discord - The Boys (KUVART Project) - GROUP CALL INCOMING]{/b}\n\"DANISH ANSWER THE DAMN PHONE\""
    "{b}[[Discord - The Boys (KUVART Project)]{/b}\n\"PR #142 MERGED! KUVART ALPHA IS LIVE AND COMPILING!\""
    "{b}[[Discord - The Boys (KUVART Project)]{/b}\n\"DON'T DIE OF OVERTIME OR CHEAP BEER! POST CAKE PICS!\""

    mc "Ack—wait—!"
    "My hand slipped on a stray drop of caramel as I lunged for it."
    "Before I could recover, Sayori's hand snatched the phone out of the air like an Olympic goalie."

    show sayori 1bm at t41
    s "Ohohoho! It's calling! It's making funny noises!"

    mc "Sayori, no! Don't press that! They're gonna—"

    play sound audio.phone
    "BEEP."
    "Speakerphone filled the living room instantly."
    "A barrage of loud, overlapping guy voices blared through the tiny smartphone speaker:"
    "'—YO DANISH! ARE YOU ALIVE?! DID THE BACKEND CRASH—'"
    "'—Tell me you're not still debugging that webhook, bro, it's literally your birthday!—'"
    "'—Happy twenty-one, man! KUVART build 0.4.1 just passed regression testing! We're ordering pizza!—'"
    "'—Wait, why is it so quiet? Danish, who are you with? Did corporate HR kidnap you—'"

    show sayori 1bc at h41
    s "HE'S AT HIS HOUSE WITH THE LITERATURE CLUB!"

    "Dead silence fell over the call."
    "Two whole seconds of pure, unadulterated shock."
    "Then, an absolute panic meltdown from the boys:"
    "'—WAIT WHAT—'"
    "'—Is that a GIRL?!—'"
    "'—BRO, HE HAS WOMEN OVER AT HIS HOUSE?!—'"
    "'—DUDE, DANISH HAS A SOCIAL LIFE?! SINCE WHEN?!—'"
    "'—ABORT CALL! ABORT CALL! DON'T EMBARRASS HIM!—'"

    play sound audio.phone
    "CLICK. Call ended."

    "Silence returned to the living room."
    "I buried my face in both hands, groaning so hard my ribs ached."
    mc "I am going to delete their GitHub accounts. Every single one of them. Revoked."

    show natsuki 1bl at t42
    "Natsuki collapsed sideways onto the couch, clutching her stomach with tears in her eyes."
    n "AHAHAHAHA! 'Abort call! Don't embarrass him!' Oh my god! Who ARE those absolute nerds?!"

    mc "They are absolute nerds. They're my software buddies from university."

    show monika 1ba at t44
    m "Well, they sound like very loyal friends, Danish. Even if their phone etiquette could use polish."
    show monika 1bb at t44
    m "So... 'KUVART.' That's the name of this secret project of yours, isn't it?"

    mc "Yeah. It's called KUVART."
    mc "We've been building an independent software platform from scratch for the past few months."
    mc "We kept it secret because we didn't want outside hype until the core engine actually worked."
    mc "And... I didn't want you guys to think I was ignoring literature for more computer stuff."

    show yuri 1ba at t43
    y "Danish... why would we ever be annoyed that you are pursuing something you are passionate about?"

    show natsuki 1ba at t42
    n "Yeah, idiot! If you're building something cool with your friends, you should be proud of it!"
    n "Just... stop skipping sleep for it. Even super-coders need to rest."

    show sayori 1ba at t41
    s "And if you ever need beta testers, I'm first in line!"
    s "I don't know what a 'PR' is, but I can click things until the screen turns purple!"

    mc "That's called chaos engineering, Sayori. And honestly, you'd be terrifyingly good at it."

    # --- SCENE 6: Monika's Truth & The Warmth of Home — 06:30 PM ---
    play music t10

    show monika 1bb at t11
    m "Alright, everyone. Before we help Danish clean up, there's one last tradition we need to observe."

    show sayori 1ba at t21
    show monika 1bb at t22
    s "Ooh! Monika's poem!"

    show monika 1be at t11
    "Monika picked up my acoustic guitar resting on its stand in the corner."
    "She strummed a soft, cascading four-chord progression that hung gently in the quiet room."
    m "In the Literature Club, we share our hearts through words."
    m "When Danish first walked through our clubroom door, he carried a heavy backpack."
    m "He was quiet, guarded, and often looked like he was trying to solve ten impossible equations at once."

    "She strummed another gentle chord, resolving into something warm and bright."
    m "Today, Danish, you turned twenty-one."
    m "I know how heavy that number feels. I know how much pressure you've been carrying with your internship."
    m "Carrying production deadlines while sitting in lectures, fearing that you're falling behind."
    "My throat tightened. Leave it to Monika to see straight through every defense I had."

    show monika 1bb at t11
    m "The world out there is loud, Danish. It tells you that you are only worth what you produce."
    m "It tells you that if you can't run as fast as an AI pipeline, you are obsolete. But that's a lie."
    m "An algorithm can write syntax, but it cannot feel the ache of a poem."
    m "An algorithm can automate a deployment, but it cannot wake at five to bake a cake for a friend."
    m "It cannot brew lavender tea to quiet an anxious mind."
    m "And it cannot keep a spare key for eight months just to fill your living room with laughter."

    "Sayori sniffled quietly beside me, wiping a tear from her cheek."
    "Natsuki looked away toward the kitchen, blinking back moisture."
    "Yuri rested both hands over her heart, her violet eyes shining."

    show monika 1be at t11
    m "Your worth has never been your output, Danish."
    m "Your worth is the kindness you bring into our lives. The way you listen when we need to be heard."
    m "Twenty-one isn't a cliff where you have to prove yourself to the universe."
    m "It's just the next page in the book."
    m "And no matter how fast the world runs... this club, and this home, will always be your place to breathe."

    "Silence filled the living room—sweet, heavy, and profound."
    "I looked at the four of them sitting in my living room."
    "At Natsuki, whose chocolate masterpiece sat on my table."
    "At Yuri, whose annotated 1884 book was tucked in my room."
    "At Sayori, whose goofy smile and spare key had broken through my isolation."
    "And at Monika, who had given me the one thing no corporate ladder could offer: absolute belonging."

    mc "Thank you."
    "My voice was thick, but it was the truest thing I had ever spoken."
    mc "All of you. Seriously. This... this is the best birthday I've ever had in my life."

    show sayori 1bc at h11
    s "Awwwww! GROUP HUG!"

    "Sayori launched herself off the carpet and wrapped both arms around my neck."
    "Within two seconds, Natsuki was dragged in too, grumbling while burying her face against my shoulder."
    "Yuri stepped in with gentle grace, wrapping her long sleeves around us."
    "And Monika joined from the side, laughing as the five of us stood tangled together under the warm light."
    "The future was still out there."
    "Tomorrow, my boss would still want his code. The tech market would still be chaotic."
    "Grad school and KUVART would still be waiting."
    "But tonight, standing in my home surrounded by the people who loved me..."
    "Twenty-one didn't feel scary anymore."
    "It felt like the start of something beautiful."

    stop music fadeout 2.0
    scene black
    with dissolve_scene_full

    pause 2.0

    "{b}End of Chapter 4{/b}\n\nTo be continued in Chapter 5..."

    return
