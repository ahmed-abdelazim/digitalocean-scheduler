import digitalocean
import os
def main(args):
      manager = digitalocean.Manager(token=os.getenv('TOKEN'))
      my_projects = manager.get_all_projects()
      # name = args.get("name", "stranger")
      print(my_projects)
      return {"body": greeting}
      # return {"body": my_projects}
