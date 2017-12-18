import web
import team

urls = (
	"/(.*)", 'index',
	"/main", "main_menu"
	)

render = web.template.render("templates/")
app = web.application(urls, globals())

class index:
	def GET(self, A):
		return render.index(A)

class main_menu:
	def GET(self):
		return "BLA BLA VLA"

if __name__ == "__main__":
	app.run()
