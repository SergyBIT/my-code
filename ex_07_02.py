fileName = open('mbox-short.txt')
#print(fileName)
count = 0
average = 0
for line in fileName:
    if not line.startswith('X-DSPAM-Confidence:') : continue
    average += float(line[20:-1].strip())
    count = count + 1
    #print(line.lower())
#print('done')

print('Average spam confidence:', (average/count))

#ivar = str.find('X-DSPAM-Confidence:')
#print(ivar)

#data = 'X-DSPAM-Confidence:    0.8475'
#x = fileName.find(':')
#print(x)
