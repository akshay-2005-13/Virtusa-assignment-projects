from datetime import datetime
from expense import Expense
import tracker
import insights
import visualizer


def display_header():
    print("\n" + "=" * 55)
    print("       SMART EXPENSE TRACKER WITH INSIGHTS")
    print("=" * 55)


def display_menu():
    print("\n" + "-" * 55)
    print("                    MAIN MENU")
    print("-" * 55)
    print("  1.  Add New Expense")
    print("  2.  View All Expenses")
    print("  3.  View This Month's Expenses")
    print("  4.  Monthly Summary")
    print("  5.  Category Analysis")
    print("  6.  Spending Insights")
    print("  7.  Delete an Expense")
    print("  8.  Charts & Visualizations")
    print("  0.  Exit")
    print("-" * 55)


def display_chart_menu():
    print("\n--- Charts Menu ---")
    print("  1. Category Pie Chart")
    print("  2. Monthly Bar Chart")
    print("  3. Category Bar Chart")
    print("  4. Spending Trend Line")
    print("  5. Daily Spending Chart")
    print("  0. Back to Main Menu")


def get_valid_amount():
    while True:
        try:
            amount = float(input("  Enter amount (Rs.): ").strip())
            if amount <= 0:
                print("  Amount must be greater than zero. Try again.")
                continue
            return amount
        except ValueError:
            print("  Invalid amount. Enter a number like 450 or 1200.50")


def get_valid_date():
    while True:
        date_input = input(
            "  Enter date (YYYY-MM-DD) or press Enter for today: "
        ).strip()

        if date_input == "":
            return datetime.now().strftime("%Y-%m-%d")

        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("  Invalid date format. Use YYYY-MM-DD like 2024-01-15")


def get_valid_category():
    print("  Available categories:")
    for i, cat in enumerate(Expense.CATEGORIES, start=1):
        print(f"    {i}. {cat}")

    while True:
        try:
            choice = int(input("  Choose category number: ").strip())
            if 1 <= choice <= len(Expense.CATEGORIES):
                return Expense.CATEGORIES[choice - 1]
            else:
                print(f"  Enter a number between 1 and {len(Expense.CATEGORIES)}")
        except ValueError:
            print("  Invalid input. Enter a number.")


def get_valid_month_year():
    while True:
        month_input = input(
            "  Enter month (YYYY-MM) or press Enter for current month: "
        ).strip()

        if month_input == "":
            now = datetime.now()
            return now.year, now.month

        try:
            parsed = datetime.strptime(month_input, "%Y-%m")
            return parsed.year, parsed.month
        except ValueError:
            print("  Invalid format. Use YYYY-MM like 2024-01")


def handle_add_expense():
    print("\n--- Add New Expense ---")
    try:
        date = get_valid_date()
        amount = get_valid_amount()
        category = get_valid_category()
        description = input("  Enter description: ").strip()

        if not description:
            print("  Description cannot be empty.")
            return

        expense = tracker.add_expense(date, amount, category, description)

        print("\n  Expense added successfully!")
        print(f"  {expense}")

    except ValueError as e:
        print(f"  Error: {e}")
    except Exception as e:
        print(f"  Unexpected error: {e}")


def handle_view_all():
    print("\n--- All Expenses ---")
    expenses = tracker.get_all_expenses()

    if not expenses:
        print("  No expenses recorded yet.")
        return

    print(f"\n  {'DATE':<12} {'CATEGORY':<15} {'AMOUNT':>12} {'DESCRIPTION'}")
    print("  " + "-" * 60)

    for i, expense in enumerate(expenses, start=1):
        print(f"  [{i:>2}] {expense}")

    total = tracker.get_total_spending(expenses)
    print("  " + "-" * 60)
    print(f"  Total: Rs.{total:.2f} across {len(expenses)} transactions")


def handle_current_month():
    print("\n--- This Month's Expenses ---")
    expenses = tracker.get_current_month_expenses()

    if not expenses:
        print("  No expenses this month yet.")
        return

    now = datetime.now()
    print(f"  Month: {now.strftime('%B %Y')}")
    print(f"\n  {'DATE':<12} {'CATEGORY':<15} {'AMOUNT':>12} {'DESCRIPTION'}")
    print("  " + "-" * 60)

    for expense in expenses:
        print(f"  {expense}")

    total = tracker.get_total_spending(expenses)
    print("  " + "-" * 60)
    print(f"  Month Total: Rs.{total:.2f} ({len(expenses)} transactions)")


def handle_monthly_summary():
    print("\n--- Monthly Summary ---")
    expenses = tracker.get_all_expenses()

    if not expenses:
        print("  No expenses recorded yet.")
        return

    summary = insights.monthly_summary(expenses)

    print(f"\n  {'MONTH':<12} {'TRANSACTIONS':>14} {'TOTAL':>14}")
    print("  " + "-" * 44)

    for month, data in summary.items():
        print(f"  {month:<12} {data['count']:>14} {'Rs.'+str(round(data['total'],2)):>14}")

    all_totals = [data["total"] for data in summary.values()]
    best_month = max(summary, key=lambda m: summary[m]["total"])
    low_month = min(summary, key=lambda m: summary[m]["total"])

    print("  " + "-" * 44)
    print(f"\n  Highest spending month : {best_month} "
          f"(Rs.{summary[best_month]['total']:.2f})")
    print(f"  Lowest spending month  : {low_month} "
          f"(Rs.{summary[low_month]['total']:.2f})")


