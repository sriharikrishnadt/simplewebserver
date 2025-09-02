from http.server import HTTPServer,BaseHTTPRequestHandler
content='''
<!doctype html>
<html>
    <head>
      <title> My Web Server</title>
    </head>
    <body>
        <table border="1" align="center" cellpadding="10" bgcolor="pink" >
        <caption><h1>List Of Protocols in TCP/IP Protocol Suite</h1></caption>
        <tr>
            <th>S.No.</th><th>Name Of The Layer</th><th>Name of The Protocol</th>
        </tr>
        <tr>
            <td>1.</td><td>Application Layer</td><td>HTTP,FTP,DNS,TELNET & SSH</td>
        </tr>
        <tr>
            <td>2.</td><td>Transport Layer</td><td>TCP & UDP</td>
        </tr>
        <tr>
            <td>3.</td><td>Network Layer</td><td>IPV4/IPV6</td>
        </tr>
        <tr>
            <td>4.</td><td>Link Layer</td><td>Ethernet</td>
        </tr>
        </table>
    </body>
</html>'''


    
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver")
server_address=('',8000)
httpd=HTTPServer(server_address,MyServer)
httpd.serve_forever()