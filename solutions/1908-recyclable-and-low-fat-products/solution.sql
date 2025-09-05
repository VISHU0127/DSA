# Write your MySQL query statement below

/*
Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     | PRIMARY KEY
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
*/
SELECT product_id from products where low_fats = 'Y' and recyclable = 'Y';
