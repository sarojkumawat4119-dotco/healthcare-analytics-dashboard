-- Healthcare Analytics Dashboard - SQL Queries
-- Author: Saroj Kumawat

USE healthcare_analytics;

-- 1. Total number of patients
SELECT COUNT(*) AS total_patients FROM healthcare;

-- 2. Most common medical conditions
SELECT medical_condition, COUNT(*) AS total_cases
FROM healthcare
GROUP BY medical_condition
ORDER BY total_cases DESC;

-- 3. Gender distribution
SELECT gender, COUNT(*) AS count
FROM healthcare
GROUP BY gender;

-- 4. Average age by medical condition
SELECT medical_condition, ROUND(AVG(age), 1) AS avg_age
FROM healthcare
GROUP BY medical_condition
ORDER BY avg_age DESC;

-- 5. Top 5 hospitals by patient count
SELECT hospital, COUNT(*) AS total_patients
FROM healthcare
GROUP BY hospital
ORDER BY total_patients DESC
LIMIT 5;

-- 6. Average billing amount by hospital
SELECT hospital, ROUND(AVG(billing_amount), 2) AS avg_billing
FROM healthcare
GROUP BY hospital
ORDER BY avg_billing DESC
LIMIT 10;

-- 7. Insurance provider distribution
SELECT insurance_provider, COUNT(*) AS total_patients
FROM healthcare
GROUP BY insurance_provider
ORDER BY total_patients DESC;

-- 8. Admission type breakdown
SELECT admission_type, COUNT(*) AS count
FROM healthcare
GROUP BY admission_type;

-- 9. Most prescribed medications
SELECT medication, COUNT(*) AS times_prescribed
FROM healthcare
GROUP BY medication
ORDER BY times_prescribed DESC;

-- 10. Test results distribution
SELECT test_results, COUNT(*) AS count
FROM healthcare
GROUP BY test_results;

-- 11. Average length of stay by medical condition
SELECT medical_condition, ROUND(AVG(length_of_stay), 1) AS avg_stay_days
FROM healthcare
GROUP BY medical_condition
ORDER BY avg_stay_days DESC;

-- 12. Blood type distribution
SELECT blood_type, COUNT(*) AS count
FROM healthcare
GROUP BY blood_type
ORDER BY count DESC;

-- 13. Most active doctors by patient count
SELECT doctor, COUNT(*) AS patients_treated
FROM healthcare
GROUP BY doctor
ORDER BY patients_treated DESC
LIMIT 10;

-- 14. Average billing by admission type
SELECT admission_type, ROUND(AVG(billing_amount), 2) AS avg_billing
FROM healthcare
GROUP BY admission_type;

-- 15. Patients aged above 60 by condition
SELECT medical_condition, COUNT(*) AS senior_patients
FROM healthcare
WHERE age > 60
GROUP BY medical_condition
ORDER BY senior_patients DESC;

-- 16. Yearly patient admissions trend
SELECT YEAR(date_of_admission) AS year, COUNT(*) AS admissions
FROM healthcare
GROUP BY year
ORDER BY year;

-- 17. High billing cases above 40000
SELECT name, medical_condition, hospital, billing_amount
FROM healthcare
WHERE billing_amount > 40000
ORDER BY billing_amount DESC
LIMIT 10;

-- 18. Average stay by admission type
SELECT admission_type, ROUND(AVG(length_of_stay), 1) AS avg_days
FROM healthcare
GROUP BY admission_type;

-- 19. Medical condition vs test results
SELECT medical_condition, test_results, COUNT(*) AS count
FROM healthcare
GROUP BY medical_condition, test_results
ORDER BY medical_condition, count DESC;

-- 20. Monthly admission trends
SELECT DATE_FORMAT(date_of_admission, '%Y-%m') AS month,
COUNT(*) AS admissions
FROM healthcare
GROUP BY month
ORDER BY month;
