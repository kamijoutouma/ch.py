import requests, json, re

class updater:

  def findid(self):
    data = requests.get("http://st.chatango.com/js/gz/emb_perc.js").text
    return re.search("r\d+",data).group(0)

  def findweights(self):
    data = requests.get("http://st.chatango.com/h5/gz/%s/id.html"%self.ID).text.splitlines()
    print("Found server weights.")
    tags = json.loads(data[6].split(" = ")[-1])
    weights = []
    for a,b in tags["sm"]:
      c = tags["sw"][b]
      weights.append([a,c])
    return weights

  def updatech(self):
    print("Writing server weights to ch.py...")
    with open("ch.py","r+") as ch:
      rdata=ch.read()
      wdata=re.sub("tsweights = .*","tsweights = %s"%str(self.weights),rdata)
      ch.seek(0)
      ch.write(wdata)
      ch.truncate()

  def run(self):
    print("Searching for latest server weights list...")
    self.ID = self.findid()
    print("Server weight list found!")
    print("ID: "+self.ID)
    print("Retrieving server weights...")
    self.weights = self.findweights()
    #print(self.weights)
    self.updatech()
    print("The server weights are now updated for ch.py, enjoy!")

main = updater()
main.run()

