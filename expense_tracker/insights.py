from datetime import datetime


def monthly_summary(expenses):
    if not expenses:
        return {}

    totals = {}

    for expense in expenses:
        month_key = expense.date[:7]

        if month_key not in totals:
            totals[month_key] = {
                "total": 0,
                "count": 0,
                "expenses": []
            }

        totals[month_key]["total"] += expense.amount
        totals[month_key]["count"] += 1
        totals[month_key]["expenses"].append(expense)

    sorted_totals = dict(sorted(totals.items()))
    return sorted_totals


def category_breakdown(expenses):
    if not expenses:
        return {}

    breakdown = {}

    for expense in expenses:
        cat = expense.category

        if cat not in breakdown:
            breakdown[cat] = {
                "total": 0,
                "count": 0,
                "expenses": []
            }

        breakdown[cat]["total"] += expense.amount
        breakdown[cat]["count"] += 1
        breakdown[cat]["expenses"].append(expense)

    sorted_breakdown = dict(
        sorted(breakdown.items(),
               key=lambda item: item[1]["total"],
               reverse=True)
    )

    return sorted_breakdown


def highest_spending_category(expenses):
    if not expenses:
        return None, 0

    breakdown = category_breakdown(expenses)

    top_category = max(
        breakdown,
        key=lambda cat: breakdown[cat]["total"]
    )

    return top_category, breakdown[top_category]["total"]


def lowest_spending_category(expenses):
    if not expenses:
        return None, 0

    breakdown = category_breakdown(expenses)

    lowest_category = min(
        breakdown,
        key=lambda cat: breakdown[cat]["total"]
    )

    return lowest_category, breakdown[lowest_category]["total"]


def average_daily_spending(expenses):
    if not expenses:
        return 0

    total = sum(expense.amount for expense in expenses)

    unique_dates = set(expense.date for expense in expenses)

    return total / len(unique_dates)


def average_per_transaction(expenses):
    if not expenses:
        return 0

    total = sum(expense.amount for expense in expenses)
    return total / len(expenses)


def most_expensive_expense(expenses):
    if not expenses:
        return None

    return max(expenses, key=lambda e: e.amount)


def least_expensive_expense(expenses):
    if not expenses:
        return None

    return min(expenses, key=lambda e: e.amount)


def category_percentages(expenses):
    if not expenses:
        return {}

    breakdown = category_breakdown(expenses)
    total_spending = sum(
        data["total"] for data in breakdown.values()
    )

    percentages = {}
    for cat, data in breakdown.items():
        percentages[cat] = {
            "total": data["total"],
            "count": data["count"],
            "percentage": (data["total"] / total_spending) * 100
        }

    return percentages


def spending_trend(expenses):
    if not expenses:
        return []

    summary = monthly_summary(expenses)

    trend = []
    months = list(summary.keys())

    for i in range(1, len(months)):
        current = summary[months[i]]["total"]
        previous = summary[months[i - 1]]["total"]
        change = current - previous
        percent_change = (change / previous) * 100

        trend.append({
            "month": months[i],
            "total": current,
            "change": change,
            "percent_change": percent_change,
            "direction": "up" if change > 0 else "down"
        })

    return trend