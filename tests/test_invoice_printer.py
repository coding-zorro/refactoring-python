from unittest import TestCase
from app.invoice_printer import statement, Play, Invoice, Performance

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

        expected = "Statement for BigCo\n"
        expected += "\tHamlet: $650.00 (55 seats)\n"
        expected += "\tAs You Like It: $580.00 (35 seats)\n"
        expected += "\tOthello: $500.00 (40 seats)\n"
        expected += "Amount owed is $1,730.00\n"
        expected += "You earned 47 credits"
        self.assertEqual(expected, statement(invoice, plays))
    
