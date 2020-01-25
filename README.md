# coderdojo
Notes for CoderDojo Tramore (python).

This is a collection of worksheets covering programming in python.

## General Python and <code>turtle</code> Worksheets

This subset of worksheets were based around the <code>turtle</code> module. We used the python editor [Thonny](https://thonny.org) across OSX, Linux and windows.

 * [01-Guess_my_Number](01-Guess_my_Number/01-Guess_my_Number.pdf)</br>
 Simple guessing game to demo storing data, looping and making decisions. Very little code is given as worksheet was intended to be augmented with one-on-one instruction.

 * [02-Take_Away](02-Take_Away/02-Take_Away/.pdf)</br>
 Simple game that we first implement on the console and later we will develop a graphical version.

 * [03-Graphical_Take_Away](03-Graphical_Take_Away/03-Graphical_Take_Away.pdf)</br>
 Introduction to drawing using the <code>turtle</code> module.

 * [04-Some_More_Turtle_Graphics](04-Some_More_Turtle_Graphics/04-Some_More_Turtle_Graphics.pdf)</br>
 In this worksheet we will build more complicated drawings using <code>turtle</code> module.

 * [05-Doing_Physics_with_Python](05-Doing_Physics_with_Python/05-Doing_Physics_with_Python.pdf)</br>
 This worksheet is a little different. Here we use python to see how objects behave when they are dropped from a height or thrown upwards.

 * [06-Graphical_Take_Away_-_Second_Time_Lucky](06-Graphical_Take_Away_-_Second_Time_Lucky/06-Graphical_Take_Away_-_Second_Time_Lucky.pdf)</br>
 Finally we return to our Take Away game and implement a graphical version using <code>turtle</code> graphics.

 * [07-Monkey_Wars](07-Monkey_Wars/07-Monkey_Wars.pdf)</br>
 OK, we are ready for more complicated games. This time we will build our version of the classic Monkey Wars game.

 * [08-Working_with_Lists](08-Working_with_Lists/08-Working_with_Lists.pdf)</br>
 This is the first of our worksheets intended to cover various fundamental programming concepts. In this worksheet we will look at lists.

 * [11-Building_a_GUI](11-Building_a_GUI/11-Building_a_GUI.pdf)</br>
 In this worksheet we will develop a simple graphical interface which we can use to control our other python games and programs.

 * [12-Happy_Holidays](12-Happy_Holidays/12-Happy_Holidays.pdf)</br>
 We build some animated e-cards using the <code>turtle</code> module.

 * [15-Cellular_Automation](15-Cellular_Automation/15-Cellular_Automation.pdf)</br>
 This worksheet is much more advanced and uses cellular automation to simulate how fires spread in a forest.

## <code>pgzero</code>/<code>pygame</code> Worksheets

In January 2020 we switched focus and:

 * Moved from <code>turtle</code> to
  [Pygame Zero (pgzero)](https://pygame-zero.readthedocs.io/en/stable/) for graphics. Pygame Zero is a layer on top of   
[pygame](https://www.pygame.org) and simplifies game development for new programmers.
 * Switched editor from [Thonny](https://thonny.org) to
 [Mu](https://codewith.mu). The Mu editor has a nicer interface and has some nice tools to identify and fix coding style issues (now if only it could fix my spelling ...). Recent versions of Thonny also support [pgzero](https://pygame-zero.readthedocs.io/en/stable/) so you can continue to use that if you wish.

In the following worksheets, the plan is to give the steps to build the basic game idea, and then give suggestions/outlines on how this game idea can be further developed into a proper game.
Many of the game ideas from the excellent book <a href="https://www.dk.com/uk/book/9780241317792-computer-coding-python-games-for-kids/">Coding Games in Python (Computer Coding for Kids)</a> and from suggestions from the coders themselves.
</div>

* [Python tools and other software](20-Python_for_2020/20-Python_for_2020.pdf)</br>

* [Fruit Ninja games](21-fruit_ninga_games/21-fruit_ninga_games.pdf)
  * Basic game idea
  * Adding sound effects and background music
  * Using physics to get moving targets
  * Having lives to deal with missing the target
  * Multiple fruit (and non-fruit) targets
* [Collector games](22-collector_games/22-collector_games.pdf)
  * Basic game idea
  * Adding sound effects and background music
  * Multiple levels with increasing difficulty
  * Different and vanishing targets 
  
* Network games
  * Basic game idea
  
* Geometry Dash games

## Typesetting the worksheets

The worksheets are written in LaTeX, typeset using luaLaTeX due to extra fonts, using the document class [coderdojo.cls](latex/coderdojo.cls).
