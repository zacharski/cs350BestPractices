# Best Practices
1. Code that is database specfic should be in a separate file (as should be configuration code).
2. Use try except blocks
3. Dispose of old cursors as soon as the data is not required anymore
Call Close on them.
4. Keep connections open as long as required.
Creating connections can be slow so it is best practice to keep them open as long as required.
5. Rollback or commit frequently
6. Warning. 
Never, never, NEVER use Python string concatenation (+) or string parameters interpolation (%) to pass variables to a SQL query string. Not even at gunpoint. So if,  
   `user = 'ann'`
   then
	`query = 'select * from users where name = %s' % user`
	and 
	`query = "select * from users where name = '" + user  + "'"`
	ARE NOT GOOD
7. Never, never never store passwords (or password-like data) in the clear. Not even at gunpoint.
8. It is an incredibly bad idea to store credit card information in a database. (unless you are a humongous company that can do it right). Always use a payment gateway/vendor.
9. When you create passwords for Postgresql users (among others) always use real passwords vs. *password*, *12345*, etc.