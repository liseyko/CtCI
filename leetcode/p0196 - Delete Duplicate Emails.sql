DELETE p1 FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id

#DELETE p1 FROM Person as p1 join Person as p2 on p1.id > p2.id and p1.email = p2.email
