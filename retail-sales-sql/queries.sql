create database retail_sales_db;
use retail_sales_db;

create table Customers(
customer_id int auto_increment not null primary key,
first_name varchar(50) not null,
last_name varchar(50) not null,
email varchar(50) not null,
city varchar(50),
country varchar(50),
registration_date date not null
);
describe Customers;

create table products(
product_id int auto_increment not null primary key,
product_name varchar(50) not null,
category varchar(50) not null,
price varchar(50) not null,
stock_quantity varchar(50) not null default 0
);
describe products;

create table orders(
order_id int auto_increment not null primary key,
customer_id int not null,
order_date date not null,
status varchar(50) not null default "pending",
total_amount decimal(10,2) not null,
foreign key(customer_id) references customers(customer_id)
); 
describe orders;

create table order_items(
item_id int not null auto_increment primary key,
order_id int not null,
product_id int not null,
quantity int not null,
unit_price int not null,
foreign key(order_id) references orders(order_id),
foreign key(product_id) references products(product_id)
);
describe order_items;
select * from order_items;

show tables;

/*1.Top Selling Products*/
select 
    p.product_id,
    p.product_name,
    sum(oi.quantity) as total_quantity_sold
from order_items oi
join products p 
    on oi.product_id = p.product_id
group by 
    p.product_id, p.product_name
order by 
    total_quantity_sold desc
limit 5;

/*2.Most Valuable Customers*/
select
    c.customer_id,
    c.first_name,
    c.last_name,
    sum(o.total_amount) as total_spent
from orders o
join customers c 
    on o.customer_id = c.customer_id
where o.status = 'delivered'
group by
    c.customer_id, c.first_name
order by 
    total_spent desc
limit 5;

/*3.Monthly Revenue Calculation*/
select 
    extract(year from o.order_date) as year,
    extract(month from o.order_date) as month,
    sum(o.total_amount) AS monthly_revenue
from orders o
where o.status = 'delivered'
group by 
    extract(year from o.order_date),
    extract(month from o.order_date)
order by
    year asc,
    month asc;

/*4.Category-Wise Sales Analysis*/
select 
    p.category,
    sum(oi.quantity) as total_units_sold,
    sum(oi.quantity * oi.unit_price) as total_revenue
from order_items oi
join products p 
    on oi.product_id = p.product_id
join orders o 
    on oi.order_id = o.order_id
where o.status = 'delivered'
group by 
    p.category
order by 
    total_revenue desc;

/*5.Detect Inactive Customers*/
select 
    c.customer_id,
    c.first_name,
    c.last_name,
    o.order_date
from customers c
left join orders o 
    on c.customer_id = o.customer_id
where 
    o.order_date < date_sub(curdate(), interval 6 month)
    or o.order_date is null;




