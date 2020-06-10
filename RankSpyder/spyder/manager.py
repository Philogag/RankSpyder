from . import vjudge

def get(platform, id, passwd, newlength):
    if newlength is None:
        newlength = -1
    
    if platform == 'VJ':
        return vjudge.download_submitions(id, passwd, newlength)