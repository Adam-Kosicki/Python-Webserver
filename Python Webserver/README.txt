IDE Used:
PyCharm CE

How to run:
1. Open PyCharm and import Webserver.py
2. Run Webserver (green arrow)
3. “Listening on port 8080 …” should be shown in console
4. Open Google Chrome and type into address bar, “http://localhost:8080/…” where … is the file name

For example:
If I have a file named test.html in the same directory (folder) as Webserver.py, I would type “http://localhost:8080/test.html” into the address bar in Chrome.

This code sets up a simple HTTP server. It listens on IP address '0.0.0.0' and port 8080. 
When a connection is received, it reads the incoming HTTP request, extracts the requested file, 
tries to open and read it. If the file exists, it sends a 200 OK response with the file's content; 
if not, it responds with a 404 NOT FOUND message.