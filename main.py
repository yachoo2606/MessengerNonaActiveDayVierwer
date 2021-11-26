import os,json
import datetime as dt
import pandas as pd



def plot_data(messenges):
    datelist = pd.date_range(start=str(messenges[0]), end=str(messenges[-1]))
    dates = []
    for e in datelist:
        dates.append(e.date())
    #print(type(dates))
    #print(type(messenges))
    #"""
    for m in messenges:
        if m in dates:
            dates.remove(m)
    #"""
    #print(messenges)
    print(dates)
    print(len(dates))
    for day in dates:
        print(day)

    #print(type(datelist[0]))
    #counts = collections.Counter(d for d in messenges)
    #plt.hist(counts.keys(),bins=850)
    #plt.show()

def main():
    temp1 = os.listdir()
    files=[]
    for file in temp1:
        if file.endswith(".json"):
            files.append(file)
    #files.pop(0)
    #files.pop(0)
    #files.pop()
    #print(files)
    temp = []
    messenges =[]
    for file in files:
        with open(file) as file:
            position = json.load(file)
            #print(position.keys())
            for k in position['messages']:
                temp.append(k['timestamp_ms'])
        file.close()

    for v in temp:
        messenges.append(dt.datetime.fromtimestamp(int( v/ 1000.0)))

    s = {d.date() for d in messenges}
    messenges=[]
    for e in s:
        messenges.append(e)
    messenges = sorted(messenges)

    plot_data(messenges)
    #print(messenges)
    #print(len(messenges))


if __name__ == '__main__':
    main()
