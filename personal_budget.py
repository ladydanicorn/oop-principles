# Task 1

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

# Task 2

    def get_category_name(self):
        return self.__category_name
    
    def set_category_name(self, new_category_name):
        self.__category_name = new_category_name

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, new_budget,):
        if new_budget > 0:
            self.__allocated_budget = new_budget
            self.__remaining_budget = new_budget
        else:
            print("Budget must be positive number.")

# Task 3 - Note, parts of Task 3 have been added into existing code

    def get_remaining_budget(self):
        return self.__remaining_budget
    
    def add_expense(self, expense_amount):
        if expense_amount <= 0:
            print("Expense amount must be a positive number.")
        elif expense_amount > self.__remaining_budget:
            print("Expense exceeds current budget.")
        else:
            self.__remaining_budget -= expense_amount
            print(f"Expense of {expense_amount} added. New remaining budget: {self.__remaining_budget}")

# Task 4

    def display_category_summary(self):
        print("Category Summary")
        print(f"Category Name: {self.get_category_name()}")
        print(f"Allocated Budget: {self.get_allocated_budget()}")
        print(f"Remaining Budget: {self.get_remaining_budget()}")


food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()