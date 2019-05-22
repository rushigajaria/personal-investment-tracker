#Interface to control what to do
from computations import calculate_profit, buy_sell_recommendations
from visualize import graph

def help_message(_):
    print "This is a program to view your portfolio."
    print "Type 'recommend' to see buy-sell recommendations based on the score"
    print "Type 'graph' to visualize your portfolio"
    print "Type 'profit' to see how much you've made"

def error_message(command):
    print "'%s' is not a valid command" % command

commands = {"help": help_message,
            "profit": calculate_profit,
            "graph": graph,
            "recommend": buy_sell_recommendations}

while(1):
    print "\n"
    print "What do you want to do? Type 'help' for help"
    command = raw_input().lower()
    commands.get(command, error_message)(command)
