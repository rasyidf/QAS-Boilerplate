
import telegram
from os.path import exists, join
from Sastrawi import Stemmer
def LoadTemplate(path):
    result : str
    mode : telegram.ParseMode
    
    if path.startswith("#"):
        fn = join('qasbot\\templates\\jawaban', path[1:])
    elif path.startswith("@"):
        fn = join('qasbot\\templates\\lokasi', path[1:])
    else:
        fn = join('qasbot\\templates\\utama',path)
        
    if exists(fn + '.md'):
        mode = telegram.ParseMode.MARKDOWN
        fn = fn + '.md'
    elif exists(fn + '.html'):
        mode = telegram.ParseMode.HTML
        fn = fn + '.html' 
    else:
        return "_gagal menghubungkan ke server_", telegram.ParseMode.MARKDOWN
    
    with open(fn,mode='r') as f:
        result = f.read()
    
    return result, mode