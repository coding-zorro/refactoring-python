import math
from typing import List, Dict
from collections import namedtuple

Play = namedtuple('Play', ['name', 'type'])
Performance = namedtuple('Performance', ['play_id', 'audience'])
Invoice = namedtuple("Invoice", ["customer", "performances"])

def statement (invoice: Invoice, plays: Dict[str, Play]) -> str:
    total_amount = 0
    volume_credits = 0
    result = f"Statement for {invoice.customer}\n"

    def format(n):
        return "${:0,.2f}".format(n)
        
    for perf in invoice.performances:
        play = plays[perf.play_id]
        this_amount = 0

        if(play.type == "tragedy"):
            this_amount = 40000
            if (perf.audience > 30):
                this_amount += 1000 * (perf.audience - 30); 
        elif(play.type == "comedy"):
            this_amount = 30000
            if (perf.audience > 20):
                this_amount += 10000 + 500 * (perf.audience - 20)
            this_amount += 300 * perf.audience
        else:
            raise Exception("unknown type: " + play.type)
       
        # add volume credits
        volume_credits += max(perf.audience - 30, 0)
        #add extra credit for every ten comedy attendees
        if ("comedy" == play.type):
            volume_credits += math.floor(perf.audience / 5)
        #print line for this order
        result += f"\t{play.name}: {format(this_amount/100)} ({perf.audience} seats)\n" 
        total_amount += this_amount
    result += f"Amount owed is {format(total_amount/100)}\n"
    result += f"You earned {volume_credits} credits" 
    return result