def handle_category_analysis():
    print("\n--- Category Analysis ---")
    expenses = tracker.get_all_expenses()

    if not expenses:
        print("  No expenses recorded yet.")
        return

    percentages = insights.category_percentages(expenses)
    total = tracker.get_total_spending(expenses)

    print(f"\n  Total spending: Rs.{total:.2f}")
    print(f"\n  {'CATEGORY':<15} {'TRANSACTIONS':>13} {'TOTAL':>12} {'SHARE':>8}")
    print("  " + "-" * 52)

    for cat, data in percentages.items():
        bar_length = int(data["percentage"] / 5)
        bar = "#" * bar_length
        print(f"  {cat:<15} {data['count']:>13} "
              f"{'Rs.'+str(round(data['total'],2)):>12} "
              f"{data['percentage']:>7.1f}%")
        print(f"  {'':15} {bar}")

    top_cat, top_amt = insights.highest_spending_category(expenses)
    print(f"\n  Highest spending category: {top_cat} (Rs.{top_amt:.2f})")


def handle_insights():
    print("\n--- Spending Insights ---")
    expenses = tracker.get_all_expenses()

    if not expenses:
        print("  No expenses recorded yet.")
        return

    print(f"\n  Total expenses recorded  : {len(expenses)}")
    print(f"  Total amount spent       : Rs."
          f"{tracker.get_total_spending(expenses):.2f}")
    print(f"  Average per transaction  : Rs."
          f"{insights.average_per_transaction(expenses):.2f}")
    print(f"  Average daily spending   : Rs."
          f"{insights.average_daily_spending(expenses):.2f}")

    most_exp = insights.most_expensive_expense(expenses)
    least_exp = insights.least_expensive_expense(expenses)

    print(f"\n  Most expensive expense:")
    print(f"  {most_exp}")
    print(f"\n  Least expensive expense:")
    print(f"  {least_exp}")

    trend = insights.spending_trend(expenses)
    if trend:
        print(f"\n  Spending trend:")
        for t in trend:
            arrow = "↑" if t["direction"] == "up" else "↓"
            print(f"  {t['month']}: Rs.{t['total']:.2f} "
                  f"{arrow} {abs(t['percent_change']):.1f}% "
                  f"vs previous month")


def handle_delete():
    print("\n--- Delete an Expense ---")
    handle_view_all()

    expenses = tracker.get_all_expenses()
    if not expenses:
        return

    while True:
        try:
            index = int(input("\n  Enter expense number to delete (0 to cancel): "))
            if index == 0:
                print("  Deletion cancelled.")
                return
            if 1 <= index <= len(expenses):
                expense = expenses[index - 1]
                confirm = input(
                    f"  Delete '{expense.description}' "
                    f"(Rs.{expense.amount:.2f})? (yes/no): "
                ).strip().lower()

                if confirm == "yes":
                    success = tracker.delete_expense_by_index(index - 1)
                    if success:
                        print("  Expense deleted successfully.")
                    else:
                        print("  Failed to delete expense.")
                else:
                    print("  Deletion cancelled.")
                return
            else:
                print(f"  Enter a number between 1 and {len(expenses)}")
        except ValueError:
            print("  Invalid input. Enter a number.")


def handle_charts():
    expenses = tracker.get_all_expenses()

    if not expenses:
        print("  No expenses to visualize yet.")
        return

    while True:
        display_chart_menu()
        choice = input("  Enter choice: ").strip()

        if choice == "1":
            visualizer.plot_category_pie(expenses)
        elif choice == "2":
            visualizer.plot_monthly_bar(expenses)
        elif choice == "3":
            visualizer.plot_category_bar(expenses)
        elif choice == "4":
            visualizer.plot_spending_trend(expenses)
        elif choice == "5":
            visualizer.plot_daily_expenses(expenses)
        elif choice == "0":
            break
        else:
            print("  Invalid choice.")


def start():
    display_header()
    import storage
    storage.initialize_file()

    while True:
        display_menu()
        choice = input("  Enter your choice: ").strip()

        if choice == "1":
            handle_add_expense()
        elif choice == "2":
            handle_view_all()
        elif choice == "3":
            handle_current_month()
        elif choice == "4":
            handle_monthly_summary()
        elif choice == "5":
            handle_category_analysis()
        elif choice == "6":
            handle_insights()
        elif choice == "7":
            handle_delete()
        elif choice == "8":
            handle_charts()
        elif choice == "0":
            print("\n  Thank you for using Smart Expense Tracker. Goodbye!")
            print("=" * 55)
            break
        else:
            print("  Invalid choice. Enter a number from the menu.")