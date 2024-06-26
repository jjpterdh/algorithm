SELECT
    ID,
    
    FISH_NAME,
    LENGTH
    FROM FISH_INFO F 
JOIN FISH_NAME_INFO NI ON F.FISH_TYPE=NI.FISH_TYPE
WHERE F.FISH_TYPE IN (
    SELECT FISH_TYPE
    FROM FISH_INFO
    GROUP BY FISH_TYPE
    HAVING LENGTH=MAX(LENGTH)
)
ORDER BY ID;