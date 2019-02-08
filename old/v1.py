import six

def read_AI_Type(id):
    #id from 61 ~ 76
    #讀取AI 卡電壓/電流模式
    id+="0200000004"
    id=LRC(id)
    _aitypearray = bytearray()
    _aitypearray.append(58)     #起始值

    for i in id:
        _aitypearray.append(ord(i))     #起始值

    _aitypearray.append(13)  #0D
    _aitypearray.append(10)  #0A

    return _aitypearray

def read_AI(id):
    #id from 61 ~ 76
    id+="0400000004"
    id=LRC(id)
    _readai = bytearray()
    _readai.append(58)     #起始值
    for i in id:
       _readai.append(ord(i))     #起始值

    _readai.append(13)  #0D
    _readai.append(10)  #0A

    return _readai

def read_DI(id):
    #id from 41 ~ 56
    id+="0200000008"
    id=LRC(id)
    _readdi = bytearray()
    _readdi.append(58)     #起始值
    for i in id:
        _readdi.append(ord(i))     #起始值

    _readdi.append(13)  #0D
    _readdi.append(10)  #0A

    return _readdi

def read_AO(id):
    #id from 81 ~ 96
    id+="0300050004"
    id=LRC(id)
    _readao = bytearray()
    _readao.append(58)     #起始值
    for i in id:
        _readao.append(ord(i))     #起始值

    _readao.append(13)  #0D
    _readao.append(10)  #0A

    return _readao

def read_DO(id):
    #id from 21 ~ 36
    id+="0100000004"
    id=LRC(id)

    _readdo = bytearray()
    _readdo.append(58)     #起始值
    for i in id:
        _readdo.append(ord(i))     #起始值

    _readdo.append(13)  #0D
    _readdo.append(10)  #0A
    return _readdo

def write_DO(id,data):
    #id from 21 ~ 36
    id+="060000000401"

    if len(data)<2:
        data="0"+data
    id+=data
    id=LRC(id)
    _writedo = bytearray()
    _writedo.append(58)     #起始值
    for i in id:
        _writedo.append(ord(i))     #起始值

    _writedo.append(13)  #0D
    _writedo.append(10)  #0A
    return _writedo


def EXEC_AI_ValueByCurrent(smax,smin,data):
        return (smax-smin)/16 *(data-4)+smin

def EXEC_AI_ValueByVoltage(smax,smin,data):
    return (smax-smin)/16 *(data)+smin

def LRC(protocol):
    checksum=0
    i=0
    while i<len(protocol)-1:
        checksum=checksum+int(protocol[i:i+2],16)
        i+=2

    checksum=protocol+format(255-checksum+1,"x")
    return checksum
