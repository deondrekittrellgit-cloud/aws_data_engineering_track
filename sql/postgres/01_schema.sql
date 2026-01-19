-- Minimal starter schema for the DE track

CREATE TABLE IF NOT EXISTS healthcheck (
  id SERIAL PRIMARY KEY,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS customers (
  customer_id SERIAL PRIMARY KEY,
  full_name TEXT NOT NULL,
  email TEXT UNIQUE,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS orders (
  order_id SERIAL PRIMARY KEY,
  customer_id INT NOT NULL REFERENCES customers(customer_id),
  amount NUMERIC(12,2) NOT NULL CHECK (amount >= 0),
  order_ts TIMESTAMPTZ NOT NULL DEFAULT now()
);
