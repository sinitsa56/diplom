### Проверка отображения созданного заказа в базе даных:
```
SELECT c.login,
              COUNT(o."inDelivery")
FROM "Couriers" AS c
LEFT OUTER JOIN "Orders" AS o ON c.id=o."courierId"
GROUP BY c.login, o."inDelivery"
HAVING o."inDelivery"=true;
```

### Проверка корректного отображения статусов заказав базе даных
```
SELECT track, 
         CASE
               WHEN finished=true THEN 2
               WHEN cancelled=true THEN -1
               WHEN "inDelivery"=true THEN 1
               ELSE 0
         END
FROM "Orders";
```
