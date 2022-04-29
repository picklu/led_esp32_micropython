"""
Subrata Sarker <picklumithu@yahoo.com>
Date: 26.04.2022
Inspired from => https://RandomNerdTutorials.com
"""
def web_page():
  if led.value():
    gpio_state=""" class="red">ON"""
  else:
    gpio_state=""" class="green">OFF"""

  return html.replace("{{>gpio_state}}", gpio_state)

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(('', 80))
soc.listen(5)

while True:
  conn, addr = soc.accept()
  print('Got a connection from %s'% addr[0])
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
  if led_on == 6 and not led.value():
    print('LED ON')
    led.value(1)
  if led_off == 6 and led.value():
    print('LED OFF')
    led.value(0)
  page = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(page)
  conn.close()
