# Food Orders Processing System

## 📌 Overview

**Food Orders Processing System** is a streaming-based project for processing and analyzing food order data.

The system cleans the data using Python, streams records through Kafka, processes them using Spark Structured Streaming, stores the processed data in Parquet and MySQL, and performs analytics using SQL.

> The dataset is historical, so Kafka is used to simulate real-time streaming.

## 🏗️ Architecture

```text
Food Order Dataset
        ↓
Python Cleaning
        ↓
      Kafka
        ↓
Spark Structured Streaming
        ↓
   ┌────┴─────┐
   ↓          ↓
Parquet     MySQL
               ↓
          SQL Analytics
```

## 🛠️ Technologies

* Python
* Apache Kafka
* Apache Spark
* Parquet
* MySQL
* SQL
* Docker

## 📊 Dataset

The dataset contains **41,953 food order records** with information about:

* Delivery persons
* Locations
* Weather
* Traffic
* Vehicle type
* Order type
* Festivals
* Delivery time

## 🔄 Processing

### 1. Data Cleaning

Python is used to handle missing values, clean text fields, and convert columns into appropriate data types.

### 2. Streaming

Cleaned records are published to the Kafka topic:

```text
food_orders
```

### 3. Processing & Storage

Spark Structured Streaming processes the Kafka records and stores the processed data in Parquet.

The data is also loaded into the MySQL database:

```text
Database: food_delivery
Table: food_orders
```

### 4. Analytics

SQL is used to analyze delivery time based on:

* City
* Traffic density
* Weather
* Vehicle type
* Festival
* Multiple deliveries
* Order type


## 🎯 Outcome

Successfully processed **41,953 records** through the complete flow:

**Python → Kafka → Spark → Parquet → MySQL → SQL Analytics**

## 🚀 Future Improvements

* Apache Airflow orchestration
* AWS S3 integration
* Data quality checks
* Analytics dashboard
