-- Optimize table
OPTIMIZE gold_user_metrics;

-- Sample query
SELECT user_id, COUNT(*) AS events
FROM gold_user_metrics
GROUP BY user_id;