SELECT s.Score, r.Rank
FROM Scores s JOIN (
    SELECT Score, @row_number:=@row_number+1 AS Rank
    FROM
        (SELECT Score From Scores GROUP BY Score ORDER BY Score DESC) s,
        (SELECT @row_number:=0) t
    ) as r USING(Score)
ORDER BY Score DESC
