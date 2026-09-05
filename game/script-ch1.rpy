# CHAPTER 1: THE QUIET MORNING
# Story & Mod by Danish & Pair Programmer

label ch1_main:
    # --- SCENE 1: Danish's Bedroom — 06:45 AM ---
    stop music fadeout 1.0
    scene bg bedroom
    with dissolve_scene_full

    "The alarm didn't wake me up."

    play sound audio.phone
    "The phantom vibration of my phone on the nightstand did."
    "That sickening, Pavlovian hum."
    "It meant someone, somewhere, had opened a ticket or tagged @here before the sun was even fully over the horizon."

    "I stared at the ceiling for a solid thirty seconds, listening to the hum of my PC fans."

    "Today is my birthday."
    "Twenty-one."

    "When you're ten, turning twenty-one sounds like you'll be driving a sports car, wearing a sharp coat, and casually knowing how mortgages work."
    "When you actually hit twenty-one, you just wake up with a stiff neck and dry eyes..."
    "...and the lingering dread that you forgot to commit a branch before passing out at 3:45 AM."

    "I rolled over and swiped the lock screen."
    "The notification feed lit up my face like a flashbang."

    "{b}[[Slack - 06:12 AM]{/b}\nBoss: \"Morning Danish. Saw the PR you pushed last night. Good stuff, but we need to refactor the webhook handler before the 10 AM standup.\""

    "{b}[[Slack - 06:13 AM]{/b}\nBoss: \"Also, let's talk about locking in your contract through Semester 8 later today.\""

    "{b}[[Discord - The Boys (KUVART Project) - 02:18 AM]{/b}\n\"Yo, did you push the new build? Keep it on the private repo, don't let anyone leak the repo link yet.\""

    "{b}[[GitHub - 04:00 AM]{/b}\n[[Automated]: Build failed on master: 1 error, 4 warnings."

    "{b}[[YouTube Support - 05:30 AM]{/b}\n\"Your second channel has been suspended for violating our Community Guidelines...\""

    mc "\"Are you serious?\" I muttered aloud to the empty room."
    mc "\"My {i}second{/i} account? I literally only uploaded private screen recordings of plugin tests and a backup playlist of lofi beats.\""
    mc "\"What guideline did I violate, existing too hard?\""

    "I rubbed the bridge of my nose, tossing the phone back onto the mattress."

    "Semester five. One full year at this internship already."
    "My boss was already dangling that Semester 8 contract over my head like a carrot on a fishing rod—a mix of flattering trust and suffocating commitment."
    "Between college lectures, twenty hours a week of backend code, and trying to keep up with the tech world that reinvents itself every two weeks..."
    "...plus hacking together custom Minecraft plugins just to remember why I liked programming in the first place..."
    "My brain felt like a browser with forty tabs open and audio playing from somewhere I couldn't find."

    "{i}Twenty-one.{/i}"

    mc "\"Happy birthday to me,\" I whispered, dragging myself out of bed."
    mc "\"Now go fix the build before you get fired.\""

    # --- SCENE 2: The Residential Street — 07:35 AM ---
    scene bg house
    with wipeleft_scene

    "I barely managed a bowl of lukewarm cereal before slipping on my jacket, tossing my laptop into my bag, and stepping outside."

    scene bg residential_day
    with wipeleft_scene

    "The morning air hit my face like a cold splash of water, shocking the grogginess out of my system."
    "I hadn't even made it twenty yards down the street when a familiar, chaotic commotion echoed from behind me."

    play sound "sfx/run.ogg"
    s "DANNNNIIIISHHHHH!"

    play music t2
    "Footsteps came slapping against the asphalt at dangerous speeds."
    "I barely had time to turn around before a blur of peach hair and a loose school blazer practically collided into my backpack."

    mc "Woah—careful!"

    "I braced my feet, catching her by the shoulders before she wiped out on the concrete."

    mc "Sayori, do you ever leave your house at a speed below Mach 1?"

    show sayori 1l zorder 2 at t11
    s 1l "Haaaah... haaaah... I saw you... walking past my window..."
    s "And I didn't even... tie my left shoe..."

    "She bent over, hands on her knees, panting like she'd just sprinted an Olympic mile."

    mc "I can tell."

    "I glanced down. Her left sneaker was indeed completely untied, the laces dragging through autumn leaves."

    mc "You're gonna break your neck one of these days."

    show sayori 2c zorder 2 at h11
    s 2c "Worth it!"

    "She straightened up with a triumphant bounce, puffed out her chest, and spread her arms wide."

    show sayori 2r zorder 2 at t11
    s 2r "HAPPY TWENTY-FIRST BIRTHDAAAAAY!"

    "A couple of middle schoolers walking on the other side of the street turned to stare."
    "I instinctively shrank into my collar, feeling heat rise up my neck."

    mc "Keep it down, the whole prefecture doesn't need to know my age."

    show sayori 1q zorder 2 at t11
    s 1q "Nope! Everyone needs to know!"

    "Sayori marched alongside me, her steps full of that bouncy, uncoordinated energy she’d had since we were six years old."

    show sayori 1a zorder 2 at t11
    s 1a "Twenty-one! You're officially an old man now!"
    s "How does it feel? Do your bones ache? Do you suddenly have the urge to complain about property taxes?"

    mc "My back already aches from sitting in an office chair debugging Java code until four in the morning, so yeah, basically."

    show sayori 1t zorder 2 at s11
    s 1t "Danish! You stayed up late again?!"

    mc "It wasn't my fault."
    mc "The event listener was canceling player interactions every time someone opened a custom chest inventory."
    mc "If I didn't patch the plugin, the whole server economy would have tanked."

    show sayori 1b zorder 2 at t11
    s 1b "You and your Minecraft servers."

    "Sayori rolled her eyes, but there was an affectionate warmth behind it."

    s "You code for school, you code for your job, and then you relax by... coding for blocks."
    s "Sometimes I think your brain is made of silicon chips."

    mc "Hey, the block game pays for my sanity."
    mc "Or at least it did, until YouTube decided to ban my second channel this morning."

    show sayori 1m zorder 2 at h11
    s 1m "Wait, really?! The one with your secret testing stuff?!"

    mc "Yup. Completely wiped."
    mc "No strike, no warning, just 'Your account has been terminated.'"
    mc "I don't even have the energy to fight the automated appeal form."
    mc "Dealing with Google's bot system is like trying to talk to a brick wall that gives you generic error codes."

    show sayori 1h zorder 2 at t11
    "Sayori frowned, bumping her shoulder gently against mine."

    s 1h "That really sucks, Danish. YouTube bots are meanies."
    s "If I could reach into the computer and smack the bot with a rolled-up newspaper, I totally would."

    mc "Thanks, Sayori. I'm sure YouTube's automated compliance algorithms would be terrified of you."

    # --- SCENE 3: The Path by the Hillside — 07:45 AM ---
    stop music fadeout 2.0
    scene bg residential_day
    with wipeleft_scene

    "For a little while, we walked in comfortable silence."
    "That was always the thing with Sayori—she could be the loudest, most energetic person in the room, but she was also the only person who never made quiet moments feel awkward."

    show sayori 1a zorder 2 at t11
    "Still, she kept sneaking sidelong glances at me."

    mc "What? Do I have toothpaste on my cheek?"

    show sayori 1h zorder 2 at t11
    s 1h "No... You just look... quiet."

    mc "I'm always quiet in the morning."

    s "Not this kind of quiet. You have your 'thinking-too-much' face on."
    s "The one where your eyebrows pinch together and you look like you're carrying a whole server rack on your shoulders."

    "I let out a breath I hadn't realized I was holding."
    "The air came out in a thin wisp of steam in the cool morning air."

    play music t8 fadein 2.0
    mc "It's just... the birthday thing, Sayori."
    mc "Twenty-one feels weird. It feels like someone hit the fast-forward button and snapped the remote control in half."

    "Sayori didn't interrupt. She just tilted her head, listening with her whole attention."

    mc "In school, everything had steps, y'know?"
    mc "You finish grade nine, you go to grade ten. You graduate, you go to university."
    mc "But now? I'm in semester five."
    mc "My internship boss told me this morning he wants to lock me down through semester eight."
    mc "That means I'm basically working full-time hours while juggling coursework for the next year and a half."
    mc "And knowing how brutal the job market is right now... part of me feels like I should be grateful."
    mc "But another part of me is just terrified."

    show sayori 1j zorder 2 at t11
    s 1j "Terrified of what?"

    mc "Of getting stuck. Of never being good enough."
    mc "The tech world is completely unhinged right now, Sayori."
    mc "I swear, it moves faster than anyone can breathe."
    mc "Last year everyone was hyped about n8n and workflow automations."
    mc "Then boom—OpenClaw drops, and suddenly everyone calls the old stuff useless."
    mc "Then in under a single year, Hermes comes out of nowhere and everyone's scrambling again."
    mc "Every time I spend weeks mastering a tool or building a framework..."
    mc "...some new AI drops on Twitter and makes half of what I learned obsolete overnight."
    mc "How am I supposed to build a career when the ground under my feet won't stop shaking?"

    "I stopped, realizing how worked up I’d gotten over something that probably sounded like foreign gibberish to her."

    mc "Sorry... I'm just rambling. It's stupid."

    show sayori 3c zorder 2 at h11
    s 3c "It's not stupid!"

    "Sayori grabbed my sleeve, stopping me on the path."
    "Her blue eyes were wide, earnest, and completely devoid of judgment."

    show sayori 3a zorder 2 at t11
    s "Danish, listen to me."

    "Her voice dropped that silly sing-song tone and turned into the quiet, fierce friend who had pulled me out of my shell a hundred times before."

    s "You've been working at that internship for a whole year already. A whole year!"
    s "While taking classes! Do you know how amazing that is?"
    s "My biggest achievement this week was remembering to put matching socks on two days in a row."

    mc "Sayori, that's not—"

    s "I'm serious!"

    "She squeezed my arm."

    s "You're always looking ten steps ahead, worrying about what's gonna break next."
    s "But look at where you are right now."
    s "You're twenty-one today. You're smart, you build cool things, you make everyone around you feel safe..."
    s "...and you don't have to solve your whole entire future before the sun goes down."

    "I looked at her."
    "Beneath that bright, determined smile, I could see the familiar, faint shadow in her eyes—the quiet, personal battles she fought every day with her own mind."
    "The 'rainclouds' she rarely talked about, always putting everyone else's happiness ahead of her own."
    "Yet here she was, standing on a sidewalk at 7:50 AM, using every ounce of her warmth to hold up my sky."

    "A lump formed in my throat. I cleared it quickly, giving her a soft smile."

    mc "When did you get so wise?"

    show sayori 2q zorder 2 at h11
    s 2q "Ehehe~ I've always been wise!"

    "She instantly bounced back, letting go of my sleeve and striking a proud, goofy superhero pose."

    s "I just keep it hidden so Monika doesn't make me write philosophical essays for the club."

    # --- SCENE 4: Approaching the School Gates & Lockers — 08:05 AM ---
    stop music fadeout 2.0
    scene bg corridor
    with wipeleft_scene

    "As we neared the entrance, my phone buzzed in my pocket again."

    play sound audio.phone
    "I pulled it out half an inch. A Discord notification popped up:"

    "{b}[[The Boys - KUVART]{/b}\n\"Danish, make sure you don't mention KUVART's core concept to anyone today. We're locking down the alpha build this weekend.\""

    "I tapped my pocket to silence it, quickly sliding it back in."

    play music t3
    show sayori 1o zorder 2 at t11
    "Sayori’s eyes instantly narrowed. A sly, detective-like grin spread across her face."

    s 1o "Ooooh... who was that?"

    "She purred, leaning into my personal space."

    s "Checking your phone all sneaky-like."
    s "Is someone texting you birthday wishes? A secret girl from your lectures?"

    mc "No. It's just the guys from my side project."

    show sayori 1u zorder 2 at t11
    s 1u "The secret project you never tell anyone about? You've been disappearing to work on that for weeks!"
    s "If you're secretly building an AI robot to replace the Literature Club, I'm going to unplug it."

    mc "It's not a robot to replace anyone."
    mc "It's called KUVART, and the guys want to keep the details quiet until it's actually ready."
    mc "It's purely guy-talk and code architecture, alright? Nothing juicy."

    show sayori 1a zorder 2 at t11
    s 1a "Hmm... I'll let you off the hook for now. Only because it's your birthday."

    "She paused by the shoe lockers, turning back to face me with a look that was suddenly very deliberate."

    s "By the way, Danish... you're coming to the club room right after classes today, right?"
    s "No running off to do internship overtime?"

    mc "I have to submit that refactor to my boss, but yeah, I'll be there."
    mc "Why? Did Monika plan something?"

    show sayori 1v zorder 2 at t11
    "Sayori’s eyes darted upward for half a second in classic, terrible-at-lying Sayori fashion."

    s 1v "Ehehe... nope! Totally normal club meeting!"
    s "Just poems, and reading, and... regular literature stuff! Yup! Nothing special at all!"

    mc "Sayori, you are the worst liar in human history."

    show sayori 1q zorder 2 at h11
    s 1q "I don't know what you're talking about! See you after school! Don't be late!"

    show sayori zorder 1 at thide
    hide sayori

    play sound "sfx/run.ogg"
    "She spun around on her heel, her untied shoelace flopping wildly as she practically sprinted down the hallway toward her homeroom."

    mc "Tie your shoe!"

    "I called after her, shaking my head."

    stop music fadeout 2.0

    "I stood by my locker, feeling the cool metal under my fingertips."
    "For the first time all morning, the heavy knot in my chest had loosened just a bit."

    "{i}Twenty-one.{/i}"

    "Maybe the future was a terrifying, runaway train."
    "Maybe tech was moving too fast to ever truly master, and maybe the job market was going to be a bloodbath."
    "But as I closed my locker door, I realized one thing:"
    "At least for today, I wasn't walking the tracks alone."

    scene black
    with dissolve_scene_full
    pause 2.0

    "{b}End of Chapter 1{/b}"

    return
