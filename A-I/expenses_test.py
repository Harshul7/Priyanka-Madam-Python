import unittest

from ExpensesLoader import *
from ExpensesManager import *


class Expenses_Test(unittest.TestCase):

    def setUp(self):
        """The setUp function runs before every test function."""

        # create expenses dictionary and populate with data
        self.expenses = {'food': Expense('food', 5.00), 'coffee': Expense('coffee', 12.40),
                         'rent': Expense('rent', 825.00), 'clothes': Expense('clothes', 45.00),
                         'entertainment': Expense('entertainment', 135.62), 'music': Expense('music', 324.00),
                         'family': Expense('family', 32.45)}

    def test_import_expenses(self):
        print("\ntest_import_expenses\n")
        # import expenses files
        expenses = {}      # create instance of ExpensesLoader class
        expenses_loader = ExpensesLoader()

        # call import_expenses method in ExpensesLoader class
        # to import expense files and store in dictionary
        expenses_loader.import_expenses(expenses, 'expenses.txt')
        expenses_loader.import_expenses(expenses, 'expenses_2.txt')

        # test existing expense amounts
        self.assertAlmostEqual(45, expenses['clothes'].amount)
        self.assertAlmostEqual(12.40, expenses['coffee'].amount)
        self.assertAlmostEqual(135.62, expenses['entertainment'].amount)

    def test_get_expense(self):
        print("\ntest_get_expense\n")
        # create instance of ExpensesManager class
        expenses_manager = ExpensesManager()

        # test getting expenses based on expense type
        self.assertAlmostEqual(12.40, expenses_manager.get_expense(self.expenses, "coffee").amount)

        # test non-existing expense types
        self.assertEqual(None, expenses_manager.get_expense(self.expenses, "phone"))

        # test getting expenses based on expense type
        self.assertAlmostEqual(825.00, expenses_manager.get_expense(self.expenses, "rent").amount)

        # test non-existing expense types
        self.assertEqual(None, expenses_manager.get_expense(self.expenses, "internet"))

    def test_add_expense(self):
        print("\ntest_add_expense\n")
        # create instance of ExpensesManager class
        expenses_manager = ExpensesManager()

        # test adding a new expense
        expenses_manager.add_expense(self.expenses, "fios", 84.5)
        self.assertAlmostEqual(84.5, self.expenses.get("fios").amount)

        #  test adding to existing expenses
        expenses_manager.add_expense(self.expenses, "coffee", 5.5)
        self.assertAlmostEqual(17.90, self.expenses.get("coffee").amount)

        # test adding a new expense
        expenses_manager.add_expense(self.expenses, "tea", 64.5)
        self.assertAlmostEqual(64.5, self.expenses.get("tea").amount)

    def test_deduct_expense(self):
        print("\ntest_deduct_expense\n")
        # create instance of ExpensesManager class
        expenses_manager = ExpensesManager()

        # test deducting from expense
        expenses_manager.deduct_expense(self.expenses, "coffee", .99)
        self.assertAlmostEqual(11.41, self.expenses.get("coffee").amount)

        # test deducting from expense
        expenses_manager.deduct_expense(self.expenses, "entertainment", 100)
        self.assertAlmostEqual(35.62, self.expenses.get("entertainment").amount)

        #  test deducting too much from expense
        with self.assertRaises(RuntimeError):
            expenses_manager.deduct_expense(self.expenses, "coffee", 20)

        # test deducting from non-existing expense
        expenses_manager.deduct_expense(self.expenses, "tea", 30)

    def test_update_expense(self):
        print("\ntest_update_expense\n")
        # create instance of ExpensesManager class
        expenses_manager = ExpensesManager()

        # test updating an expense
        expenses_manager.update_expense(self.expenses, "clothes", 19.99)
        self.assertAlmostEqual(19.99, expenses_manager.get_expense(self.expenses, "clothes").amount)

        #   test updating an expense
        expenses_manager.update_expense(self.expenses, "food", 50.00)
        self.assertAlmostEqual(50.00, expenses_manager.get_expense(self.expenses, "food").amount)

        #   test updating a non-existing expense
        expenses_manager.update_expense(self.expenses, "internet", 30.00)

    def test_sort_expenses(self):
        print("\ntest_sort_expenses\n")
        # create instance of ExpensesManager class
        expenses_manager = ExpensesManager()

        # test sorting expenses by 'expense_type'
        expense_type_sorted_expenses = [('clothes', 45.0),
                                        ('coffee', 12.4),
                                        ('entertainment', 135.62),
                                        ('family', 32.45),
                                        ('food', 5.0),
                                        ('music', 324.0),
                                        ('rent', 825.0)]

        self.assertListEqual(expense_type_sorted_expenses,
                             expenses_manager.sort_expenses(self.expenses, "expense_type"))

        # test sorting expenses by 'amount'
        amount_sorted_expenses = [('rent', 825.0),
                                  ('music', 324.0),
                                  ('entertainment', 135.62),
                                  ('clothes', 45.0),
                                  ('family', 32.45),
                                  ('coffee', 12.4),
                                  ('food', 5.0)]
        
        self.assertListEqual(amount_sorted_expenses,
                             expenses_manager.sort_expenses(self.expenses, "amount"))


    def test_export_expenses(self):
        print("\ntest_export_expenses\n")
        # create instance of ExpensesManager class
        expenses_manager = ExpensesManager()

        # test export with existing expense types
        file = 'export1.txt'
        expense_types = ['coffee', 'clothes']
        expenses_manager.export_expenses(self.expenses, expense_types, file)

        # read the exported file
        f = open(file)
        lines = f.readlines()
        f.close()
        self.assertEqual('coffee: 12.40', lines[0].strip())
        self.assertEqual('clothes: 45.00', lines[1].strip())

        #   test exporting with some non-existent expense types.
        file2 = 'export2.txt'
        expense_types2 = ['coffee', 'clothes', 'internet']
        expenses_manager.export_expenses(self.expenses, expense_types2, file2)
        with open(file2) as f:
            lines2 = f.readlines()
        self.assertEqual('coffee: 12.40', lines2[0].strip())
        self.assertEqual('clothes: 45.00', lines2[1].strip())

        #   test exporting with some duplicate expense types.
        file3 = 'export3.txt'
        expense_types3 = ['coffee', 'clothes', 'coffee']
        expenses_manager.export_expenses(self.expenses, expense_types2, file2)
        with open(file3) as f:
            lines3 = f.readlines()
        self.assertEqual('coffee: 12.40', lines3[0].strip())
        self.assertEqual('clothes: 45.00', lines3[1].strip())
        self.assertEqual('coffee: 12.40', lines3[2].strip())


if __name__ == '__main__':
    unittest.main()
