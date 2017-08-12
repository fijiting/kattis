import sys

def explode(text, trigger):
    trig_len = len(trigger)
    text_len = len(text)

    if (trig_len > text_len):
        return "FRULA"
    
    remenant = ""
    lastStartIdxs = []
    startChar = trigger[0]
    
    nextToMatchIdx = 0
    nextToMatch = trigger[nextToMatchIdx]

    i = 0
    while i < text_len:
        if text[i] == startChar:
            lastStartIdxs += [i]

        if text[i] == nextToMatch:
            if (nextToMatchIdx + 1) == trig_len :
                currStartIdx = lastStartIdxs[len(lastStartIdxs) - 1]
                text = text[ : currStartIdx ] + text[ currStartIdx + trig_len : ]
                remenant = text
                text_len = len(text)
                lastStartIdxs = lastStartIdxs[: len(lastStartIdxs) - 1]
                i = currStartIdx - 1
                nextToMatchIdx = 0
                nextToMatch = trigger[nextToMatchIdx]
                
            else:
                nextToMatchIdx += 1
                nextToMatch = trigger[nextToMatchIdx]
        else:
            nextToMatchIdx = 0
            nextToMatch = trigger[nextToMatchIdx]
            if len(lastStartIdxs) != 0:
                i = lastStartIdxs[ len(lastStartIdxs) - 1]
                nextToMatchIdx = 1
                nextToMatch = trigger[nextToMatchIdx]

        i += 1
        if (i >= text_len and len(lastStartIdxs) != 0 ):
            i = lastStartIdxs[len(lastStartIdxs) - 1]
            nextToMatchIdx = 1
            nextToMatch = trigger[nextToMatchIdx]

    if remenant == "":
        return "FRULA"
    else:
        return remenant

for line in sys.stdin:
    text = line.strip('\n')
    trigger = sys.stdin.readline().strip('\n')
    print explode(text, trigger)
        
