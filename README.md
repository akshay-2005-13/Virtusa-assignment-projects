# Virtusa Assignment Projects

Three projects built from scratch covering Java, Python, and SQL.
Each project demonstrates core programming concepts and clean architecture.

---

## Project 1 — Library Management System (Java)

A command-line Library Management System built with Java OOP principles
and a clean layered architecture.

### Tech Stack
- Java 17
- Maven (build tool)

### OOP Concepts Applied
- **Encapsulation** — all model fields are private with controlled access via getters/setters
- **Inheritance** — all custom exceptions extend a base `LibraryException` class
- **Abstraction** — Repository interfaces define contracts; implementations can be swapped without changing business logic
- **Dependency Injection** — service layer receives repositories via constructor

### Architecture

```
library-management/
├── model/           → Book, User, Transaction classes
├── repository/      → Interfaces + InMemory implementations
│   └── impl/        → InMemoryBookRepository, InMemoryUserRepository, InMemoryTransactionRepository
├── service/         → Business logic (borrow, return, fine calculation)
├── exception/       → Custom exception hierarchy
│   ├── LibraryException.java
│   ├── BookNotFoundException.java
│   ├── UserNotFoundException.java
│   ├── BookNotAvailableException.java
│   └── MaxBorrowLimitException.java
└── ui/              → CLI menu system
```

### Features
- Add and manage books with copy tracking
- Register library users with borrow limit enforcement (max 3 books)
- Borrow and return books with automatic due date (14 days)
- Automatic late fine calculation (Rs.2 per day after due date)
- Search books by title or author
- View all users and their borrowed books
- Full transaction history per user
- View all active (unreturned) transactions

### How to Run

```bash
cd library-management
mvn compile
mvn compile exec:java
```

### Key Design Decisions

| Decision | Reason |
|----------|--------|
| `HashMap<String, Book>` for storage | O(1) ISBN lookup regardless of library size |
| `unit_price` stored in `Transaction` | Preserves historical price at time of borrowing |
| Repository as interface | Allows swapping to a real database without changing service layer |
| `Optional<T>` return type | Forces callers to handle "not found" case explicitly, prevents NullPointerException |
| Custom exception per scenario | Caller knows exactly what went wrong — BookNotFound vs BookNotAvailable |

### Sample Output

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
```

---

## Project 2 — Smart Expense Tracker with Insights (Python)

A CLI-based expense tracking application with a full analytics engine
and matplotlib visualizations — built with clean module separation.

### Tech Stack
- Python 3.11
- matplotlib (charts and visualizations)
- csv — built-in (data persistence)
- datetime — built-in (date handling)

### Python Concepts Applied
- **OOP** — `Expense` class with `@classmethod`, `__str__`, and `__init__`
- **File I/O** — `csv.writer` for writing, `csv.DictReader` for reading
- **Lambda functions** — used with `max()`, `min()`, `sorted()`
- **Exception handling** — `try/except` on all user inputs, never crashes
- **Set operations** — used for unique date counting in daily averages
- **Separation of concerns** — each module has exactly one responsibility

### Project Structure

```
expense_tracker/
├── main.py          → Entry point (2 lines)
├── expense.py       → Expense data class
├── storage.py       → CSV read/write layer
├── tracker.py       → Business logic and validation
├── insights.py      → Analytics engine
├── visualizer.py    → matplotlib charts (5 chart types)
├── cli.py           → CLI menu and user interaction
└── data/
    └── expenses.csv → Persistent data storage
```

### Features
- Add expenses with date, amount, category, and description
- View all expenses with running total
- View current month expenses automatically
- Monthly summary with highest and lowest month detection
- Category breakdown with percentage share and transaction count
- Spending insights — averages, extremes, month-over-month trend
- Delete expenses with confirmation prompt
- 5 chart types via matplotlib

### Chart Types

| Chart | What it shows |
|-------|---------------|
| Category Pie Chart | Proportional spending per category |
| Monthly Bar Chart | Total spend per month, highlights highest |
| Category Bar Chart | Bar for amount + line for transaction count |
| Spending Trend Line | Month-over-month trend with fill area |
| Daily Spending Chart | Day-by-day bars with average line overlay |

### How to Run

```bash
cd expense_tracker
pip install matplotlib
python main.py
```

### Key Design Decisions

| Decision | Reason |
|----------|--------|
| CSV over JSON | Data is tabular with fixed fields — CSV is ideal |
| `storage.py` is the only file touching CSV | If storage changes, nothing else breaks |
| `from_dict()` as `@classmethod` | Creates objects from CSV rows without needing an existing instance |
| `CATEGORIES` as class variable | Accessible everywhere as `Expense.CATEGORIES` without creating an object |
| Input validation loops | User is never shown a crash — they always get a retry prompt |

### Sample Output

```
=======================================================
       SMART EXPENSE TRACKER WITH INSIGHTS
