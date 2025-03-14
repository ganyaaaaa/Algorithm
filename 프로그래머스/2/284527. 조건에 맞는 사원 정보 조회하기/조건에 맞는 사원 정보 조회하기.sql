SELECT 
    T.SCORE,
    T.EMP_NO,
    HR_EMPLOYEES.EMP_NAME,
    HR_EMPLOYEES.POSITION,
    HR_EMPLOYEES.EMAIL
FROM (
    SELECT 
        HR_GRADE.EMP_NO,
        SUM(HR_GRADE.SCORE) AS SCORE
    FROM 
        HR_GRADE
    GROUP BY 
        HR_GRADE.EMP_NO
    ORDER BY 
        SCORE DESC
    LIMIT 1
) AS T
LEFT JOIN HR_EMPLOYEES ON T.EMP_NO = HR_EMPLOYEES.EMP_NO;
