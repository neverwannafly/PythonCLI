#!/usr/bin/env python3

from packages import (
    execute_news, 
    execute_quote,
    execute_wallpaper,
)

import cmd
import sys

class CMDApplication(cmd.Cmd):

    try:
        intro = "Welcome {username}!".format(username=sys.argv[1])
    except IndexError:
        print("Please provide your username!")
        exit()
    prompt = '(shell) '

    def do_history(self, arg):
        "Shows history of commands used"
        print(self._history)

    def do_news(self, arg):
        "Read today's news"
        execute_news()

    def do_quotes(self, arg):
        "Read quote of the day"
        execute_quote()

    def do_wallpapers(self, arg):
        "Get links for some good wallpapers"
        execute_wallpaper()

    def do_exit(self, arg):
        "Exit the application"
        return -1

    def precmd(self, line):
        """ This method is called after the input but before
            it has been interpreted. If you want to modify the input line
            before execution (for example, variable substitution) do it here.
        """
        if line != '':
            self._history += [ line.strip() ]
        return line

    def postcmd(self, stop, line):
        """If you want to stop the console, return something that evaluates to true.
           If you want to do some post command processing, do it here.
        """
        return stop

    def preloop(self):
        "Initialization before prompting user for commands"
        cmd.Cmd.preloop(self)
        self._history = []

    def postloop(self):
        "Take care of any unfinished business."
        print("Exiting...")
        cmd.Cmd.postloop(self)

if __name__=='__main__':
    CMDApplication().cmdloop()
    