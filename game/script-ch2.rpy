# CHAPTER 2: FLOUR, CODE, AND BURNT SUGAR
# Story & Mod by Danish & Pair Programmer

label ch2_main:
    # --- SCENE 1: The Clubroom Hallway — 03:15 PM ---
    stop music fadeout 1.5
    scene bg corridor
    with wipeleft_scene

    "Classes ended twenty minutes ago."
    "Normally, this was the part of the day where my brain officially shut down and slipped into low-power mode."
    "Today, though, my backpack felt like it was packed with lead bricks."

    "Inside was my laptop, holding three urgent Slack threads from my boss..."
    "...two open Jira tickets with alarming red exclamation marks..."
    "...and a half-written Python script to parse webhook payloads."

    "I just needed a quiet corner with an outlet."
    "Somewhere with a functioning desk where I could plug in, push this hotfix to GitHub, and breathe for ten straight minutes."

    "The Literature Club room was always dead empty before 3:45 PM."
    "Sayori was usually running around helping teachers, Yuri rarely arrived before the kettle was ready..."
    "...and Monika always had student council obligations to wrap up first."

    "I grabbed the brass door handle, twisted it, and pushed the door open."

    play sound audio.door_open
    pause 0.4

    "\"Hah! Got you, you little—\""
    "{i}\"WAIT, NO, DON'T SLAM—!\"{/i}"

    play sound audio.fall
    with vpunch

    "{i}CLATTER!{/i}"
    "A metallic tray rattled violently against a wooden desk."
    "A cloud of fine white dust poofed into the air like a smoke grenade."

    scene bg club_day
    with dissolve_scene_half

    "I froze in the doorway, hand still on the knob."

    show natsuki 1e zorder 2 at t11
    "Standing in the center of the classroom was Natsuki."
    "Her pigtails were slightly askew."
    "Her face was smudged with a streak of flour right across her left cheekbone."
    "In her hands was an aluminum baking tray, which she was clutching to her chest like a riot shield."
    "Her magenta eyes were wide with pure, unadulterated terror."

    "We stared at each other for three excruciating seconds."

    play music t5

    show natsuki 1n at s11
    n "\"...Danish?\""

    mc "\"Natsuki?\""
    mc "\"Did... did a bag of flour explode in here, or are you trying to summon a pastry demon?\""
    mc "\"And wait... did you seriously bake in your school uniform without an apron?\""
    mc "\"You've got white flour all over your sleeves!\""

    show natsuki 1m at h11
    with hpunch
    n "\"WHAT ARE YOU DOING HERE SO EARLY?!\""

    "She slammed the tray onto the nearest desk and frantically brushed at her sleeves."

    show natsuki 2f at t11
    n "\"I didn't have time to grab an apron from the home ec room, okay?!\""
    show natsuki 4t at t11
    n "\"Club doesn't start for another half hour! You're not supposed to be here!\""
    show natsuki 4r at t11
    n "\"Turn around! Walk out! Wipe your memory!\""

    mc "\"I have a key! Well, Monika gave me a spare copy last month.\""
    mc "\"And why are you baking in the clubroom? I thought the domestic science room had the ovens?\""

    show natsuki 4c at h11
    n "\"They {i}do{/i} have the ovens, genius!\""

    show natsuki 4f at t11
    n "\"I baked them downstairs during my free study period!\""
    show natsuki 4r at t11
    n "\"I just... brought them up here to cool down and do the frosting where people wouldn't steal them!\""
    show natsuki 4t at t11
    n "\"Not that it's any of your business!\""

    "She lunged sideways, throwing a checkered kitchen towel over whatever was on the tray with the speed of an Olympic goalie."

    show natsuki 1p at h11
    n "\"Don't look at it!\""

    mc "\"I'm not looking, I'm not looking.\""
    mc "\"I just came to plug my laptop in and fix a crash before my boss calls my cell.\""

    show natsuki 1h at t11
    n "\"Your boss?\""

    "Her glare softened just a fraction, replaced by that sharp, perceptive squint of hers."

    show natsuki 1o at t11
    n "\"Wait... you're doing your stupid internship work {i}right now{/i}? On a school desk?\""

    # --- SCENE 2: The Two Desks — 03:25 PM ---
    stop music fadeout 1.5
    scene bg club_day
    with dissolve_scene_half

    play music t3

    "I pulled out a chair near the window, unzipped my bag, and ran the power cord to the wall outlet."

    show natsuki 1a zorder 2 at t11 with dissolve
    "Natsuki hopped onto the edge of the adjacent desk, folding her arms as she watched my screen."

    mc "\"Yeah. My boss wants this webhook fix merged before our late afternoon sync.\""
    mc "\"If the payload times out, the client's API rejects the whole transaction.\""

    "Natsuki leaned forward slightly, squinting at the cascades of green, orange, and white text scrolling across my dark mode editor."

    show natsuki 1f at t11
    n "\"Ugh. Just looking at that gives me a migraine.\""
    show natsuki 1h at t11
    n "\"It's just a wall of brackets, dots, and words that don't make sense. How do you even know what you're doing?\""

    mc "\"Half the time? I don't.\""
    mc "\"Programming is basically 10 percent knowing what you're doing...\""
    mc "\"...and 90 percent staring at a stack trace wondering why the thing that worked yesterday decided to catch fire today.\""

    show natsuki 1d at t11
    n "\"Sounds miserable.\""

    "She didn't walk away, though."
    "She stayed perched on the edge of the desk, idly swinging her legs back and forth."

    mc "\"It's not miserable when it's your own project.\""
    mc "\"Like... when I'm at home messing with Minecraft plugins, or working on that side thing with my friends, it's actually fun.\""
    mc "\"You build something from scratch, you watch it run, and it feels like magic.\""
    mc "\"But corporate stuff? Jira tickets, sprint retros, bosses pinging you at 6 AM on your birthday...\""

    "I clamped my mouth shut."
    "{i}Nice one, Danish. Smooth.{/i}"

    "Natsuki's swinging legs froze instantly."

    show natsuki 1e at h11
    n "\"Wait.\""

    "She turned her head so fast her ribbon bounced."
    "Her eyes locked onto mine like laser-guided missiles."

    show natsuki 1o at t11
    n "\"What did you just say?\""

    mc "\"Uh... nothing. I said... 'bosses pinging you at 6 AM about their paychecks.' Very boring adult stuff.\""

    show natsuki 2t at h11
    n "\"Don't play dumb with me, Danish!\""

    "Natsuki slid off the desk, planted her fists on her hips, and leaned right into my face."
    "The faint scent of vanilla extract and powdered sugar drifted off her."

    show natsuki 2m at t11
    n "\"You said 'on your birthday.' Is today your birthday?!\""

    "I shrank back into my chair, feeling the tips of my ears burning."

    mc "\"I mean... technically, yeah. But it's not a big deal. Really. You don't have to make it a thing.\""

    show natsuki 1e at h11
    n "\"Not a big deal?!\""
    show natsuki 1w at t11
    n "\"Are you out of your mind?! Sayori didn't tell me! Monika didn't—\""
    show natsuki 1o at t11
    n "\"Wait, actually, Monika might have known. She's weirdly omniscient about everyone's records...\""

    "She trailed off, muttering under her breath before snapping right back to me."

    show natsuki 1t at t11
    n "\"How old are you even turning?!\""

    mc "\"Twenty-one.\""

    show natsuki 1e at s11
    "Natsuki stared at me like I had just grown a second head."

    n "\"Twenty-one.\""
    show natsuki 2f at t11
    n "\"You're twenty-one today... and you're sitting in an empty classroom, in uniform, fixing some soulless tech company's broken computer garbage?\""

    mc "\"It's not garbage, it's—\""

    show natsuki 2m at h11
    with hpunch
    n "\"It is garbage!\""

    show natsuki 4m at t11
    n "\"Danish! You've been working that internship for, what, a whole year now?! Ever since third semester!\""
    show natsuki 4c at t11
    n "\"Every single week you come to the club looking like a walking corpse who subsists entirely on convenience store iced coffee!\""
    show natsuki 4t at t11
    n "\"And now it's your actual twenty-first birthday and you're still typing away for some guy who probably doesn't even know what your face looks like?!\""

    "The sheer aggression in her voice caught me completely off guard."
    "Yet looking at her, beneath the sharp brows and flushed cheeks, there wasn't cruelty in her eyes."
    "It was frustration."
    "The raw, unfiltered frustration of someone who hated watching someone she cared about get ground down."

    mc "\"Natsuki... it's... it's not that simple.\""

    show natsuki 1h at t11
    n "\"Why isn't it?\""
    show natsuki 1u at s11
    n "\"You don't even look happy. You look like you're bracing for an earthquake.\""

    # --- SCENE 3: The Metaphor of Burnt Sugar — 03:35 PM ---
    stop music fadeout 2.0
    scene bg club_sunset
    with dissolve_scene_full

    "I stared down at the blinking cursor on my terminal."
    "The afternoon sunlight was deepening into warm honey-gold, slanting long shadows across the wooden floorboards."
    "The classroom went completely still, save for the faint hum of my laptop fan."

    mc "\"Because I'm scared.\""

    "The words came out quieter than I intended, but in the silence of the room, they landed heavy."

    show natsuki 1e zorder 2 at t11 with dissolve
    "Natsuki blinked, caught off guard by the blunt honesty."
    "She shifted her weight, uncrossing her arms."

    show natsuki 1u at t11
    n "\"Scared of what?\""

    play music t8

    mc "\"Of what happens when college ends.\""
    mc "\"Everyone tells you getting an internship early is the dream. 'Oh, you got in at semester three? You're set!'\""
    mc "\"But my boss told me this morning he expects me to renew all the way through semester eight.\""
    mc "\"That's another year and a half of this grind.\""
    mc "\"And if I quit? If I say I need to focus on school or personal sanity?\""
    mc "\"Then I graduate into the worst tech job market in a decade with a burned bridge.\""

    "I ran a hand through my messy hair, letting out a ragged sigh."

    mc "\"And tech doesn't wait for anyone, Natsuki.\""
    mc "\"It's moving so ridiculously fast right now it makes me nauseous.\""
    mc "\"You spend months learning a framework like n8n, then some crazy tool like OpenClaw drops and everyone says your skills are useless.\""
    mc "\"Then Hermes comes out in less than a year and the cycle restarts.\""
    mc "\"Everything is automated. Everything is moving at warp speed.\""
    mc "\"I feel like if I take one afternoon off—just one day to breathe—I'll wake up tomorrow and be completely obsolete.\""

    "I stopped, bracing myself for a sarcastic quip or a lecture about being dramatic."

    show natsuki 1v at t11
    "Instead, Natsuki just stood there, looking at me with a steady, unreadable gaze."

    show natsuki zorder 1 at thide
    hide natsuki
    "Then, she turned around, walked over to the desk with the covered tray, and lifted the kitchen towel."

    n "\"Hey.\""
    n "\"Move your laptop.\""

    mc "\"What?\""

    n "\"I said move your stupid laptop. Push it over.\""

    "I hesitated, then slid the machine toward the far edge of the desk."

    show natsuki 1b zorder 2 at t11 with dissolve
    "Natsuki carried over a small porcelain plate."
    "On it sat a square, impeccably crafted pastry."
    "It wasn't one of her usual pastel-pink cupcakes with kitty faces."
    "This one was structured like a miniature, pixelated cube—"
    "—brown cocoa sponge on the bottom, a perfectly leveled layer of rich white vanilla buttercream on top..."
    "...and tiny, hand-piped red fondant squares arranged neatly in a grid."

    "It looked exactly like a slice of cake straight out of Minecraft."

    show cake zorder 3 at truecenter with dissolve

    mc "\"Natsuki... is this...\""

    show natsuki 1r at h11
    n "\"Shut up.\""
    show natsuki 4r at t11
    n "\"It's not a big deal. Don't make that stupid face.\""

    "She set the plate down right in front of me with an aggressive clack."

    mc "\"Did you... make a Minecraft cake?\""

    show natsuki 2m at h11
    with hpunch
    n "\"I said shut up!\""

    "She aggressively pulled out the chair across from me, turned it backward, and sat down."
    "Her chin rested on her folded arms against the backrest."

    show natsuki 1h at t11
    n "\"Sayori mentioned last week that you were whining about your server plugins crashing.\""
    show natsuki 1i at t11
    n "\"And then you were rambling about pixel art textures or whatever.\""
    show natsuki 2q at t11
    n "\"I had extra cocoa powder, and the red fondant was leftover from a project last weekend. I didn't want it to go to waste.\""

    mc "\"You don't 'accidentally' pipe individual pixel-perfect fondant squares, Natsuki.\""
    mc "\"This must have taken you hours.\""

    show natsuki 4h at t11
    n "\"Are you going to eat it or are you going to sit there doing forensic analysis on it?!\""
    show natsuki 4t at t11
    n "\"Just... try it.\""
    show natsuki 4p at t11
    n "\"The ganache inside has real espresso in it so your brain doesn't completely rot while you stare at your dumb screens.\""

    "I picked up the little plastic fork she set down beside the plate."
    "I cut off a corner, catching the layers of sponge, coffee-infused cream, and rich cocoa, and took a bite."

    "The flavor hit instantly."
    "Deep, slightly bitter chocolate balanced by smooth, buttery sweetness..."
    "...with a subtle punch of roasted coffee that cut right through the sugar."
    "It was insanely good."

    hide cake with dissolve

    stop music fadeout 1.5

    mc "\"Holy crap.\""
    mc "\"Natsuki, this is ridiculous. This is better than the bakery by the station.\""

    play music t7

    show natsuki 4d at h11
    n "\"Of course it is!\""
    show natsuki 1d at t11
    n "\"Those bakery hacks use artificial coffee syrup and powdered egg whites.\""
    show natsuki 1b at t11
    n "\"Real baking is precision, Danish. You can't cheat the chemistry.\""

    "She paused, watching me take another bite, her smug grin softening into something thoughtful."

    show natsuki 1v at t11
    n "\"You know...\""
    show natsuki 1a at t11
    n "\"Baking is kind of like what you just said.\""

    mc "\"What do you mean?\""

    show natsuki 1v at t11
    n "\"People think baking is just following instructions on a box.\""
    show natsuki 1a at t11
    n "\"They think you just dump flour, sugar, and butter in a bowl and turn on heat. But it's not.\""
    show natsuki 1f at t11
    n "\"If the butter is two degrees too warm, your cookies spread out like greasy pancakes.\""
    show natsuki 1h at t11
    n "\"If you whip egg whites ten seconds too long, the whole meringue curdles.\""
    show natsuki 1t at t11
    n "\"If you crank the heat to finish faster, the outside burns while the inside stays raw goop.\""

    "She looked up at me, her sharp magenta eyes meeting mine with absolute clarity."

    show natsuki 1w at t11
    n "\"You're trying to crank the oven to 500 degrees, Danish.\""
    show natsuki 1u at t11
    n "\"You're trying to bake the whole cake in five minutes because you're scared someone else is gonna finish before you.\""

    "The room went dead quiet."
    "The hum of my laptop suddenly felt distant."

    show natsuki 1v at t11
    n "\"Your boss, the tech market, those stupid AI things you were just talking about...\""
    show natsuki 1a at t11
    n "\"They want you to run at maximum speed until you burn to a crisp.\""
    show natsuki 1u at t11
    n "\"But you can't rush things that actually take time to become good.\""
    show natsuki 1v at t11
    n "\"You've been working your butt off for a year. You're twenty-one today.\""
    show natsuki 1w at t11
    n "\"You're allowed to let the pastry cool down before you frost it, idiot.\""

    "A strange warmth settled into my chest, cutting right through the cold anxiety that had followed me since 6 AM."

    "I set the fork down and looked at her."

    mc "\"That was surprisingly profound, Natsuki. Who taught you that?\""

    show natsuki 4d at h11
    n "\"Nobody taught me, I'm just naturally a genius!\""
    show natsuki 1q at t11
    n "\"Unlike you, who needs a high school girl to remind him to eat a piece of cake on his own birthday.\""

    # --- SCENE 4: The Buzz on the Desk — 03:45 PM ---
    "Right on cue, my phone on the desk gave two short, violent buzzes."

    play sound audio.phone
    pause 0.2
    play sound audio.phone
    pause 0.4

    "{b}[[Discord - The Boys (KUVART Project)]{/b}\n\"Danish, check your DM. We just finalized the architecture doc.\""
    "{b}[[Discord - The Boys (KUVART Project)]{/b}\n\"Don't show this to anyone yet, it's gotta stay between the five of us until launch.\""

    "Before I could even reach for the screen, Natsuki's hand shot across the desk, tapping the wooden surface."

    show natsuki 2d at h11
    n "\"Aha! Another ping!\""
    show natsuki 1q at t11
    n "\"You've been checking that phone every five minutes. Who is it?\""
    show natsuki 1d at t11
    n "\"Some secret girlfriend from your university classes wishing you a happy birthday?\""

    mc "\"No! I told Sayori this morning, it's just the guys from my side project.\""

    "I snatched the phone and stuffed it directly into my pocket."

    show natsuki 1o at t11
    n "\"The mysterious project you won't tell anyone about?\""
    show natsuki 1h at t11
    n "\"You're always typing away on your laptop during club time, whispering about 'repos' and 'branches.'\""
    show natsuki 1f at t11
    n "\"What are you guys even building? Some super-secret video game?\""

    mc "\"It's called KUVART.\""
    mc "\"And we're keeping it quiet because the guys want the release to be a complete surprise.\""
    mc "\"No leaks, no hype before it's ready. If I blab about it, they'll revoke my GitHub access.\""

    show natsuki 4b at t11
    n "\"KUVART?\""
    show natsuki 4f at t11
    n "\"Sounds like an evil villain corporation from a sci-fi manga.\""

    mc "\"It's not evil! It's actually really cool.\""
    mc "\"And besides, if I spent all day talking about database schemas, you'd throw an eraser at my head.\""

    show natsuki 1d at h11
    n "\"Damn right I would.\""

    "She stood up from the chair, casually brushing off the front of her uniform with a huff."
    "The classroom was starting to fill with the faint, comforting sounds of other students in the hall."
    "The rest of the club would be arriving any minute."

    show natsuki 1a at t11
    "Natsuki glanced down at the plate."
    "The Minecraft cake was almost entirely gone, save for a few crumbs of dark cocoa sponge."

    show natsuki 1h at t11
    n "\"Well? Did it suck?\""

    "I stood up, closing my laptop screen with a satisfying snap."

    mc "\"It was the best thing I've had all week, Natsuki. Honestly. Thank you.\""

    show natsuki 1e at s11
    "She froze for half a second. Her shoulders tensed, then relaxed."
    "When she turned around, her face was composed into that familiar, stubborn pout..."
    "...but her cheeks were flushed a soft, warm pink."

    show natsuki 1r at t11
    n "\"Yeah, well... don't get used to it.\""
    show natsuki 4r at t11
    n "\"I only make custom orders for people once every twenty-one years.\""

    mc "\"Fair enough.\""

    "As she picked up the empty plate to rinse it in the sink down the hall, she paused by the door, glancing back over her shoulder."

    show natsuki 1w at t11
    n "\"Happy birthday, Danish.\""

    play sound audio.door_close
    show natsuki zorder 1 at thide
    hide natsuki

    "Before I could answer, she slipped out into the corridor..."
    "...leaving behind only the sweet, lingering scent of vanilla in the quiet afternoon air."

    stop music fadeout 2.0
    scene black
    with dissolve_scene_full

    pause 2.0

    "{b}End of Chapter 2{/b}\n\nTo be continued in Chapter 3..."

    return
