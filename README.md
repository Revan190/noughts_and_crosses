# noughts_and_crosses
 
This is 
This is a simple "Noughts and crosses" game project created by Revan190, whose name he doesn't want to reveal at the moment. This documentation is intended to help you figure out which folder and/or file does what. Well, here we go:

This is structure project:
noughts_and_crosses/
    game/                     # Main directory with game logic
        bot/                 # Catalog for different AI levels
            __init__.py     # Package initialization `game/bot/`
            easy_ai.py      # Light AI logic
            medium_ai.py    # Medium AI logic
            hard_ai.py      # Hard AI logic
        __init__.py         # Package initialization `game/`
        ai_player.py         # Basic class for AI player
        board.py             # Game board logic
        game.py              # Basic game logic
        player.py            # Player logic for game
        scoreboard.py        # Tracking game results
        settings.py          # Game Settings
    tests/                   # Catalog with tests
        ai/                  # Tests for AI
            __init__.py     # Package initialization `tests/ai/`
            test_easy_ai.py # Tests for Light AI logic
            test_medium_ai.py # Tests for Medium AI logic
            test_hard_ai.py # Tests for Hard AI logic
        game/                # Tests for game logic
            __init__.py     # Package initialization `tests/game/`
            test_ai.py      # Tests for the AI ​​class
            test_board.py   # Playing Field Tests
            test_game.py    # Tests for the main game logic
            test_player.py   # Tests for the player
            test_scoreboard.py # Tests for the results table
            test_settings.py # Tests for game settings
        ui/                  # User Interface Tests
            __init__.py     # Package initialization `tests/ui/`
            test_console.py  # Tests for the console interface
            test_gui_ui.py   # GUI tests
        utils/               # Tests for utilities
            __init__.py     # Package initialization `tests/utils/`
            test_utils.py    # Tests for utilities
        __init__.py         # Package initialization `tests/`
    ui/                      # Catalog with user interface
        __init__.py         # Package initialization `ui`
        console_ui.py       # Console interface
        gui_ui.py           # GUI
    .gitattributes           # Git Settings
    .gitignore               # Ignored files for Git
    main.py                  # Main file for launching the game
    README.md                # Project documentation
    requirements.txt         # Project Dependencies
    utils.py                 # Utilities

The command to activate the game is `python main.py`, but before that you need to activate .venv.