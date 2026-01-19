INSERT INTO customers(full_name,email)
VALUES
  ('Ada Lovelace','ada@example.com'),
  ('Grace Hopper','grace@example.com')
ON CONFLICT (email) DO NOTHING;

INSERT INTO orders(customer_id, amount)
SELECT customer_id, 49.99 FROM customers WHERE email='ada@example.com'
UNION ALL
SELECT customer_id, 29.99 FROM customers WHERE email='grace@example.com';
