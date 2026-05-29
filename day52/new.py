#Enumerate

languages=["Spanish","English","Russian","Chinese"]

for language in languages:
    print(language)

#if i want to priint index for eac element

index=0
for language in languages:
    print(f"Index {index} and language {language}")
    index+=1

#enumerate()
#this keeps track of the index for an iterable and returns an enumerate object

print(list(enumerate(languages)))
# [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]

languages=['Spanish','English','Russian','Chinese']
for index,language in enumerate(languages):
    print(f'Index {index} and language {language}')
 