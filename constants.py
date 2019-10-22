"""Contains constants from the game."""

from collections import namedtuple
Wish = namedtuple("Wish", "id name levels divider")
WISH_ORDER = [
    Wish(1, "I wish that wishes kicked ass", 1, 1e15),
    Wish(62, "I wish I was more OP", 10, 8e19),
    Wish(29, "I wish I could dual wield weapons", 10, 5e16),
    Wish(46, "I wish I could dual wield weapons II", 10, 1e19),
    Wish(7, "I wish I was stronger in Adventure mode I", 10, 3e15),
    Wish(30, "I wish I was stronger in Adventure mode II", 10, 2e17),
    Wish(19, "I wish the Greasy Nerd took a shower", 10, 1e16),
    Wish(43, "I wish the Greasy Nerd took a shower II", 10, 7e17),
    Wish(64, "I wish the Greasy Nerd could at least wear some body spray", 10, 5e20),
    Wish(16, "I wish I had more Resource 3 Power I", 10, 5e15),
    Wish(38, "I wish I had more Resource 3 Power II", 10, 1e17),
    Wish(55, "I wish I had more Resource 3 Power III", 10, 5e18),
    Wish(71, "I wish I had more Resource 3 Power IV", 10, 3e20),
    Wish(17, "I wish I had more Resource 3 Cap I ", 10, 5e15),
    Wish(39, "I wish I had more Resource 3 Cap II", 10, 1e17),
    Wish(56, "I wish I had more Resource 3 Cap III", 10, 5e18),
    Wish(72, "I wish I had more Resource 3 Cap IV", 10, 3e20),
    Wish(77, "I wish the QP Hack had more milestones I", 5, 2e17),
    Wish(79, "I wish the HACK HACK had more milestones I", 10, 6e20),
    Wish(20, "I wish Active Quests were more Rewarding I", 10, 2e16),
    Wish(63, "I wish Active Quests were more Rewarding II", 10, 8e20),
    Wish(48, "I wish Quests gave more QP", 10, 3e18),
    Wish(42, "I wish the Titan after Godmother would also drop QP", 1, 3e20),
    Wish(41, "I wish the Godmother would drop QP", 1, 1e19),
    Wish(74, "I wish the Beast would drop some QP", 1, 2e16),
    Wish(75, "I wish the Greasy Nerd would drop some QP", 1, 5e17),
    Wish(47, "I wish enemies spawned faster", 10, 6e18),
    Wish(4, "I wish V2/3/4 Titans had better rewards", 3, 8e15),
    Wish(2, "I wish that wishes weren't so slow :c", 10, 1e15),
    Wish(22, "I wish Wishes weren't so slow :c II", 10, 5e16),
    Wish(44, "I wish Wishes weren't so slow :c III", 10, 2e18),
    Wish(3, "I wish MacGuffin drops mattered", 5, 2e15),

    Wish(10, "I wish I had more Energy Power I", 10, 5e15),
    Wish(32, "I wish I had more Energy Power II", 10, 1e17),
    Wish(49, "I wish I had more Energy Power III", 10, 5e18),
    Wish(65, "I wish I had more Energy Power IV", 10, 3e20),
    Wish(11, "I wish I had more Energy Cap I", 10, 5e15),
    Wish(33, "I wish I had more Energy Cap II", 10, 1e17),
    Wish(50, "I wish I had more Energy Cap III", 10, 5e18),
    Wish(66, "I wish I had more Energy Cap IV", 10, 3e20),
    Wish(13, "I wish I had more Magic Power I", 10, 5e15),
    Wish(35, "I wish I had more Magic Power II", 10, 1e17),
    Wish(52, "I wish I had more Magic Power III", 10, 5e18),
    Wish(68, "I wish I had more Magic Power IV", 10, 3e20),
    Wish(14, "I wish I had more Magic Cap I", 10, 5e15),
    Wish(36, "I wish I had more Magic Cap II", 10, 1e17),
    Wish(53, "I wish I had more Magic Cap III", 10, 5e18),
    Wish(69, "I wish I had more Magic Cap IV", 10, 3e20),

    Wish(5, "I wish money pit didn't suck", 10, 6e15),
    Wish(9, "I wish I had a cool new move for Adventure I", 1, 6e15),
    Wish(78, "I wish the Number Hack had more milestones I", 5, 1e19),
    Wish(6, " I wish I could beat up more bosses I", 10, 3e15),
    Wish(31, "I wish I could beat up more bosses II", 10, 2e17),

    Wish(28, "I wish the Daycare Kitty was even happier", 10, 5e16),
    Wish(26, "I wish Fruit of MacGuffin α wasn't so random", 1, 6e16),
    Wish(25, "I wish Blood MacGuffin α wasn't so random", 1, 6e16),
    Wish(61, "I wish Fruit of MacGuffin α also didn't suck", 10, 4e20),
    Wish(60, "I wish blood MacGuffin α also didn't suck", 10, 4e20),
    Wish(18, "I wish I had more Resource 3 Bars I", 10, 5e15),
    Wish(40, "I wish I had more Resource 3 Bars II", 10, 1e17),
    Wish(57, "I wish I had more Resource 3 Bars III", 10, 5e18),
    Wish(73, "I wish I had more Resource 3 Bars IV", 10, 3e20),
    Wish(12, "I wish I had more Energy Bars I", 10, 5e15),
    Wish(34, "I wish I had more Energy Bars II", 10, 1e17),
    Wish(51, "I wish I had more Energy Bars III", 10, 5e18),
    Wish(67, "I wish I had more Energy Bars IV", 10, 3e20),
    Wish(15, "I wish I had more Magic Bars I", 10, 5e15),
    Wish(37, "I wish I had more Magic Bars II", 10, 1e17),
    Wish(54, "I wish I had more Magic Bars III", 10, 5e18),
    Wish(70, "I wish I had more Magic Bars IV", 10, 3e20),
    Wish(24, "I wish Basic Training was EVEN FASTER >:)", 1, 1e17),

    Wish(8, "I wish I had more Inventory space I", 12, 3e15),
    Wish(21, "I wish I didn't have to wait 3 minutes per rebirth", 6, 3e16),
    Wish(23, "I wish I had more Inventory space II", 12, 8e16),
    Wish(27, "I wish I were an Oscar Meyer Weiner", 1, 1e18),
    Wish(45, "I wish there was more cute Daycare Kitty Art", 1, 3e19),
    Wish(58, "I wish I had more Inventory space III", 12, 8e19),
    Wish(59, "I wish I had another cool new move for adventure", 1, 3e21),
    Wish(76, "I wish I was a giant jar of Mayo.", 1, 5e21),

    # sad

    Wish(89, "I wish I had more Resource 3 Power V", 10, 5e+21),
    Wish(91, "I wish I had more Resource 3 Cap V", 10, 5e+21),
    Wish(98, "I wish I had more Resource 3 Power VI", 10, 1e+23),
    Wish(100, "I wish I had more Resource 3 Cap VI", 10, 1e+23),
    Wish(83, "I wish I had more Energy Power V", 10, 5e+21),
    Wish(85, "I wish I had more Energy Cap V", 10, 5e+21),
    Wish(92, "I wish I had more Energy Power VI", 10, 1e+23),
    Wish(94, "I wish I had more Energy Cap VI", 10, 1e+23),
    Wish(86, "I wish I had more Magic Power V", 10, 5e+21),
    Wish(88, "I wish I had more Magic Cap V", 10, 5e+21),
    Wish(95, "I wish I had more Magic Power VI", 10, 1e+23),
    Wish(97, "I wish I had more Magic Cap VI", 10, 1e+23),

    Wish(104, "I wish I was stronger in Adventure mode III", 10, 1e+19),
    Wish(105, "I wish I was stronger in Adventure mode IV", 10, 3e+21),
    Wish(80, "I wish I the ITOPOD had more Base PP awarded", 10, 2e+21),
    Wish(102, "I wish Major Quests had better Base QP Rewards.", 10, 1e+22),
    Wish(103, "I wish Minor Quests had better Base QP Rewards.", 2, 1.8e+23),
    Wish(101, "I wish Titan 10 dropped QP", 1, 5e+22),
    Wish(110, "I wish I had yet another Accessory Slot!", 1, 5e+24),

    Wish(81, "I wish higher level quest drops counted for even more Quest progress I", 2, 5e+17),
    Wish(82, "I wish higher level quest drops counted for even more Quest progress II", 2, 1e+22),

    Wish(106, "I wish I could beat up more bosses III", 10, 2e+19),
    Wish(107, "I wish I could beat up more bosses IV", 10, 1e+21),
    Wish(108, "I wish the Sadistic Boss Multiplier didn't suck so bad I", 10, 2e+22),
    Wish(109, "I wish the Sadistic Boss Multiplier didn't suck so bad II", 10, 5e+23),
    Wish(90, "I wish I had more Resource 3 Bars V", 10, 5e+21),
    Wish(99, "I wish I had more Resource 3 Bars VI", 10, 1e+23),
    Wish(84, "I wish I had more Energy Bars V", 10, 5e+21),
    Wish(87, "I wish I had more Magic Bars V", 10, 5e+21),
    Wish(93, "I wish I had more Energy Bars VI", 10, 1e+23),
    Wish(96, "I wish I had more Magic Bars VI", 10, 1e+23),
    ]

