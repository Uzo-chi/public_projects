import re, pyperclip

urlRegex = re.compile(r'''(
    (http://|https://)?
    ([a-zA-Z0-9]+)
    (\.[a-zA-Z]{2,4})
    (/.*)?
    )''',re.VERBOSE)

site = str(pyperclip.paste())
print(urlRegex.findall(site))