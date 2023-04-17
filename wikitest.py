import wikipedia

wikipedia.set_lang('uz')

print(wikipedia.search('text'))
print(wikipedia.summary('text'))