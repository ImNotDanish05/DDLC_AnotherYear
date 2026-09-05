# Chapter 5: Streetlights and the Long Walk Home
# Finale and Epilogue for "Another Year, Another Page"

label ch5_main:
    $ chapter = 5

    # --- SCENE 1: The Porch Goodbyes — 07:00 PM ---
    stop music fadeout 2.0
    scene bg entry_night
    with dissolve_scene_full

    play music t9

    "We stood gathered at my front door and genkan, saying our final goodbyes under the warm porch light."
    "Inside, my living room was wonderfully messy."
    "Streamers hung from the shelves, empty cider cups were by the sink, and half the cake was stored in Tupperware."

    show natsuki 1bd at t31
    show yuri 1ba at t32
    show monika 1ba at t33

    "Natsuki adjusted her tote bag with an exaggerated, feisty huff."
    n "Alright, birthday boy. I packed four giant slices of cake into those containers in your fridge."
    n "If you leave them on the counter to get stale, I will personally revoke your right to eat sugar forever."

    mc "I put them on the top shelf, Natsuki, I swear!"
    mc "And seriously... thank you. That was the best cake I\'ve ever tasted in my life."

    show natsuki 1bv at t31
    "Natsuki quickly looked away to hide her blushing, pleased grin."
    n "Hmph. Obviously."
    n "Just don't stay up until three in the morning coding with those loud Discord dorks."
    show natsuki 1ba at t31
    n "Happy twenty-first, again."

    hide natsuki with wipeleft
    "She spun on her heel, marching down my front walkway with a satisfied bounce in her step."

    show yuri 1bb at t21
    show monika 1ba at t22

    "Yuri stood beside the railing, her long dark coat pulled close around her cream knit sweater."
    "She gave me a gentle, respectful bow, her violet eyes warm and serene."
    y "Thank you for sharing your home with us, Danish. It was truly a delightful evening."

    mc "Thank you for coming, Yuri. And thank you for the tea, and for the 1884 book."
    mc "It's on my desk right now. I'm going to read a chapter before bed."

    show yuri 1be at t21
    "Her eyes lit up with a quiet, radiant joy."
    y "Please take your time with it."
    y "When the world demands you race against its machinery, allow yourself to breathe."

    hide yuri with wipeleft
    "Yuri offered a delicate wave before heading down the walkway to join Natsuki."

    show monika 1be at t11
    "Monika stepped forward, pulling on a light autumn jacket over her white tank top."
    "Her poised, radiant smile softened into something deeply fond."
    m "We called a cab to the corner of the avenue, so we'll be heading out together."

    show monika 1bb at t11
    "She rested a hand gently on my shoulder, looking right into my eyes."
    m "Danish... thank you for being the heart of this club."
    m "Don't let your internship boss or the job market intimidate you."
    m "You're doing better than you know. Trust me."

    mc "Thanks, Monika. That means a lot. Text me when you all get home safe."

    show monika 1ba at t11
    m "Will do."

    show sayori 1ba at t21
    show monika 1bb at t22
    m "Take care of him, Sayori. Don't let him sneak back into his bedroom to check pull requests tonight."

    show sayori 1bq at t21
    "Sayori saluted enthusiastically with her right hand."
    s "Aye-aye, Captain! I will tackle him onto the carpet if he touches a keyboard!"

    show monika 1ba at t22
    "Monika laughed, giving us both a warm wave as she walked down the driveway."
    hide monika with wipeleft

    show sayori 1ba at t11
    "The sound of their footsteps and fading laughter drifted away into the cool evening."
    "Soon, the street fell into that deep, peaceful stillness that only quiet neighborhoods have after dark."

    "Beside me on the porch step, Sayori let out a long, contented sigh."
    s "Haaaaah... that was the best party ever."

    mc "It really was."
    "I looked down at her. Her breath formed little puffs of white vapor in the chill air."
    mc "Hey... want to walk down to the corner streetlight before we head in? Just for fresh air?"

    show sayori 1bc at h11
    s "Yes! Night walk! Let's go!"

    # --- SCENE 2: The Residential Road — 07:15 PM ---
    stop music fadeout 2.0
    scene bg street_night
    with wipeleft_scene

    play music t8

    "We walked side by side down the familiar asphalt at an easy, unhurried pace."
    "My phone in my jacket pocket gave two quick, gentle vibrations."

    play sound audio.phone
    pause 0.2
    play sound audio.phone

    "I pulled it out with one hand."
    "The screen showed two notifications."

    "{b}[[Discord - The Boys (KUVART Project)]{/b}\n\"Danish, we're off the call. Enjoy your night bro. Rest up. Architecture docs on Saturday.\""

    "I quickly typed back with one thumb: 'Thanks guys. Build is clean. Catch you Saturday.'"

    "{b}[[Company Mail - Internship Supervisor]{/b}\n\"Saw PR merged and webhook tests passing. Excellent turnaround. Let's discuss Semester 8 contract Friday.\""

    "For the first time in twelve months, seeing my boss's name didn't send ice down my spine."
    "The contract was still there. The job market was still intimidating."
    "College, graduation, and the choice between corporate work, a Magister, or KUVART were still waiting."
    "But looking at the screen, I realized something simple:"
    "I am capable."
    "I survived a whole year of this already. I was learning, building, and moving forward."
    "I clicked the screen off and slipped my phone deep into my pocket."

    show sayori 1ba at t11
    s "All good?"

    mc "All good. Just the boys. And my boss."

    show sayori 1bd at t11
    "She puffed her cheeks out, instantly ready for battle."
    s "Did your boss yell at you?!"

    mc "Nope. He said good job."

    show sayori 1bq at t11
    "A soft, triumphant smile broke across her face."
    s "Hmph. He better!"

    show sayori 1ba at t11
    "A gentle gust of wind shook the maple trees, sending amber leaves fluttering down around us."
    s "Hey, Danish?"

    mc "Yeah?"

    s "Do you remember when you turned seven?"

    mc "Of course I do."
    mc "You tried to bake me a cake in your backyard using dirt, rainwater, and crushed flower petals."
    mc "And then you cried because a stray cat knocked it over."

    show sayori 1bc at t11
    s "I was very emotionally invested in that dirt cake!"
    show sayori 1ba at t11
    s "And when you turned twelve, you got your first desktop computer."
    s "You locked yourself in your room for three days installing an OS from a scratched CD."

    mc "Hey, getting Linux to boot on a ten-year-old PC with 512MB RAM was a milestone!"

    s "And when you turned sixteen, we sat on my front porch eating supermarket ice cream..."
    s "Talking about how weird high school was gonna be."

    # --- SCENE 3: The Light Beneath the Lamp — 07:30 PM ---
    scene bg park_path_night
    with dissolve_scene_full

    "She stopped walking."
    "We had reached the tall streetlamp on the crest of the hill."
    "The lamp hummed softly overhead, casting a wide circle of amber light on the pavement."
    "Below us, the distant lights of the town twinkled like a sea of fallen stars."

    show sayori 1bh at t11
    "Sayori kept her head tilted downward, hands clutched in front of her denim shorts."
    "The playful energy that carried her all afternoon softened into tender stillness."

    mc "Sayori? What's on your mind?"

    "She didn't answer right away."
    "When she lifted her head, her sky-blue eyes were glassy with unshed tears."
    "She wasn't smiling her goofy smile. She was just looking at me with heartbreaking sincerity."

    show sayori 1bj at t11
    s "I was just thinking..."
    s "...about how fast you're running."

    mc "How fast I'm running?"

    s "You're in semester five now. You work at a real company. You build secret software with your friends."
    s "You talk about webhooks and architectures and Magister degrees... big things I can barely pronounce."
    "She wrapped her arms around herself, holding her sleeves tight against the chill."
    s "And today... you turned twenty-one. A real adult."
    s "And I'm just... Sayori."
    s "I wake up late, I forget to tie my shoes, I burn toast..."
    s "And I have these stupid, heavy rainclouds inside my head that make some days impossible."

    show sayori 1bh at t11
    "A single tear escaped her lash, catching the amber streetlight as it traced down her cheek."
    s "Sometimes... I get so scared, Danish."
    s "I get scared that you're going to run so far ahead that you'll look back and think I'm holding you down."
    s "That my messiness and my sadness will just be another bug you have to fix."
    s "And I don't want to be a burden on you. I want you to fly."

    "My chest tightened until it physically ached."
    "I stepped forward and gently caught both of her cold hands in mine."
    "I wrapped my palms around hers, warming them with my own."

    mc "Sayori. Look at me."

    "She hesitated, then raised her tear-streaked eyes to mine."

    mc "Do you have any idea why I didn't lose my mind today?"
    "She sniffled quietly, shaking her head."

    mc "This morning at dawn, I was lying in bed feeling like my life was over."
    mc "Suffocating under emails, dreading the future, feeling like a failure before I even started."
    mc "And then I stepped out onto the street, and a girl with an untied sneaker tackled me at Mach 1 screaming happy birthday."

    show sayori 1bw at t11
    "A wet, choked laugh escaped her lips."

    mc "Sayori... all that tech stuff? The code, the internship, the deadlines? That's just work."
    mc "It's just lines on a screen."
    mc "You... you are the reason I remember to be human."

    "I squeezed her hands gently, brushing a stray tear from her cheek with my thumb."
    mc "You're not a bug I have to fix. You've never been a burden."
    mc "You're the person who knows who I am when all the titles and achievements are stripped away."
    mc "When the world tries to turn me into an output machine, you pull me back into the sunlight."

    mc "You don't have to keep up with me, Sayori. Because I'm not running away from you."
    mc "We're walking this road together. Just like when we were seven with that dirt cake."
    mc "Just like at twelve, and sixteen, and right now at twenty-one."
    mc "No matter how big the future gets... you're my home. You got that?"

    show sayori 1bj at t11
    "Sayori stared at me, her lower lip trembling."
    "Then, she buried her face directly into my chest, wrapping her arms around me in a fierce embrace."

    "I wrapped my arms around her shoulders, resting my chin lightly against the crown of her head."
    "The cool wind blew around the warm circle of our embrace."
    "She cried softly into my jacket for a moment—the quiet release of a heavy knot she had carried for weeks."

    s "I... I wrote you something."

    mc "A poem?"

    show sayori 1ba at t11
    "She pulled back an inch, wiping her eyes with the cuff of her pink sleeve."
    "She reached deep into her pocket and pulled out a small piece of paper folded into fourths."
    s "Don't laugh! I'm not as poetic as Yuri or Monika. It's just... what was in my head."

    # --- SCENE 4: The Poem on the Pavement — 07:45 PM ---
    stop music fadeout 2.0
    play music t10

    play sound audio.page_turn
    "Under the warm hum of the amber lamp, I carefully unfolded the paper."

    call screen sayori_poem_screen

    play sound audio.page_turn
    "I stood there on the quiet hilltop street, staring down at that little doodle of the smiling sun."
    "The simplicity of it was devastating."
    "It cut straight through every layer of overthinking, every corporate dread, every phantom fear."

    mc "Sayori..."
    "I carefully folded the paper along its creases and tucked it into my inner coat pocket, right over my heart."
    mc "It's perfect. Truly."

    show sayori 1bc at h11
    s "Ehehe... I told you I was wise!"

    mc "You're the wisest person I know."
    "I offered her my elbow with a grin."
    mc "Come on. Let's get you home before your mom thinks you ran away with the club."

    show sayori 1ba at t11
    "She looped her arm through mine, leaning her shoulder warmly against my side as we walked."

    # --- SCENE 5: The Threshold & The Next Page — 08:00 PM ---
    scene bg house_night
    with wipeleft_scene

    "We reached the foot of our driveways."
    "Across the narrow road, Sayori's front porch light cast a welcoming yellow rectangle on the pavement."

    mc "Here. Take this Tupperware of Natsuki's cake for you and your family for breakfast tomorrow."

    show sayori 1bc at h11
    s "Yay! Cake for breakfast!"
    "She hugged the container happily to her chest."

    show sayori 1bw at t11
    "She turned on the bottom step, looking up at me with bright, clear eyes under the amber porch light."
    s "Goodnight, Danish. And... happy twenty-first birthday. For real this time."

    mc "Goodnight, Sayori. Tie your shoe before you walk across the street."

    show sayori 1bq at t11
    s "I won't! It's my signature style now!"
    "She stuck her tongue out playfully, then jogged across the asphalt to her front door."
    "She gave me one last energetic wave with both arms, then slipped inside."

    hide sayori with wipeleft
    play sound audio.door_close
    "Her front door clicked shut. Her porch light stayed on, glowing warmly in the dark."

    scene bg bedroom_night
    with dissolve_scene_full

    "I stepped into my own house, locked the door, and walked upstairs into my bedroom."
    "The room was quiet, bathed in the soft, pale blue standby glow of my dual monitors."
    "Twelve hours ago, this room had felt like a suffocating cockpit in a crashing plane."
    "Now, it just felt like home. A place where I lived, studied, and tinkered."

    "I reached into my bag and took out Yuri's dark green 1884 novel, setting it reverently beside my keyboard."
    "I took Sayori's poem from my coat pocket and slid it under the edge of my primary monitor."
    "The little smiling sun peeked out right beneath the screen."

    play sound audio.phone
    "My phone gave one last gentle buzz on the desk."

    "{b}[[Discord - The Boys (KUVART Project)]{/b}\n\"Get some sleep, birthday boy. Big things ahead.\""

    "I smiled, setting the phone face down."

    scene bg sky_night_moon
    with dissolve_scene_full

    "I walked over to the window, pushed the curtains aside, and looked up into the deep indigo sky."
    "The stars were sharp, cold, and ancient—unmoved by how fast the earth turned beneath them."
    "The future was still coming."
    "Tomorrow morning, my boss would want an update. The job market would still be uncertain."
    "New frameworks would be announced, and the world would keep spinning at its terrifying pace."
    "But as I leaned against the cool glass of the window, there was no panic left in my chest."
    "I am twenty-one today."
    "I have code to write. I have a project to build. And I have people who love me."
    "I smiled softly into the dark glass, meeting my own reflection."
    mc "Happy twenty-first, Danish."
    mc "Now let's see what the next page looks like."

    stop music fadeout 3.0
    scene black
    with dissolve_scene_full

    pause 3.0

    "{b}Another Year, Another Page{/b}\n\n{i}Dedicated to growing older without drifting apart.{/i}"

    pause 2.0

    "{b}Created by ImNotDanish05{/b}\n\nBased on Doki Doki Literature Club by Team Salvato."

    pause 2.0

    "{b}THE END{/b}"

    return
