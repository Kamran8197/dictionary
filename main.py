lugət = {}
lugət["ad"] = "Kamran"
lugət["yas"] = 14
print(lugət)


if "ad" in lugət:
    print(lugət["ad"])


for acar in lugət.keys():
    print(acar)


for deyer in lugət.values():
    print(deyer)



for acar, deyer in lugət.items():
    print(acar, ":", deyer)



lugət.pop("yas")
print(lugət)



a = {"x": 1}
b = {"y": 2}
a.update(b)
print(a)




acar = input("Açar daxil et: ")
deyer = input("Dəyər daxil et: ")
lugət[acar] = deyer
print(lugət)


uzun_acar = max(lugət, key=len)
print(uzun_acar, ":", lugət[uzun_acar])



ededler = [v for v in lugət.values() if type(v) == int]
print(max(ededler))


print(lugət.get("ad", "Belə açar yoxdur"))

