##We have a nested object. We would like a function where you pass in the object and a key and get back the value. 
#The choice of language and implementation is up to you.

#Example Input
#object = {“a”:{“b”:{“c”:”d”}}}
#key = a/b/c
#object = {“x”:{“y”:{“z”:”a”}}}
#key = x/y/z
#value = a



def nested_obj(obj,key):
    keys=key.split('/')
    #print(keys)
    value= "no value present for key"
    for k in keys:
        if not (type(obj) is dict) or (obj.get(k) is None):
            return value
        obj = obj.get(k)
    return obj
    
object = {"a":{"b":{"c":"d"}}}
key = "a/b/c"
print(nested_obj(object,key))
