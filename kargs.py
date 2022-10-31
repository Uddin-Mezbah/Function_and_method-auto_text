def full_name(f_name,l_name):
    name = f'{f_name} {l_name}'
    return name

name = full_name(l_name='chowdhury', f_name='choto')
#print(name)

def long_name (**kargs):
    #print(kargs)

    long_name(first= 'Dr. ', last='chowdhury',middle = 'Rahman')

def name_mixed(first,last, **name_parts):
    print(first,last,name_parts)

name = name_mixed(first='chowdhury', last='choto',middle = 'major')
#print(name)

def all_types(first,*args,**kargs):
    print(first)
    for word in args:
        print(word)
    #print(args)
    print(kargs)
    for key, value in kargs.items():
        print(key,value)

all_types('abc','ccc','dddd','eee',name='Abul',father='babul')

