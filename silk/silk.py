import jinja2

tplLoader = jinja2.FileSystemLoader(searchpath='./templates')
tplEnv = jinja2.Environment(loader=tplLoader)

tplVars = {
    'parts': range(1,11),
    'lines' : range(5,8),
    'transitions' : ('most of all', 'most noteworthy', 'especially relevant', 'seems like', 'maybe', 'probably', 'almost', 'as a result', 'hence', 'consequently', 'therefore', 'in conclusion', 'same', 'less', 'rather', 'while', 'yet', 'opposite', 'much as', 'either', 'because', 'so', 'due to', 'while', 'since', 'therefore', 'and', 'first of all', 'also', 'another', 'furthermore', 'finally', 'in addition'),
    'verbs' : ('catch', 'concentrate on', 'devote oneself', 'follow', 'get a load of', 'hear', 'hearken', 'heed', 'keep one\'s eye on', 'lend an ear', 'listen', 'listen up', 'look after', 'look on', 'mark', 'mind', 'note', 'notice', 'observe', 'occupy oneself with', 'pay heed', 'pick up', 'regard', 'see to', 'watch'),
	'pronouns' : ('this', 'that', 'those'),
	'adjectives' : ('absurd', 'batty', 'boffo', 'camp', 'comical', 'crazy', 'dippy', 'diverting', 'dizzy', 'droll', 'entertaining', 'facetious', 'farcical', 'flaky', 'fool', 'foolheaded', 'for grins', 'freaky', 'funny', 'gelastic', 'goofus', 'goofy', 'gump', 'horse\'s tail', 'humorous', 'ironic', 'jerky', 'jocular', 'joking', 'joshing', 'laughable', 'light', 'loony', 'ludicrous', 'nutty', 'off the wall', 'priceless', 'ridiculous', 'risible'),   
	'keywords' : ('cats', 'kitten', 'cat', 'pussy', 'kitty', 'puss'),
}

template = tplEnv.get_template( "body_extends" )
print template.render(tplVars)