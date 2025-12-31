from mivina_api import register_command 
#decoding things
enc = {'a':'1','b':'a','c':'7','d':'*','e':'2','f':'|','g':'+','h':'q',
'i':'i','j':'s','k':'<','l':'z', 'm':'?','n':'N','o':'c', 'p':'~', 
'q':'x', 'r':'4', 's':'6', 't':'d', 'u':'0', 'v':'8', 'w':'>', 'x':',', 'y':'!',
'z':'@', ' ':'_', '.':'=', ',':'%',
'1':'#', '2':'$', '3':'^','4':'`','5':'&', '6':'/', '7':'*', '8':'(', '9':'+',
'-':'"', '/':'¼','*':'{', ':':';', '+':'b', '-':'f', '?':'j', '=': 'q', '!':'M'}
dec = {v:k for k,v in enc.items()}

def encrypt(text):
    return ''.join(enc.get(ch, '?') for ch in text) 
    
def decrypt(cipher):
    return ''.join(dec.get(ch, '?') for ch in cipher)

def minit_minit91(args, stdin):
    import minit91
    mode, *text = line.split(maxsplit=1)
    text = text[0] if text else ""
    text = text.lower()
    if "-e" in args:
        return minit91.encrypt(text)

    elif "-d" in args:
        return minit91.decrypt(text)

def init():
    register_command("mt91", minit_minit91)
