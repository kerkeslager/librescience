from twisted.web.static import File
import jinja2
from klein import Klein

template_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates'),
    trim_blocks=True,
)

app = Klein()

@app.route('/script/', branch=True)
def static(request):
    return File('./script', defaultType='text/javascript')

@app.route('/')
def home(request):
    template = template_environment.get_template('index.html')
    return template.render()

if __name__ == '__main__':
    app.run('localhost', 8080)
