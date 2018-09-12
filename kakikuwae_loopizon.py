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
tree=ET.parse('test.xml')
root=tree.getroot()
n_root=ET.Element('root')


line1=[]
line2=[]
for e in root.getiterator():
    a=e.items()
    for b in a:
        if(b[0]=='file'):
            f=0
            for c in line1:
                if(len(b[1])-2!=b[1].rfind('.c')):
                    f=1
                    break
                elif(len(b[1])-2==b[1].rfind('.c') and c!=b[1]):
                    f=2
                    break
            if(f==0):
                line1.append(b[1])
                line2.append(0)

            
#st="<yanyan>\n"

parent_map=dict((c,p)for p in tree.getiterator() for c in p)
#def funkcall_body(fele):
    
    

def mini_clook_up(cele):
    Ystr1="funcAddr"
    Ystr2="forStatement"
    Ystr3="body"
    print (cele.tag+":"+parent_map.get(cele).tag)
    if(parent_map.get(cele).tag == "XcodeProgram"):
        return 1
    elif(parent_map.get(cele).tag == Ystr2):
        return 0
    if(parent_map.get(cele).tag == Ystr1):
        ss=parent_map.get(cele).tag.text
        if(ss==Ystr3 ):
            return 1
    return mini_clook_up(parent_map.get(cele))


#def mini_clook_down(ele,str1,str2):
    

def pospra(ele,pos_root):
    if(mini_clook_up(ele)==0):
        return 0
#   for e in list(ele):
#        if(mini_clook_down(e,str1,str2)==0):
#            return 0
    return 1


def hantei(ele,ch_root):#forStatement
    global line
    a=ele.items()
    sw=yan=0
    for b in a:
        if(b[0]=='file'):
            for sw,c in enumerate(line1):
                if(c==b[1]):
                    break
        if(b[0]=='lineno'):
            yan=int(b[1])
            
    if(ele.tag=="forStatement" and pospra(ele,ch_root)==1):
        sub=ET.SubElement(ch_root,'pragma')
        sub.set('lineno',str(yan+line2[sw]))
        sub.text="acc karnels"
        line2[sw]+=1
          

def itmm(ele,i_root):
    global line1
    global line2
    a=ele.items()
    asd=0
    sw=0
    for b in a:
        if(b[0]=='file'):
            for sw,c in enumerate(line1):
                if(c==b[1]):
                    break
    for b in a:
        if(b[0]=='lineno'):
            asd=int(b[1])
            i_root.set(b[0],str(line2[sw]+asd))
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

