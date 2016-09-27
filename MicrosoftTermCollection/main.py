# coding=utf-8

import xml.etree.cElementTree as ET
import csv

tree = ET.parse('MicrosoftTermCollection.xml')
root = tree.getroot()

#       <termEntry id="14926_6">
#         <langSet xml:lang="en-US">
#           <descripGrp>
#             <descrip type="definition">To terminate abruptly, often used in reference to a program or procedure in progress.</descrip>
#           </descripGrp>
#           <ntig>
#             <termGrp>
#               <term id="6">abort</term>
#               <termNote type="partOfSpeech">Verb</termNote>
#             </termGrp>
#           </ntig>
#         </langSet>
#         <langSet xml:lang="zh-cn">
#           <ntig>
#             <termGrp>
#               <term id="23">中止</term>
#               <termNote type="partOfSpeech">Verb</termNote>
#             </termGrp>
#           </ntig>
#         </langSet>
#       </termEntry>

list = []

for termEntry in root.iter('termEntry'):
    listRow = []
    # print(termEntry.attrib)
    # print(termEntry.find('langSet').find('descripGrp').find('descrip').text)
    for langSet in termEntry.findall('langSet'):
        listRow.append(langSet.find('ntig').find('termGrp').find('term').text)
        # print(langSet.find('ntig').find('termGrp').find('term').text)
        # print(langSet.find('ntig').find('termGrp').find('termNote').text)

    list.append(listRow)

csvfile = open('terminology.csv', 'w')
with open('terminology.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerow(['en', 'zh_CN', 'pos', 'description'])
    a.writerows(list)