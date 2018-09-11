from xml.etree.ElementTree import *
import xml.etree.ElementTree as ET
from xml.dom.minidom import parse, parseString
import xml.dom.minidom as minidom
import time
import math
import sys
import argparse
import pickle
import codecs
tree=ET.parse('a.xml')
root=tree.getroot()
n_root=ET.Element('n_root')

Ystr1="funcAddr"
Ystr2="scanf"
Ystr3="forStatement"


#st="<yanyan>\n"
line=0

parent_map=dict((c,p)for p in tree.getiterator() for c in p)


def mini_clook_up(cele):
    #print (cele.tag+":"+parent_map.get(cele).tag)
    if(parent_map.get(cele).tag == "XcodeProgram"):
        return 1
    elif(parent_map.get(cele).tag == Ystr3):
        return 0
    elif(parent_map.get(cele).tag == Ystr1):
        if(parent_map.get(cele).tag.text==Ystr2):
            return 1
    else:
        return mini_clook_up(parent_map.get(cele))


#def mini_clook_down(ele,str1,str2):
    

def pospra(ele,pos_root):
    if(mini_clook_up(ele)==0):
        print(mini_clook_up(ele))
        return 0
#   for e in list(ele):
#        if(mini_clook_down(e,str1,str2)==0):
#            return 0
    return 1


def hantei(ele,ch_root):#forStatement
    global line
    a=ele.items()
    for b in a:
        if(b[0]=='lineno'):
            yan=int(b[1])
    # if(pospra(ele,ch_root)==1):
    #     print("yansu")
    if(ele.tag=="forStatement" and pospra(ele,ch_root)==1):
        sub=ET.SubElement(ch_root,'pragma')
        sub.set('lineno',str(yan+line))
        sub.text="acc karnels"
        line+=1
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        

def itmm(ele,i_root):
    global line
    a=ele.items()
    for b in a:
        if(b[0]=='lineno'):
            asd=int(b[1])
            i_root.set(b[0],str(line+asd))
        else:
            i_root.set(b[0],b[1])


def clook(ele,child_root):
    hantei(ele,child_root)
    child_root=ET.SubElement(child_root,ele.tag)
    if(ele.items()):
        itmm(ele,child_root)
    child_root.text=ele.text
    for e in list(ele):
        clook(e,child_root)        


for ele in list(root):
    clook(ele,n_root)

string = ET.tostring(n_root, 'utf-8')
pretty_string = minidom.parseString(string).toprettyxml(indent='  ')
with open('output.xml','w')as f:
    #f.write(st)
    f.write(pretty_string)

