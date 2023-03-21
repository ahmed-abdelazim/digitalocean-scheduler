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
      print(digitalocean.Volume(token=os.getenv('TOKEN'), id="a8258f70-c722-11ed-a838-0a58ac1447fa").snapshot(name="wordpress-backup-vol_"+str_date_time))
      print(digitalocean.Droplet(token=os.getenv('TOKEN'), id="203453589").take_snapshot(snapshot_name="Indian-server_"+str_date_time))
      print(digitalocean.Droplet(token=os.getenv('TOKEN'), id="340456218").take_snapshot(snapshot_name="Wordpress_"+str_date_time))
      #return {"body":  manager.get_all_droplets()[0].__dict__}
      return {"body":  "ok"}
      # return {"body": my_projects}
if __name__ == "__main__":
      main({'droplets': ['203453589','340456218']})