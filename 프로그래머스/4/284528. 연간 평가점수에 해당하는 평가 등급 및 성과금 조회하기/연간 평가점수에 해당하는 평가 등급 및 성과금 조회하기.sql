SELECT 
    e.EMP_NO,
    e.EMP_NAME,
    CASE
        WHEN SUM(g.SCORE)/2 >= 96 THEN "S"
        WHEN SUM(g.SCORE)/2 >= 90 THEN "A"
        WHEN SUM(g.SCORE)/2 >= 80 THEN "B"
        ELSE "C"
    END AS 'GRADE',
    CASE 
    WHEN SUM(g.SCORE)/2 >= 96 THEN e.SAL * 0.2
        WHEN SUM(g.SCORE)/2 >= 90 THEN e.SAL * 0.15
        WHEN SUM(g.SCORE)/2 >= 80 THEN e.SAL * 0.1
        ELSE 0
    END AS 'BONUS'
FROM HR_EMPLOYEES e JOIN HR_GRADE g
    ON e.EMP_NO = g.EMP_NO
GROUP BY e.EMP_NO