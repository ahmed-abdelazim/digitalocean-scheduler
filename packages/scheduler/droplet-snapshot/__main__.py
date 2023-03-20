import digitalocean
import os
def main(args):
      manager = digitalocean.Manager(token=os.getenv('TOKEN'))
      my_projects = manager.get_all_projects()
      # name = args.get("name", "stranger")
      #print(args.get('droplets'))
      print(digitalocean.Volume(token=os.getenv('TOKEN'), id="a8258f70-c722-11ed-a838-0a58ac1447fa").snapshot(name="wordpress-backup-vol"))
      print(digitalocean.Droplet(token=os.getenv('TOKEN'), id="203453589").take_snapshot(snapshot_name="Indian-server"))
      print(digitalocean.Droplet(token=os.getenv('TOKEN'), id="340456218").take_snapshot(snapshot_name="Wordpress"))
      #return {"body":  manager.get_all_droplets()[0].__dict__}
      return {"body":  "ok"}
      # return {"body": my_projects}
if __name__ == "__main__":
      main({'droplets': ['203453589','340456218']})