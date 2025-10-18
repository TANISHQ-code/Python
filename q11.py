sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
res={}
# Keys to extract
keys = ["name", "salary"]
for k in keys:
    res.update({k:sample_dict[k]})
print(res)
