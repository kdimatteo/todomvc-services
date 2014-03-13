Python basedREST API for TodoMVC
================================
Most basic functioality possible, useful for testing online/offline synchronization.

- Uses sqlite3 for simplicity (no need to spin up mySQL)
- CORS compliant for flexibility
- Requires POSTs to be of content-type application/json
- Probably needs some cleanup :)

Use
---
1. Create the db by running ```python create-table.py```
2. Start the server ```python server.py```
3. Your end-point is ```http://localhost:5000/api/todos```

Dependencies
------------
[Flask](http://flask.pocoo.org/)
