import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import datetime
import insights


def plot_category_pie(expenses):
    if not expenses:
        print("No expenses to display.")
        return

    breakdown = insights.category_breakdown(expenses)

    labels = list(breakdown.keys())
    sizes = [data["total"] for data in breakdown.values()]
    colors = [
        "#FF6B6B", "#4ECDC4", "#45B7D1",
        "#96CEB4", "#FFEAA7", "#DDA0DD",
        "#98D8C8", "#F7DC6F"
    ]

    fig, ax = plt.subplots(figsize=(9, 6))

    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        colors=colors[:len(labels)],
        startangle=140,
        pctdistance=0.85
    )

    for text in texts:
        text.set_fontsize(11)
    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_fontweight("bold")

    total = sum(sizes)
    ax.set_title(
        f"Spending by Category\nTotal: Rs.{total:.2f}",
        fontsize=14,
        fontweight="bold",
        pad=20
    )

    plt.tight_layout()
    plt.show()


def plot_monthly_bar(expenses):
    if not expenses:
        print("No expenses to display.")
        return

    summary = insights.monthly_summary(expenses)

    months = list(summary.keys())
    amounts = [data["total"] for data in summary.values()]

    colors = []
    max_amount = max(amounts)
    for amount in amounts:
        if amount == max_amount:
            colors.append("#FF6B6B")
        else:
            colors.append("#4ECDC4")

    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.bar(months, amounts, color=colors, width=0.5, edgecolor="white")

    for bar, amount in zip(bars, amounts):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + max_amount * 0.01,
            f"Rs.{amount:.0f}",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold"
        )

    ax.set_xlabel("Month", fontsize=12)
    ax.set_ylabel("Total Spending (Rs.)", fontsize=12)
    ax.set_title("Monthly Spending Trend", fontsize=14, fontweight="bold")
    ax.set_ylim(0, max_amount * 1.15)

    plt.xticks(rotation=45, ha="right")

    high_patch = mpatches.Patch(color="#FF6B6B", label="Highest month")
    normal_patch = mpatches.Patch(color="#4ECDC4", label="Other months")
    ax.legend(handles=[high_patch, normal_patch])

    plt.tight_layout()
    plt.show()


def plot_category_bar(expenses):
    if not expenses:
        print("No expenses to display.")
        return

    breakdown = insights.category_breakdown(expenses)

    categories = list(breakdown.keys())
    amounts = [data["total"] for data in breakdown.values()]
    counts = [data["count"] for data in breakdown.values()]

    fig, ax1 = plt.subplots(figsize=(10, 6))

    bars = ax1.bar(
        categories,
        amounts,
        color="#45B7D1",
        width=0.5,
        edgecolor="white",
        label="Total Amount"
    )

    for bar, amount in zip(bars, amounts):
        ax1.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + max(amounts) * 0.01,
            f"Rs.{amount:.0f}",
            ha="center",
            va="bottom",
            fontsize=9,
            fontweight="bold"
        )

    ax2 = ax1.twinx()
    ax2.plot(
        categories,
        counts,
        color="#FF6B6B",
        marker="o",
        linewidth=2,
        markersize=8,
        label="No. of transactions"
    )
    ax2.set_ylabel("Number of Transactions", fontsize=12, color="#FF6B6B")

    ax1.set_xlabel("Category", fontsize=12)
    ax1.set_ylabel("Total Amount (Rs.)", fontsize=12)
    ax1.set_title("Category-wise Spending Analysis", fontsize=14,
                  fontweight="bold")

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper right")

    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.show()


def plot_spending_trend(expenses):
    if not expenses:
        print("No expenses to display.")
        return

    summary = insights.monthly_summary(expenses)

    if len(summary) < 2:
        print("Need at least 2 months of data for trend analysis.")
        return

    months = list(summary.keys())
    amounts = [data["total"] for data in summary.values()]

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(
        months,
        amounts,
        color="#4ECDC4",
        marker="o",
        linewidth=2.5,
        markersize=10,
        markerfacecolor="#FF6B6B",
        markeredgecolor="white",
        markeredgewidth=2
    )

    ax.fill_between(
        months,
        amounts,
        alpha=0.15,
        color="#4ECDC4"
    )

    for i, (month, amount) in enumerate(zip(months, amounts)):
        ax.annotate(
            f"Rs.{amount:.0f}",
            (month, amount),
            textcoords="offset points",
            xytext=(0, 12),
            ha="center",
            fontsize=10,
            fontweight="bold"
        )

    ax.set_xlabel("Month", fontsize=12)
    ax.set_ylabel("Total Spending (Rs.)", fontsize=12)
    ax.set_title("Spending Trend Over Time", fontsize=14, fontweight="bold")
    ax.grid(True, linestyle="--", alpha=0.5)

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def plot_daily_expenses(expenses):
    if not expenses:
        print("No expenses to display.")
        return

    date_totals = {}
    for expense in expenses:
        if expense.date not in date_totals:
            date_totals[expense.date] = 0
        date_totals[expense.date] += expense.amount

    sorted_dates = dict(sorted(date_totals.items()))
    dates = list(sorted_dates.keys())
    amounts = list(sorted_dates.values())

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.bar(dates, amounts, color="#96CEB4", width=0.6, edgecolor="white")

    avg = sum(amounts) / len(amounts)
    ax.axhline(
        y=avg,
        color="#FF6B6B",
        linestyle="--",
        linewidth=1.5,
        label=f"Daily average: Rs.{avg:.2f}"
    )

    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Amount (Rs.)", fontsize=12)
    ax.set_title("Daily Spending", fontsize=14, fontweight="bold")
    ax.legend()

    plt.xticks(rotation=60, ha="right")
    plt.tight_layout()
    plt.show()