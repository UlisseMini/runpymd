# runpymd
*Run python blocks in markdown*

I use this all the time in my notes, where I have some calculations which I want to modify but see the results for. Copy and pasting it into ipython and back was just not good enough.

## Bugs
- When ran multiple times it just appends more results without removing past results
- If you do shell redirection wrong, eg `runpymd < file.md > file.md` you'll lose your data (because `file.md` is truncated before read)

Don't expect fixes anytime soon since I don't really use this anymore

## Example

a.md:
````
Do a complex calculation
```py
print(1e6 * 43.2 / 2)
```
````

`runpymd a.md > b.md`

b.md:
````
Do a complex calculation
```py
print(1e6 * 43.2 / 2)
```
Output:
```
21600000.0
```
````
