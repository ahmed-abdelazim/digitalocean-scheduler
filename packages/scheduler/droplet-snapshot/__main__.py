import digitalocean
import os
from datetime import datetime
def main(args):
      timestamp = datetime.now().timestamp()
      date_time = datetime.fromtimestamp(timestamp)
      str_date_time = date_time.strftime("%d-%m-%Y_%H:%M:%S")
      print("Current timestamp", str_date_time)
      # name = args.get("name", "stranger")
      #print(args.get('droplets'))
      for v in manager.get_all_volumes():
            print(digitalocean.Volume(token=os.getenv('TOKEN'), id=str(v.id)).snapshot(name=v.name+"_"+str(v.id)+"_"+str_date_time))
      for i in manager.get_all_droplets(tag_name="backup-true"):
            print(digitalocean.Droplet(token=os.getenv('TOKEN'), id=str(i.id)).take_snapshot(snapshot_name=i.name+"_"+str(i.id)+"_"+str_date_time))

      return {"body":  "ok"}
if __name__ == "__main__":
      main({'droplets': ['203453589','340456218']})