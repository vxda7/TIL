# Backtraking

```python
procedure bt(c)
  if reject(P,c) then return
  if accept(P,c) then output(P,c)
  s ← first(P,c)
  while s ≠ NULL do
    bt(s)
    s ← next(P,s)
```

```python
function first(P, c)
  k ← length(c)
  if k = n
    then return NULL
  else return (c[1], c[2], …, c[k], 1)

function next(P, s)
  k ← length(s)
  if s[k] = m
    then return NULL
  else return (s[1], s[2], …, s[k - 1], 1 + s[k])
```

