### ord() / chr()
Convert between characters and ASCII codes
- `ord(char)` - character → ASCII code
- `chr(code)` - ASCII code → character
- Example: `ord('a')` → `97`, `chr(97)` → `'a'`
- Alphabet index: `ord(char) - ord('a')` → 'a'=0, 'b'=1, ...
- Alphabet count: `counts[ord(char) - ord('a')] += 1`
