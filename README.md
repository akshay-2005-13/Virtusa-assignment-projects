# Virtusa Assignment Projects

Hi, I'm Akshay. This repo has three projects I built as part of my assignment —
one in Java, one in Python, and one in SQL. I wrote everything from scratch,
so this is a good look at how I think through problems and structure code.

---

## 1. Library Management System — Java

A command-line app for managing books, users, borrowing, and returning.
Built with Java OOP and a layered architecture.

**Tools:** Java 17, Maven

**What it does:**
- Add books and register users
- Borrow and return books with due dates (14 days)
- Calculates late fines automatically (Rs.2/day)
- Search by title or author
- View full transaction history

**How to run:**
```bash
cd library-management
mvn compile
mvn compile exec:java
```

**Sample output:**

```
========================================
   Welcome to Library Management System
========================================
1. Add Book
2. Register User
3. Borrow Book
4. Return Book
5. Search Books
6. View All Books
7. View All Users
8. View User Transaction History
9. View All Active Transactions
0. Exit
========================================
Enter your choice: 3

--- Borrow Book ---
Enter User ID: U001
Enter Book ISBN: 978-0-13-110362-7

Book borrowed successfully!
Transaction ID: a3f2c1d4-9e8b-4a7f-b2c1
Borrow Date:    2026-04-13
Due Date:       2026-04-27

Enter your choice: 9

--- Active Transactions ---
------------------------
Transaction ID : a3f2c1d4-9e8b-4a7f
Book           : The C Programming Language
User           : John Doe
Borrow Date    : 2026-04-13
Due Date       : 2026-04-27
Return Date    : Not returned yet
Fine           : Rs.0.0

Enter your choice: 4

--- Return Book ---
Enter User ID: U001
Enter Book ISBN: 978-0-13-110362-7

Book returned successfully! No fine.
```

**How I structured it:**

I split it into 5 layers — model, exceptions, repository, service, and UI.
The service layer handles all the rules like borrow limits and fine calculation.
The repository layer is just an interface, so if I wanted to swap from a HashMap
to a real database, I'd only change one file and nothing else breaks.

---

## 2. Smart Expense Tracker — Python

A CLI app to track daily expenses, view summaries, and generate charts.
I kept each file focused on one job so the code stays clean and easy to follow.

**Tools:** Python 3.11, matplotlib

**What it does:**
- Add expenses with date, amount, category, description
- Monthly summaries with highest and lowest month
- Category breakdown with percentage share
- Spending trend (month-over-month change)
- 5 types of charts

**How to run:**
```bash
cd expense_tracker
pip install matplotlib
python main.py
```

**Sample output:**

```
=======================================================
       SMART EXPENSE TRACKER WITH INSIGHTS
=======================================================
1.  Add New Expense
2.  View All Expenses
3.  View This Month's Expenses
4.  Monthly Summary
5.  Category Analysis
6.  Spending Insights
7.  Delete an Expense
8.  Charts & Visualizations
0.  Exit
-------------------------------------------------------
Enter your choice: 5

--- Category Analysis ---

  Total spending: Rs.12450.00

  CATEGORY        TRANSACTIONS        TOTAL      SHARE
  ----------------------------------------------------
  Transport                  5     Rs.4500.0     36.1%
  ##########
  Food                       8     Rs.3200.0     25.7%
  ######
  Shopping                   3     Rs.2800.0     22.5%
  ######
  Bills                      2     Rs.1950.0     15.7%
  ####

  Highest spending category: Transport (Rs.4500.00)

Enter your choice: 6

--- Spending Insights ---

  Total expenses recorded  : 18
  Total amount spent       : Rs.12450.00
  Average per transaction  : Rs.691.67
  Average daily spending   : Rs.1037.50

  Spending trend:
  2026-02: Rs.3800.00  ↑ 12.4% vs previous month
  2026-03: Rs.4250.00  ↑ 11.8% vs previous month
  2026-04: Rs.4400.00  ↑  3.5% vs previous month
```

**How I structured it:**

There are 7 files and each one does exactly one thing.
`storage.py` is the only file that reads or writes the CSV.
`insights.py` just does calculations — it never touches files.
`cli.py` just handles input and output — no logic in there.
This way each piece can change independently without breaking the others.

---

## 3. Online Retail Sales Analysis — SQL

A database project where I designed a retail schema and wrote analytical
queries to pull business insights from the data.

**Tools:** MySQL 8.0, MySQL Workbench

**Tables:** Customers, Products, Orders, Order_Items

**Queries I wrote:**
- Top 10 best selling products by quantity and revenue
- Most valuable customers by lifetime spend
- Monthly revenue trend
- Category-wise sales with percentage share
- Customers who haven't ordered in 6 months

**How to run:**
```
1. Open MySQL Workbench
2. Run retail_sales_database.sql — creates all tables and inserts data
3. Open queries.sql and run any query you want
```

**Sample output:**

```sql
-- Top 5 products by revenue

SELECT p.name, p.category,
       SUM(oi.quantity) AS total_sold,
       SUM(oi.quantity * oi.unit_price) AS total_revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_id
ORDER BY total_revenue DESC
LIMIT 5;

+---------------------------+-------------+------------+--------------+
| name                      | category    | total_sold | total_revenue|
+---------------------------+-------------+------------+--------------+
| Wireless Headphones       | Electronics |        142 |    284000.00 |
| Running Shoes             | Sports      |        198 |    237600.00 |
| Office Chair              | Furniture   |         67 |    201000.00 |
| Python Programming Book   | Education   |        312 |    156000.00 |
| Smartwatch Pro            | Electronics |         89 |    133500.00 |
+---------------------------+-------------+------------+--------------+
5 rows in set (0.04 sec)


-- Monthly revenue trend

SELECT YEAR(order_date) AS year,
       MONTH(order_date) AS month,
       SUM(total_amount) AS monthly_revenue
FROM orders
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY year, month;

+------+-------+-----------------+
| year | month | monthly_revenue |
+------+-------+-----------------+
| 2026 |     1 |       142500.00 |
| 2026 |     2 |       168200.00 |
| 2026 |     3 |       195400.00 |
| 2026 |     4 |       210800.00 |
+------+-------+-----------------+
4 rows in set (0.02 sec)
```

**How I designed it:**

The `Order_Items` table is the most important one analytically — it stores
one row per product per order, so you can calculate revenue and quantities
accurately. I stored `unit_price` there separately from `Products.price`
because prices change over time and old records need to show what the
customer actually paid, not today's price.

---

## What I picked up across all three

Every project kept pushing me back to the same idea — keep each piece
doing one job. A Java class, a Python file, a SQL table — things get messy
fast when one thing tries to do too much. Naming things clearly and
separating responsibilities made debugging a lot easier than I expected.

---

## Folder structure

```
mini_vir/
├── library-management/     Java project
├── expense_tracker/        Python project
└── retail-sales-sql/       SQL scripts
```

---

*Akshay — April 2026*
