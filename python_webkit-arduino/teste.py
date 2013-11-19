import signal
import sys
import os
import gtk

import time
import urllib
import cgi

from webgui import start_gtk_thread
from webgui import launch_browser
from webgui import synchronous_gtk_message
from webgui import asynchronous_gtk_message
from webgui import kill_gtk_thread

class Global(object):
    quit = False
    @classmethod
    def set_quit(cls, *args, **kwargs):
        cls.quit = True

def WrapperSaida(fun):	
    signal.signal(signal.SIGINT, Global.set_quit)
    def fun2(*args, **kwargs):
        try:
            x = fun(*args, **kwargs) 
        finally:
            kill_gtk_thread()
            Global.set_quit()
        return x
    return fun2

def CallbackURL(view, frame, req, data=None):
	uri = req.get_uri()
	splited = uri.split(':', 2)
	scheme	=	splited[0]
	data 		=	splited[1] 
	if scheme == 'callback':
		if data == '//enviarcomando':
			print uri
		return True
	else:
		return False

def main():	
	global disks
	global browser
	global web_send
	start_gtk_thread()	

	file = os.path.abspath('pagina.html')				
	uri = 'file://' + urllib.pathname2url(file)	
	browser, web_recv, web_send = synchronous_gtk_message(launch_browser)(uri,quit_function=Global.set_quit,echo=False,width=640,height=640)	#	Iniciamos e mapeamos a resposta da funcao launch_browser do script utilitario que nos retorna browser ( o webview ), web_recv ( nao utilizado, porem detecta mudancas no titulo ), web_send ( usado para enviar comandos javascript)
	browser.connect("navigation-requested", CallbackURL)
	while not Global.quit:	
		time.sleep(1)

WrapperSaida(main)()
