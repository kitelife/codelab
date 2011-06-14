from reportlib.pdfgen import canvas

def hello():
	c = canvas.Canvas("helloworld.pdf")
	c.drawString(100,100,"Hello World")
	c.showPage()
	c.save()

hello()