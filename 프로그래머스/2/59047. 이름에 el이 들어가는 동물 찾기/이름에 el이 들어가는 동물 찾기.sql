-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME like '%EL%'
    and NAME like '%el%'
    and ANIMAL_TYPE in ('Dog')
ORDER BY NAME, ANIMAL_ID