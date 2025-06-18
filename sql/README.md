# [🛒 Retail](https://github.com/Furkat-github/analyst_portfolio/blob/main/sql/retail_sales_analysis.sql): Анализ продаж в PostgreSQL

## 📌 Описание  
Проект посвящён анализу розничных продаж на основе данных из CSV, загруженных в базу данных PostgreSQL.  
Выполнен с использованием чистого SQL: расчёт выручки, возвратов, определение топовых товаров и ключевых показателей.

---

## 📁 Файлы проекта  
- [`Retail_sales_data.csv`](https://github.com/Furkat-github/analyst_portfolio/blob/main/sql/Retail_sales_data.csv) — исходный датасет  
- [`retail_sales_analysis.sql`](https://github.com/Furkat-github/analyst_portfolio/blob/main/sql/retail_sales_analysis.sql) — файл с SQL-запросами  
- [`retail_sales_results`](https://github.com/Furkat-github/analyst_portfolio/tree/main/sql/retail_sales_results) — папка с выгруженными результатами запросов  

---

## 📊 Основные результаты

### 📈 Выручка по дням  

| Дата        | Выручка (сум) |
|:------------|:----------------|
| 2024-07-12  | 1 658 120 |
| 2024-07-13  | 1 761 330 |
| 2024-07-14  | 1 831 570 |
| ... | ... |
| 2024-09-10  | 4 001 110 |

📄 Полный файл с выручкой по дням: [`results/daily_revenue.csv`](https://github.com/Furkat-github/analyst_portfolio/blob/main/sql/retail_sales_results/%D0%92%D1%8B%D1%80%D1%83%D1%87%D0%BA%D0%B0%20%D0%BF%D0%BE%20%D0%B4%D0%BD%D1%8F%D0%BC.csv)

---

### 🥛 Топ-5 товаров по объёму продаж  

| Товар                     | Продано (шт) |
|:----------------------------|:----------------|
| Сметана 400 гр, 20%        | 1355 |
| Сметана 200 гр, 20%        | 1064 |
| Каймак 200 гр, 45%         | 699  |
| Каймак 400 гр, 45%         | 687  |
| Сметана 400 гр, 15%        | 674  |

📄 Полный файл: [`results/top_5_products.csv`](https://github.com/Furkat-github/analyst_portfolio/blob/main/sql/retail_sales_results/%D0%A2%D0%BE%D0%BF%205%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B2%D0%B0%D0%B5%D0%BC%D1%8B%D1%85%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%BE%D0%B2.csv)

---

### 📉 Доля возвратов  

| Возвратов | Продано | Доля возвратов (%) |
|:--------------|:------------|:----------------|
| 116 | 11 658 | 0,99 |

---

### 💵 Средняя стоимость позиции  

**13 795,09 сум**

---

## 📌 Выводы  

Анализ позволил:
- Определить динамику выручки за каждый день продаж.
- Выявить самые популярные товары (лидер — Сметана 400 гр, 20%).
- Посчитать долю возвратов, которая оказалась крайне низкой (менее 1%).
- Определить среднюю цену проданного товара.

---

## 🛠 Используемые инструменты  

- PostgreSQL 16  
- PgAdmin 4  
- CSV  
