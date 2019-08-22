SELECT
    s.Score, (
    SELECT COUNT(DISTINCT Score) 
    FROM Scores t
    WHERE t.Score >= s.Score
    ) as Rank
FROM Scores s
ORDER BY Score DESC


SELECT s.Score, r.Rank
FROM Scores s JOIN (
    SELECT Score, @row_number:=@row_number+1 AS Rank
    FROM
        (SELECT Score From Scores GROUP BY Score ORDER BY Score DESC) s,
        (SELECT @row_number:=0) t
    ) as r USING(Score)
ORDER BY Score DESC
