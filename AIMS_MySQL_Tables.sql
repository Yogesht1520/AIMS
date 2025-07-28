
-- AIMS Project MySQL Table Creation Script

CREATE DATABASE IF NOT EXISTS aims_db;
USE aims_db;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    role ENUM('admin', 'analyst'),
    password_hash VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS incidents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    severity ENUM('low', 'medium', 'high'),
    status ENUM('open', 'contained', 'resolved') DEFAULT 'open',
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    system_name VARCHAR(100),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    threat_type VARCHAR(100),
    ai_score FLOAT
);

CREATE TABLE IF NOT EXISTS responses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    incident_id INT,
    action_taken TEXT,
    responder VARCHAR(100),
    response_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (incident_id) REFERENCES incidents(id) ON DELETE CASCADE
);