=======================================================

--- Category Analysis ---

  Total spending: Rs.12450.00

  CATEGORY        TRANSACTIONS        TOTAL    SHARE
  ----------------------------------------------------
  Food                       8    Rs.3200.0    25.7%
  ####
  Transport                  5    Rs.4500.0    36.1%
  #######
  Shopping                   3    Rs.2800.0    22.5%
  ####
```

---

## Project 3 — Online Retail Sales Analysis (SQL)

A relational database project for analyzing retail sales data
using real-world analytical SQL queries.

### Tech Stack
- SQL (MySQL / SQLite)
- DDL — CREATE TABLE, constraints, foreign keys
- DML — INSERT, SELECT with joins and aggregations

### Database Schema

```
Customers
├── customer_id   INT PRIMARY KEY AUTO_INCREMENT
├── name          VARCHAR(100)
├── email         VARCHAR(100) UNIQUE
├── city          VARCHAR(100)
└── join_date     DATE

Products
├── product_id    INT PRIMARY KEY AUTO_INCREMENT
├── name          VARCHAR(100)
├── category      VARCHAR(50)
├── price         DECIMAL(10,2)
└── stock_qty     INT

Orders
├── order_id      INT PRIMARY KEY AUTO_INCREMENT
├── customer_id   INT FOREIGN KEY → Customers
├── order_date    DATE
├── status        VARCHAR(20)
└── total_amount  DECIMAL(10,2)

Order_Items
├── item_id       INT PRIMARY KEY AUTO_INCREMENT
├── order_id      INT FOREIGN KEY → Orders
├── product_id    INT FOREIGN KEY → Products
├── quantity      INT
└── unit_price    DECIMAL(10,2)
```

### Table Relationships

```
Customers (1) ──────── (N) Orders
Orders    (1) ──────── (N) Order_Items
Products  (1) ──────── (N) Order_Items
```

### SQL Concepts Applied

| Concept | Where Used |
|---------|-----------|
| `INNER JOIN` | Linking orders to customers and products |
| `LEFT JOIN` | Finding customers with no recent orders |
| `GROUP BY` | Monthly revenue, category totals |
| `HAVING` | Filtering groups (e.g. categories over Rs.10,000) |
| `SUM`, `COUNT`, `AVG` | Revenue totals, transaction counts |
| `MAX`, `MIN` | Highest/lowest spending months |
| Subqueries | Inactive customer detection with `NOT IN` |
| `YEAR()`, `MONTH()` | Extracting date parts for monthly grouping |

### Analytical Queries Built

- Top 10 selling products by quantity sold and total revenue
- Most valuable customers ranked by lifetime spend
- Monthly revenue trend (grouped by year and month)
- Category-wise sales breakdown with percentage of total
- Inactive customer detection (no orders in last 6 months)
- Average order value per customer
- Products never ordered (using LEFT JOIN + NULL check)

### Key Design Decisions

| Decision | Reason |
|----------|--------|
| `unit_price` in `Order_Items` | Product price can change — historical price must be preserved |
| `DECIMAL(10,2)` for money | `FLOAT` has rounding errors — never use for currency |
| `Order_Items` separate from `Orders` | One order can have many products — required for First Normal Form (1NF) |
| `email UNIQUE` in Customers | Prevents duplicate registrations |
| Foreign keys on all relationships | Database enforces referential integrity automatically |

---

## Tools Used Across All Projects

| Tool | Purpose |
|------|---------|
| VSCode | Code editor for all three projects |
| Git + GitHub | Version control and portfolio hosting |
| Java 17 | Object-oriented backend project |
| Maven | Java build and dependency management |
| Python 3.11 | Scripting and data analysis project |
| matplotlib | Python chart generation |
| SQL | Relational database and analytics |

## Skills Demonstrated

- Object-Oriented Programming (Java and Python)
- Layered architecture and separation of concerns
- Data persistence — CSV files and SQL relational database
- Data analysis and visualization
- CLI application design with input validation
- Exception handling and defensive programming
- Git version control

---

## How to Run Each Project

```bash
# Java — Library Management System
cd library-management
mvn compile
mvn compile exec:java

# Python — Smart Expense Tracker
cd expense_tracker
pip install matplotlib
python main.py

# SQL — Retail Sales Analysis
# Open your SQL client (MySQL Workbench / DB Browser for SQLite)
# Run the .sql files in order: schema → data → queries
```

---
