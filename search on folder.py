import glob
import os


def countSpecificWordsInText(listOfwords, text, filename, countingList):
    for word in listOfwords:
        counter = text.count(word)
        if counter != 0:
            tempList = []
            tempList.append(filename)
            tempList.append(word)
            tempList.append(counter)
            countingList.append(tempList)


def convertIntoHtmlTable(List):
    itemsForTable = ""
    List.sort(key=lambda x: x[2], reverse=True)
    for item in List:
        itemsForTable += '<tr>'
        for i in item:
            itemsForTable += '<td> ' + str(i) + ' </td> '
        itemsForTable += '</tr>'
    html = """<!DOCTYPE html>
<html>
<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>

<h2>String Counter List</h2>

<table>
  <tr>
    <th>File Name</th>
    <th>String</th>
    <th>Count</th>
  </tr>
  """ + itemsForTable + """
</table>

</body>
</html>
"""
    file = open('logCounter.html', 'w')
    file.write(html)
    print('file created at: ', os.path.realpath(file.name))
    file.close()


strings = ''
path = ''

strings = input("Please provide array of strings separated with ',': ")

path = input("Please provide path to folder of logs: ")

strings = strings.replace(" ", "")
listOfStrings = strings.split(",")
countingList = []
for filename in glob.glob(os.path.join(path, '*.log')):
    with open(filename, 'r') as f:
        texts = f.read()
        fName = os.path.basename(f.name)
        countSpecificWordsInText(listOfStrings, texts, fName, countingList)
convertIntoHtmlTable(countingList)

