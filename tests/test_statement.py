from unittest import TestCase
from app.invoices import statement, Play, Invoice, Performance

class InvoiceTest(TestCase):
    def test_statement(self):
        plays = {
            "hamlet": Play("Hamlet", "tragedy"),
            "as-like": Play("As You Like It", "comedy"),
            "othello": Play("Othello", "tragedy")
        }

        invoice = Invoice(
                "BigCo", 
                [
                    Performance("hamlet", 55),
                    Performance("as-like", 35),
                    Performance("othello", 40),
                ]
            )

        expected = "Statement for BigCo\n" + "\tHamlet: $650.00 (55 seats)\n" + "\tAs You Like It: $580.00 (35 seats)\n" + "\tOthello: $500.00 (40 seats)\n" + "Amount owed is $1,730.00\n" + "You earned 47 credits"
        self.assertEqual(expected, statement(invoice, plays))
    

    
    # assert expected == statement(invoice, plays)
# def test_statement(TestCase):
#     plays = {
#         "hamlet": Play("Hamlet", "tragedy"),
#         "as-like": Play("As You Like It", "comedy"),
#         "othello": Play("Othello", "tragedy")
#     }

#     invoice = Invoice(
#                 "BigCo", 
#                 [
#                     Performance("hamlet", 55),
#                     Performance("as-like", 35),
#                     Performance("othello", 40),
#                 ]
#             )

#     expected = "Statement for BigCo\n" + "\tHamlet: $650.00 (55 seats)\n" + "\tAs You Like It: $580.00 (35 seats)\n" + "\tOthello: $500.00 (40 seats)\n" + "Amount owed is $1,730.00\n" + "You earned 47 credits"
#     assert expected == statement(invoice, plays)
