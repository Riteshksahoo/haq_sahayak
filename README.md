# HAQ SAHAYAK

## Overview

HAQ SAHAYAK is an AI-powered citizen service assistance platform designed to simplify access to government services and improve transparency in public service delivery.

Citizens often struggle to understand government procedures, required documents, service timelines, and application status updates. This project aims to address these challenges by providing a centralized platform where citizens can access service information, submit applications, track progress, receive notifications, and interact with an intelligent assistant.

The project is built using Snowflake as the core data platform and leverages Snowpark, Streams, Tasks, Stored Procedures, and Streamlit to simulate a real-world citizen service ecosystem.

---

## Problem Statement

Citizens frequently face challenges such as:

* Lack of awareness about government services
* Difficulty understanding required documents
* Delayed application tracking
* Limited transparency in processing timelines
* Lack of proactive notifications
* Complex service procedures

HAQ SAHAYAK aims to bridge this gap by creating a digital citizen assistance platform powered by modern data engineering and analytics technologies.

---

## Project Objectives

* Centralize government service information
* Track citizen applications efficiently
* Automate service event monitoring
* Generate actionable analytics
* Provide intelligent service guidance
* Improve transparency and citizen experience

---

## Technology Stack

### Data Platform

* Snowflake
* Snowpark (Python)

### Database Objects

* Tables
* Views
* Streams
* Tasks
* Stored Procedures

### Data Ingestion

* CSV File Loading
* JSON File Loading
* Snowpipe Testing

### Frontend

* Streamlit

### APIs & Integrations

- Gemini API
- Pincode API
- Holiday API

### Programming Language

* Python

### Version Control

* Git
* GitHub

---

## Data Architecture

The project follows a layered data architecture.

### STAGING Layer

Stores incoming files before processing.

### RAW Layer

Stores original source files such as CSV and JSON datasets.

### CURATED Layer

Contains cleaned and business-ready datasets.

### ANALYTICS Layer

Contains reporting views and dashboard-ready datasets.

Architecture Flow:

Citizen Application

→ Streamlit

→ Snowflake Tables

→ Streams

→ Tasks

→ Stored Procedures

→ Event Logs

→ Analytics Views

→ Dashboard

---

## Core Features

### Service Information Management

Stores information about government services, legal timelines, required documents, offices, and process guidance.

### Application Tracking

Tracks citizen applications throughout the service lifecycle.

### Notification Management

Maintains notification records and status updates.

### Event-Driven Automation

Uses Snowflake Streams, Tasks, and Stored Procedures to automatically monitor and log application events.

### Analytics Layer

Provides analytical views for:

* Service performance
* User activity analysis
* Notification summaries
* Application tracking
* Dashboard reporting

### Semi-Structured Data Processing

Uses Snowflake VARIANT columns to process JSON-based service rules, application documents, notifications, and user activity logs.

---

## Database Design

The solution contains 21+ business tables covering:

* States
* Districts
* Offices
* Government Processes
* Legal Limits
* Required Documents
* Service Categories
* Citizen Applications
* Notifications
* Complaints
* User Activity Logs
* Service Rules
* Application Documents

Foreign key relationships are implemented to maintain data integrity across the platform.

---

## Snowflake Features Implemented

### Data Loading

* CSV File Format
* JSON File Format
* Internal Stages
* COPY INTO Operations

### Data Transformation

* Views
* Aggregations
* Joins
* Variant Data Handling

### Change Data Capture

* Streams

### Automation

* Tasks
* Stored Procedures

### Analytics

* Dashboard Views
* User Activity Analysis
* Application Tracking Views

### Snowpark

* Python-based data access
* DataFrame operations
* Aggregations
* Joins

---

## Repository Structure

sql/

* ddl/
* dml/
* views/
* streams/
* procedures/
* tasks/

app/

* Home.py
* pages/

haq_sahayak_snowpark/

* snowpark_test.py

data/

* raw/

docs/

* project documentation

---

## Future Enhancements

The following enhancements are planned for upcoming development phases:

### Application Layer

* Streamlit-based Citizen Service Portal
* Application Submission Workflow
* Application Tracking Interface
* Notification Management Dashboard

### AI & API Integrations

* Gemini AI-powered Citizen Assistant
* Pincode API for automatic district and state identification
* Holiday API for service timeline calculations

### Data Engineering Enhancements

* dbt Integration
* Apache Airflow Orchestration
* Data Quality Validation Framework

### Production Readiness

* CI/CD Pipeline
* Role-Based Access Control (RBAC)
* Monitoring and Alerting


## Learning Outcomes

This project demonstrates practical implementation of:

* Data Warehousing
* Data Modeling
* Snowflake Architecture
* Snowpark Development
* Change Data Capture
* Event-Driven Automation
* Semi-Structured Data Processing
* Analytics Engineering
* API Integration
* End-to-End Application Development

---

## Author

Ritesh Kumar Sahoo

