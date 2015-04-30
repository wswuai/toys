
import xml.etree.ElementTree

def genElement(lists):
    assert(len(lists)%3==0)
    name = lists[0]
    params = lists[1]
    content = lists[2]
    string = ''
    string +="<%s"%name + " "

    for k,v in params.items():
        string+='%s = "%s" '%(k,v)

    if(isinstance(content, str)):
        text = content
    else:
        text = genElement(content)
    string +=">" + text + "</%s>\n"%name

    if(len(lists)<=3):
        return string
    else:
        return string + genElement(lists[3:])

def genAlfredXML(rowList):
    item = []
    for row in rowList:
        tsi = ['title',{},row['title'],'subtitle',{},row['subtitle'],'icon',{},row['icon']]
        item.extend(['item',{'uid':row['uid'],'arg':row['arg'],'autocomplete':row['autocomplete']},tsi])
    items = ['items',{},item]
    return genElement(items)

if __name__=='__main__':
    rowList = [{'uid':'123321','arg':'argsx','autocomplete':'autocompletex','icon':'icon','subtitle':'subtitle','title':'title'}]
    element = genAlfredXML(rowList)

    print(element)
