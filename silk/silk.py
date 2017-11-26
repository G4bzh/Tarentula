import jinja2

tplLoader = jinja2.FileSystemLoader(searchpath='./templates')
tplEnv = jinja2.Environment(loader=tplLoader)

tplVars = {
    'From': 'toto@toto.com',
    'To' : 'titi@titi.com'
}

template = tplEnv.get_template( "body_extends" )
print template.render(tplVars)