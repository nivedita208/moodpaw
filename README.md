## Cat Mood Tracker

Track my cat's daily moods

#### License

MIT

### What does frappe.db.sql() do?
##### In Frappe, the method frappe.db.sql() is used to run raw SQL queries directly on the database.
## Syntax:
``` 
frappe.db.sql(query, values=None, as_dict=False)

```
Example:
```
data = frappe.db.sql(
    "SELECT name, email FROM tabUser WHERE enabled = %s",
    (1,),
    as_dict=True
)
```
#### Parameters:
| Parameter | Meaning                                                               |
|-----------|------------------------------------------------------------------------|
| `query`   | The raw SQL query string (can use placeholders `%s`)                  |
| `values`  | A tuple of values to safely pass into the query (`%s` placeholders)   |
| `as_dict` | If `True`, returns list of dicts. If `False`, returns list of tuples. |


### Output:
If as_dict=True:
```
[{'name': 'Administrator', 'email': 'admin@example.com'}, {...}]
```
If as_dict=False:
```
[('Administrator', 'admin@example.com'), (...)]
```
### Use Case:
Use frappe.db.sql() only when you really need raw SQL.

For normal queries, use Frappe ORM like frappe.get_all() or frappe.get_doc() — they’re safer and easier.

### When to use frappe.db.sql()?
Use it when:

You need complex joins, GROUP BY, or aggregate logic.

You want to execute non-standard queries not supported by Frappe ORM.

### Important Note:
Always use %s placeholders (never string formatting like f"...{x}...") to avoid SQL injection.

```
frappe.db.sql("SELECT * FROM tabItem WHERE item_code = %s", (item_code,))
```
