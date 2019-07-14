def delete_same(this):
    return list(set(this))


this = [1,2,3,4,3,2,1]

print(this)
print(delete_same(this))