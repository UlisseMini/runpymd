# runpymd
*Run python blocks in markdown*

I use this all the time in my notes, where I have some calculations which I want to modify but see the results for. Copy and pasting it into ipython and back was just not good enough.


## Example

a.md:
```md
Do a complex calculation
\`\`\`py
print(1e6 * 43.2 / 2)
\`\`\`
```

`runpymd a.md > b.md`

b.md:
```md
Do a complex calculation
\`\`\`py
print(1e6 * 43.2 / 2)
\`\`\`
Output:
\`\`\`
21600000.0
\`\`\`
```
