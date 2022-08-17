import wikipedia
import wolframalpha

query = input("Question:")

print(wikipedia.summary(query))

myappid= wolframalpha.Client('VHWW39-HAJ53UE5L2')
res = myappid.query(query)
ans= next(res.results).text
print(ans)