WISH_BLACKLIST = [8, 21, 23, 27, 45, 58, 59, 76]
WISH_DISCLAIMER = "Disclaimer: this class is experimental, expect issues and crashes. Please do report them on discord or open an issue on github if you encounter one. I recommend using the color 'green' as your R3 color in the settings, it yields the best OCR results in my testing."
TITAN_ZONE = [7, 9, 12, 15, 17, 20, 24, 27, 31, 35]
DEFAULT_DIGGER_ORDER = [12, 4, 9, 10, 11, 1, 2, 3, 5, 6, 7, 8]
QUEST_ZONE_MAP = {"sewers": 2, "forest": 3, "high security base": 6, "the 2d universe": 10,
                  "a very strange place": 13, "mega lands": 14, "the beardverse": 16,
                  "chocolate world": 21, "the evilverse": 22, "pretty pink princess land": 23}

ZONE_MAP = {"safe zone: awakening site": 0, "tutorial zone": 1, "sewers": 2, "forest": 3,
            "cave of many things": 4, "the sky": 5, "high security base": 6,
            "gordon ramsay bolton": 7, "clock dimension": 8, "grand corrupted tree": 9,
            "the 2d universe": 10, "ancient battlefield": 11, "jake from accounting": 12,
            "a very strange place": 13, "mega lands": 14, "uug, the unmentionable": 15,
            "the beardverse": 16, "walderp": 17, "badly drawn world": 18, "boring-ass earth": 19,
            "the beast": 20, "chocolate world": 21, "the evilverse": 22,
            "pretty pink princess land": 23, "greasy nerd": 24, "meta land": 25,
            "interdimensional party": 26, "the godmother": 27, "typo zonw": 28,
            "the fad-lands": 29, "jrpgville": 30, "the exile": 31, "the rad-lands": 32,
            "back to school": 33, "the west world": 34, "it hungers": 35,
            }
