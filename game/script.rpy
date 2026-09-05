# Script entry point for "Another Year, Another Page"

label start:
    $ anticheat = persistent.anticheat
    $ chapter = 1
    $ _dismiss_pause = config.developer

    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    $ player = "Danish"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True

    call ch1_main
    call ch2_main
    call ch3_main
    call ch4_main
    call ch5_main
    return
