# Cleaning up imported data

 PosgreSQL queries were used to cleanup repetitive view data, since the relational model, while valuable for this approach, created repetitive entries that were either considered redundant or not useful in model training.

### Identify Duplicate Views

```
SELECT
    targetentityid,
    event,
    COUNT( targetentityid )
FROM
    pio_event_2
WHERE
    Event='view'
GROUP BY
    targetentityid,
    entityid,
    event,
    entitytype
HAVING
    COUNT( targetentityid )> 1
ORDER BY
    targetentityid,
    entityid,
    event;
```


### De-Duplicate views

```
DELETE FROM pio_event_2 
WHERE id IN
    (SELECT id
    FROM 
        (SELECT id,
         ROW_NUMBER() OVER( PARTITION BY targetentityid, entityid,
         event
        ORDER BY  id ) AS row_num
        FROM pio_event_2 WHERE event='view') t
        WHERE t.row_num > 1 );
```


