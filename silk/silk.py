import jinja2

tplLoader = jinja2.FileSystemLoader(searchpath='./templates')
tplEnv = jinja2.Environment(loader=tplLoader)

tplVars = {
    'parts': range(1,11),
    'lines' : range(5,8),
   	'keywords' : ('cats', 'kitten', 'cat', 'pussy', 'kitty', 'puss'),
}

template = tplEnv.get_template( "body.jinja" )
print template.render(tplVars)